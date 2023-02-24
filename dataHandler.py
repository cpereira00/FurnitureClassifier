import os
import shutil
from PIL import Image

def copy_images(src_dir, filenames, dest_dir, class_dir):
    for filename in filenames:
        src = os.path.join(src_dir, filename)
        dest = os.path.join(dest_dir, class_dir, filename)
        shutil.copy(src, dest)

# split a directory into training, testing, and validation sets
def split_dataset(src_dir, train_ratio, test_ratio, val_ratio, class_dir):
    filenames = os.listdir(src_dir)
    num_files = len(filenames)

    train_size = int(train_ratio * num_files)
    test_size = int(test_ratio * num_files)
    val_size = int(val_ratio * num_files)

    train_filenames = filenames[:train_size]
    test_filenames = filenames[train_size:train_size + test_size]
    val_filenames = filenames[train_size + test_size:train_size + test_size + val_size]

    copy_images(src_dir, train_filenames, train_dir, class_dir)
    copy_images(src_dir, test_filenames, test_dir, class_dir)
    copy_images(src_dir, val_filenames, val_dir, class_dir)

def resize_images(directory):
    for subdir, dirs, files in os.walk(directory):
        for filename in files:
            image_path = os.path.join(subdir, filename)
            with Image.open(image_path) as img:
                img = img.resize((80, 80))
                img.save(image_path)


if __name__ == '__main__':

    dataset_dir = './Dataset'
    chair_dir = os.path.join(dataset_dir, 'Chair')
    sofa_dir = os.path.join(dataset_dir, 'Sofa')
    bed_dir = os.path.join(dataset_dir, 'Bed')

    train_dir = os.path.join(dataset_dir, 'train')
    test_dir = os.path.join(dataset_dir, 'test')
    val_dir = os.path.join(dataset_dir, 'val')

    # Create the training, testing, and validation directories if they don't exist
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)

    # Create subdirectories for each class in the training, testing, and validation directories
    for class_dir in ['chair', 'sofa', 'bed']:
        os.makedirs(os.path.join(train_dir, class_dir), exist_ok=True)
        os.makedirs(os.path.join(test_dir, class_dir), exist_ok=True)
        os.makedirs(os.path.join(val_dir, class_dir), exist_ok=True)

    split_dataset(chair_dir, 0.7, 0.2, 0.1, 'chair')
    split_dataset(sofa_dir, 0.7, 0.2, 0.1, 'sofa')
    split_dataset(bed_dir, 0.7, 0.2, 0.1, 'bed')

    resize_images(train_dir)
    resize_images(test_dir)
    resize_images(val_dir)