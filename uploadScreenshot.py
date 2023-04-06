import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore,storage
import time
import datetime
import base64
from PIL import Image
import cv2
import random
import string 



def uploadSS():
        
    # Open the original image
    db = firestore.client()
    bucket = storage.bucket()
    date = datetime.datetime.now()
    unix_time = datetime.datetime.timestamp(date)*1000


    image_path = '/Users/rohanpadhye/Desktop/Projects/smart-doorbell/TestImages/saved_img.jpg'
    uploadImgName= ''.join(random.choices(string.ascii_uppercase +string.digits, k=6))
    blob = bucket.blob(f'files/{uploadImgName}.jpg')
    blob.upload_from_filename(image_path)
    blob.make_public()
    # Get the download URL of the uploaded image
    download_url = blob.public_url

    doc_ref = db.collection('User1').document('images')
    new_map = {
        'imgLink': download_url,
        'name': 'unknown',
        'sent':False,
        'timestamp':int(unix_time)
    }


    doc_ref.update({
        'imgDet': firestore.ArrayUnion([new_map])
    })
    
