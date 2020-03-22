import os
import csv
from collections import defaultdict
from PIL import Image, ImageFilter
# from cv2 import *



BASE_FOLDER="../../five-video-classification-methods/data/"

def get_all_zip_files(base_folder):
	onlyfiles = [os.path.join(base_folder, f)\
		for f in os.listdir(base_folder) \
		if os.path.isfile(os.path.join(base_folder, f)) \
		and f.endswith('.zip')]
	return onlyfiles

def analyse_files(base_folder, folder_list):
	for folder_name in folder_list:
		folder_path = os.path.join(base_folder, folder_name)
		if(os.path.isdir(folder_path)):
			file_list = os.listdir(folder_path)
			print(folder_name, len(file_list))
	return

def analyse_csv(csv_path):
	with open(csv_path, 'rb') as csvfile:
		csv_row = csv.reader(csvfile, delimiter=' ', quotechar='|')
		list_info = defaultdict(lambda: 0)
		# list_info[csv_row[0]] = 
		for row in csv_row:
			print ', '.join(row)
	return

def analyse_dataset(base_folder):
	train_folder_list = os.listdir(os.path.join(base_folder,"train"))
	test_folder_list = os.listdir(os.path.join(base_folder,"test"))
	analyse_files(os.path.join(base_folder,"train"), train_folder_list)
	analyse_files(os.path.join(base_folder,"test"), test_folder_list)

	# print(train_folder_list)
	# print(test_folder_list)
	return

# analyse_csv(os.path.join(BASE_FOLDER,'data_file.csv'))
im = Image.open( "../../five-video-classification-methods/data/train/BenchPress/v_BenchPress_g09_c01-0001.jpg" )
print(im._getexif())
print(im.format, im.size, im.mode)

# analyse_dataset(BASE_FOLDER)
