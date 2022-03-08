
from celery import shared_task
import os
from zipfile import ZipFile
from PIL import Image
from django.conf import settings


@shared_task
def make_thumbnails(file_path, thumbnails=[]):
    os.chdir(settings.IMAGES_DIR)
    path, file = os.path.split(file_path)
    file_name, extention = os.path.splitext(file)

    zip_file = f"{file_name}.zip"
    results = {'archive_path': f"{settings.MEDIA_URL}images/{zip_file}"}
    try:
        img = Image.open(file_path)
        zipper = ZipFile(zip_file, 'w')
        zipper.write(file)
        os.remove(file_path)
        for width, height in thumbnails:
            img_copy = img.copy()
            img_copy.thumbnail((width, height))
            thumbnail_file = f'{file_name}_{width}x{height}.{extention}'
            img_copy.save(thumbnail_file)
            zipper.write(thumbnail_file)
            os.remove(thumbnail_file)

        img.close()
        zipper.close()
    except IOError:
        print(IOError)

    return results

# test
# @shared_task
# def add_task(x, y):
#    return x+y
