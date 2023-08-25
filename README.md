## SDXL Dimension JSON Output (sdxl_dimension_json_output.py)
Checks your images for the images SDXL likes and then spits out a nice json file to be processed later.<br>
In order to minimize crops, I added the full list of dimensions that are in the SDXL paper to fall back on.<br>
https://arxiv.org/abs/2307.01952<br>

# Useage
Change main(r'c:\datasets\or\some\shit') to your image directory run the script and it will output the json to the same directory as the script. 
