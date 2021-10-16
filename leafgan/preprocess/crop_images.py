import glob
import os
import image_slicer
from tqdm import tqdm

ORIGINAL_DATASET_DIR_PATH = '../dataset/original'
CROPPED_DATASET_DIR_PATH = '../dataset/cropped'

for file_path in tqdm(glob.glob('{}/**/*.jpg'.format(ORIGINAL_DATASET_DIR_PATH), recursive=True)):
    file_name = os.path.basename(file_path)
    print(file_name)
    tiles = image_slicer.slice(file_path, 9, save=False)
    image_slicer.save_tiles(tiles, directory=CROPPED_DATASET_DIR_PATH, prefix=file_name[:-4], format='jpeg')
