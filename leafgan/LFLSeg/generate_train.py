import glob

IMAGE_DIR_LIST = [
    ('full_leaf', 0),
    ('partial_leaf', 1),
    ('non_leaf', 2)
]

IMAGE_LIST_FILE_PATH = '../dataset/lflseg_train.txt'

rows = []
for image_dir, dir_suffix in IMAGE_DIR_LIST:
    for file_path in glob.glob('../dataset/cropped/{}/*.jpg'.format(image_dir)):
        rows.append('{}, {}\n'.format(file_path, dir_suffix))

with open(IMAGE_LIST_FILE_PATH, 'w') as f:
    f.writelines(rows)