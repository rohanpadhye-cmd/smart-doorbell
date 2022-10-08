import os, io
from google.cloud import vision
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'googleapi.json'
client = vision.ImageAnnotatorClient()

file_name = 'zomato.webp'
image_folder = './images/'
image_path = os.path.join(image_folder, file_name)

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)
response = client.logo_detection(image=image)
logos = response.logo_annotations
print('Logo Description:', logos.description)