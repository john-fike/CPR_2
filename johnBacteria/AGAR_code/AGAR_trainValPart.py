#grab files contained in the given train and val indicies 
#put them in use/train and use/val
import os
import re
import shutil
from tqdm import tqdm

# Source directory where images and labels are located
# source_directory = "./AGAR_dataset/dataset/use"
use_directory = "C:/Users/precisionag/Documents/bacteria/johnBacteria/AGAR_dataset/use/"
all_data_directory = os.path.join(use_directory, "all/")
train_data_directory = os.path.join(use_directory, "train/")
val_data_directory =  os.path.join(use_directory, "val/")

train_list_file = "C:/Users/precisionag/Documents/bacteria/johnBacteria/AGAR_dataset/training_lists/lower_resolution_train.txt" 
val_list_file = "C:/Users/precisionag/Documents/bacteria/johnBacteria/AGAR_dataset/training_lists/lower_resolution_val.txt" 

file_numbers = []

with open (train_list_file, 'r') as train_list:
    train_list_contents = train_list.read()

file_numbers = re.findall(r'\d+', train_list_contents)
file_numbers = [int(num) for num in file_numbers]    #make sure all numbers are ints

for file_number in tqdm(file_numbers):
    image_file = os.path.join(all_data_directory, f"{file_number}.jpg")
    label_file = os.path.join(all_data_directory, f"{file_number}.json")
    shutil.move(image_file, train_data_directory)
    shutil.move(label_file, train_data_directory)

with open (val_list_file, 'r') as val_list:
    val_list_contents = val_list.read()

file_numbers = re.findall(r'\d+', val_list_contents)
file_numbers = [int(num) for num in file_numbers]    #make sure all numbers are ints

for file_number in tqdm(file_numbers):
    image_file = os.path.join(all_data_directory, f"{file_number}.jpg")
    label_file = os.path.join(all_data_directory, f"{file_number}.json")
    shutil.move(image_file, val_data_directory)
    shutil.move(label_file, val_data_directory)



print("Done!")