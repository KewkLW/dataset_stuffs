# checks your images for the images SDXL likes and then spits out a nice json file to be processed later.
# In order to minimize crops, I added the full list of dimensions that are in the SDXL paper to fall back on.
# https://arxiv.org/abs/2307.01952

import os
import json
from PIL import Image
from tqdm import tqdm
import concurrent.futures

# List of valid dimensions
additional_resolutions = [{"width": 1024, "height": 1024}, {"width": 2048, "height": 512}, {"width": 1984, "height": 512}, {"width": 1920, "height": 512}, {"width": 1856, "height": 512}, {"width": 1792, "height": 576}, {"width": 1728, "height": 576}, {"width": 1664, "height": 576}, {"width": 1600, "height": 640}, {"width": 1536, "height": 640}, {"width": 1472, "height": 704}, {"width": 1408, "height": 704}, {"width": 1344, "height": 704}, {"width": 1344, "height": 768}, {"width": 1280, "height": 768}, {"width": 1216, "height": 832}, {"width": 1152, "height": 832}, {"width": 1152, "height": 896}, {"width": 1088, "height": 896}, {"width": 1088, "height": 960}, {"width": 1024, "height": 960}, {"width": 960, "height": 1024}, {"width": 960, "height": 1088}, {"width": 896, "height": 1088}, {"width": 896, "height": 1152}, {"width": 832, "height": 1152}, {"width": 832, "height": 1216}, {"width": 768, "height": 1280}, {"width": 768, "height": 1344}, {"width": 704, "height": 1408}, {"width": 704, "height": 1472}, {"width": 640, "height": 1536}, {"width": 640, "height": 1600}, {"width": 576, "height": 1664}, {"width": 576, "height": 1728}, {"width": 576, "height": 1792}, {"width": 512, "height": 1856}, {"width": 512, "height": 1920}, {"width": 512, "height": 1984}, {"width": 512, "height": 2048}]
valid_dimensions = [
    (1024, 1024),
    (1152, 896),
    (896, 1152),
    (1216, 832),
    (832, 1216),
    (1344, 768),
    (768, 1344),
    (1536, 640),
    (640, 1536),
]


def check_image(image_path):
    # Open the image
    image = Image.open(image_path)
    width, height = image.size
    ratio = width / height

    # Check if the image's dimensions are in the valid list
    if (width, height) not in valid_dimensions:
        best_match = None
        needs_crop = "no"

        # Check for closest matching valid dimension
        for valid_width, valid_height in valid_dimensions:
            valid_ratio = valid_width / valid_height
            if ratio == valid_ratio:
                # Check if upscaling is possible
                if width <= valid_width and height <= valid_height:
                    best_match = (valid_width, valid_height)
                    break

        # If no match found, try additional resolutions before cropping
        if best_match is None:
            for res in additional_resolutions:
                valid_width, valid_height = res["width"], res["height"]
                valid_ratio = valid_width / valid_height
                if ratio == valid_ratio:
                    if width <= valid_width and height <= valid_height:
                        best_match = (valid_width, valid_height)
                        break

        # Mark for cropping if no match found in additional resolutions
        if best_match is None:
            needs_crop = "yes"
            return {
                "filename": os.path.basename(image_path),
                "path": image_path,
                "dimension": (width, height),
                "resize_ratio": None,
                "target_dimension": None,
                "needs_crop": needs_crop
            }

        resize_ratio = best_match[0] / width if best_match[0] / width == best_match[1] / height else None

        return {
            "filename": os.path.basename(image_path),
            "path": image_path,
            "dimension": (width, height),
            "resize_ratio": resize_ratio,
            "target_dimension": best_match,
            "needs_crop": needs_crop
        }
    return None

def check_image(image_path):

  image = Image.open(image_path)
  width, height = image.size
  ratio = width / height

  for valid_width, valid_height in valid_dimensions:
    if ratio == valid_width / valid_height:
      needs_upscale = width < valid_width or height < valid_height   
      needs_downscale = width > valid_width or height > valid_height
      return {
        "filename": os.path.basename(image_path),
        "path": image_path, 
        "dimension": (width, height),
        "resize_ratio": valid_width / width,
        "target_dimension": (valid_width, valid_height),
        "needs_upscale": needs_upscale,
        "needs_downscale": needs_downscale,
        "needs_crop": "no"
      }

  for res in additional_resolutions:
    valid_width, valid_height = res["width"], res["height"]  
    if ratio == valid_width / valid_height:
      needs_upscale = width < valid_width or height < valid_height
      needs_downscale = width > valid_width or height > valid_height
      return {
        "filename": os.path.basename(image_path),
        "path": image_path,
        "dimension": (width, height), 
        "resize_ratio": valid_width / width,
        "target_dimension": (valid_width, valid_height),
        "needs_upscale": needs_upscale,
        "needs_downscale": needs_downscale,
        "needs_crop": "no"
      }
        
  closest_valid = min(valid_dimensions, key=lambda x:abs(x[0]/x[1]-ratio)) 
  resize_ratio = closest_valid[0] / width
  target_dimension = closest_valid
  needs_upscale = width < closest_valid[0] or height < closest_valid[1]
  needs_downscale = width > closest_valid[0] or height > closest_valid[1]

  return {
    "filename": os.path.basename(image_path),
    "path": image_path,
    "dimension": (width, height),
    "resize_ratio": resize_ratio,
    "target_dimension": target_dimension,
    "needs_upscale": needs_upscale,
    "needs_downscale": needs_downscale, 
    "needs_crop": "yes"
  }

def main(directory):
    # Gather all image paths
    image_paths = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_paths.append(os.path.join(root, filename))

    results = []
    crops_needed = 0
    # Process images in parallel with progress bar
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for result in tqdm(executor.map(check_image, image_paths), total=len(image_paths)):
            if result:
                results.append(result)
                if result["needs_crop"] == "yes":
                    crops_needed += 1

    # Write results to a JSON file
    with open('image_dimensions.json', 'w') as file:
        json.dump(results, file, indent=4)

    print(f"{len(results)} images do not meet the criteria. {crops_needed} crops are needed. Details saved in 'image_dimensions.json'.")

if __name__ == '__main__':
    main(r'c:\datasets\or\some\shit')