#specify indicies (from AGAR_id_list.md) and this will move from dataset to "use" folder
#after which you can use AGAR_trainValPart.py to use values contained in the "training_lists" folder
import os
import shutil
from tqdm import tqdm

start_number = 12994  # Replace with your desired start number
end_number =  17417   # Replace with your desired end number

# all "countable" images save for vague
# 309-1302
# 2712-8709
# 12994 - 17417

# Source directory where images and labels are located
# source_directory = "./AGAR_dataset/dataset/"
source_directory = "C:/Users/precisionag/Documents/bacteria/johnBacteria/AGAR_dataset/dataset/"

# Destination directory where you want to move image/label pairs
destination_directory = "C:/Users/precisionag/Documents//bacteria/johnBacteria/AGAR_dataset/use/"

# Iterate through the range of numbers
for number in tqdm(range(start_number, end_number + 1)):
    # Construct the source file paths for image and label
    image_file = os.path.join(source_directory, f"{number}.jpg")
    label_file = os.path.join(source_directory, f"{number}.json")

    # Move the image and label files into the destination folder
    shutil.copy(image_file, os.path.join(destination_directory, f"{number}.jpg"))
    shutil.copy(label_file, os.path.join(destination_directory, f"{number}.json"))

print("Done!")