# Importing required libraries
from typing import List
import requests
import json
import os
from tqdm import tqdm
from PIL import Image

# Constants
IMAGE_DIMENSIONS_JSON_PATH = "c:\\datasets\\image_dimensions.json"
OUTPUT_DIR = "c:\\cookies\\and\\cream"
# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Function to process images
def process_images(image_list: List[dict]):
    # Iterate through images with progress bar
    for image_details in tqdm(image_list, desc="Processing Images"):
        # Check for upscale and downscale needs
        needs_upscale = image_details["needs_upscale"]
        needs_downscale = image_details["needs_downscale"]
        needs_crop = image_details["needs_crop"]
        
        # Open image
        image_path = image_details["path"]
        image = Image.open(image_path)
        
        # Upscale or downscale
        if needs_upscale or needs_downscale:
            target_width, target_height = image_details["target_dimension"]
            image = image.resize((target_width, target_height), Image.LANCZOS)
        
        # Crop if needed
        if needs_crop == "yes":
            target_width, target_height = image_details["target_dimension"]
            image = image.crop((0, 0, target_width, target_height))
        
        # Save processed image
        output_path = os.path.join(OUTPUT_DIR, image_details["filename"])
        image.save(output_path)

# Function to load JSON file
def load_json_file(file_path: str) -> list:
    with open(file_path, 'r') as file:
        return json.load(file)

# Main function
def main():
    # Load image dimensions from JSON file
    image_list = load_json_file(IMAGE_DIMENSIONS_JSON_PATH)
    
    # Process images
    process_images(image_list)
    
    print(f"Processing completed. Check the output directory: {OUTPUT_DIR}")

# Run the script
if __name__ == "__main__":
    main()