import firebase_admin
from firebase_admin import credentials
import os
import requests

# Initialize the Firebase Admin SDK
# Get a reference to the KnownFaces document in the User1 collection

def emptyFolder(): 
    folder_path = "/Users/rohanpadhye/Desktop/Projects/smart-doorbell/TrainImages/cloud"
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))



def updateFaces(db):
    doc_ref = db.collection('User1').document('KnownFaces')

    # Get the imgDet array from the KnownFaces document
    img_det_arr = doc_ref.get().to_dict()['imgDet']

    # Download each image in the imgDet array
    for img_det in img_det_arr:
        img_link = img_det['imgLink']
        img_name = img_det['name'] # Extract the image name from the imgDet map
        img_path = f'/Users/rohanpadhye/Desktop/Projects/smart-doorbell/TrainImages/cloud/{img_name}.jpg' # Set the path to the local folder
        response = requests.get(img_link)
        with open(img_path, 'wb') as f:
            f.write(response.content)
            