
import json
import os
from tqdm import tqdm
from PIL import Image, ImageDraw
import time



base_path =  "C:/Users/precisionag/Documents/bacteria/johnBacteria/AGAR_dataset/test/"
json_path = os.path.join(base_path, "json/")
png_path = os.path.join(base_path, "jpg/")


# AGAR_dataset |
#              -use (useable data)
#                 -all (not val or train)
#                     txt (yolo annotations extracted from neurosys json files)
#                     json (neurosys json files)
#                     jpg (images)

with open(os.path.join(json_path, "test.json"), 'r') as json_file:
    json_file_contents = json_file.read()
    parsed_json = json.loads(json_file_contents)

image = Image.open(os.path.join(png_path, str(parsed_json["sample_id"]) + ".jpg" ))
image_width, image_height = image.size

draw = ImageDraw.Draw(image)

x_offset = (.0135 * image_width)
y_offset = (.011 * image_height)

for label in parsed_json["labels"]:
    #create a box and draw it on on the image. 
    x0 =  int((label["x"] - label["width"]/2) + x_offset)
    y0 =  int((label["y"] - label["height"]/2) + y_offset)
    x1 =  int((label["x"] + label["width"]/2) + x_offset)
    y1 =  int((label["y"] + label["height"]/2) + y_offset)
    draw.rectangle([x0, y0, x1, y1], outline = (0, 255, 0), width = 2)
    print(str(x0))
image.save("test.jpg")  



