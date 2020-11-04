from PIL import Image
import os
from os import listdir
from os.path import isfile, join, abspath, dirname


def get_list_images(path: str, expansions: list):
    list_images = []

    for file_ in listdir(path):

        if file_.endswith(tuple(expansions)) and isfile(join(path, file_)):
            list_images.append(join(path, file_))

    return list_images


def compression_images(image=None, images_dir=None, expansions=['.png,', '.jpg', 'jpeg', 'JPG'], crop=2):
    """
    Keyword arguments:
    image -- path certain image (default: None)
    images_dir -- path directory with images (default: None)
    expansions -- expansions images, which to be processed
    crop -- how many times the pictures will be compressed

    return: "IT IS DONE" or "INSUFFICIENT RESOURCES"
    """

    current_dir = os.path.join(dirname(abspath(__file__)), 'compressed_images')
    os.makedirs(current_dir)

    if image and not images_dir:
        images = [image]
    elif not image and images_dir:
        images = get_list_images(path=images_dir, expansions=expansions)
    elif image and images_dir:
        images = get_list_images(path=images_dir, expansions=expansions)
        images.append(image)
    else:
        return "INSUFFICIENT RESOURCES"

    for idx, img in enumerate(images):
        print(idx)
        img_obj = Image.open(img)
        # I downsize the image with an ANTIALIAS filter (gives the highest quality)
        width, height = img_obj.size
        foo = img_obj.resize((width // crop, height // crop), Image.ANTIALIAS)
        foo.save(f"{current_dir}/{idx}.jpg", optimize=True, quality=85)

    return "IT IS DONE"
