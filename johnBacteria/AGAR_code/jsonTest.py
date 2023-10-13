import json
import os
from tqdm import tqdm
from PIL import Image

# Open the image
# image = Image.open("your_image.jpg")  # Replace with the path to your image

# # Get the dimensions
# width, height = image.size

# print(f"Image Dimensions - Width: {width}, Height: {height}")


use_path =  "C:/Users/precisionag/Documents/bacteria/johnBacteria/AGAR_dataset/test/"
json_path = os.path.join(use_path, "json/")
txt_path = os.path.join(use_path, "txt/")
png_path = os.path.join(use_path, "jpg/")

# AGAR_dataset |
            #  -use (useable data)
                # -all (not val or train)
                    #txt (yolo annotations extracted from neurosys json files)
                    #json (neurosys json files)
                    #jpg (images)

if os.path.exists(json_path) and os.path.isdir(json_path):
    for json_file_name in tqdm(os.listdir(json_path)):
        if json_file_name.endswith(".json"):
            file_path = os.path.join(json_path, json_file_name)
            try:
                with open(os.path.join(json_path, json_file_name), "r") as json_file:
                    json_file_contents = json_file.read()
                    parsed_json = json.loads(json_file_contents)

                    image = Image.open(os.path.join(png_path, str(parsed_json["sample_id"]) + ".jpg" ))
                    image_width, image_height = image.size

                    with open ((os.path.join(txt_path,str(parsed_json["sample_id"]))+".txt") , 'w+') as output_file:
                        for label in parsed_json["labels"]:
                            output_file.write("0 " + str(label["x"]/image_width) + " " + str(label["y"]/image_height) + " " + str(label["width"]/image_width) + " " + str(label["height"]/image_height) + "\n")
                


            except Exception as e:
                print("Could not create YOLO label for file: " + json_file_name + " because of exception: " + str(e))
else:
    print(f"The folder '{json_path}' does not exist.")




