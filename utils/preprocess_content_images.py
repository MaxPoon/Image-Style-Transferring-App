from concurrent.futures import ProcessPoolExecutor, wait
from os import listdir
from PIL import Image


def resize_and_save_image(image_name):
    image = Image.open(src_dir+image_name)
    image = image.resize(target_size)
    image.save("./content_images/"+image_name, "JPEG")


src_dir = input("Source directory: ")
if not src_dir.endswith('/')
    src_dir += '/'
target_size = (224, 224)
images = listdir(src_dir)
images = [image for image in images if image.endswith('.JPEG')]
pool = ProcessPoolExecutor()
tasks = [pool.submit(resize_and_save_image, image) for image in images]
wait(tasks)
