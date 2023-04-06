import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import requests

# Initialize the Firebase Admin SDK
cred = credentials.Certificate('/Users/rohanpadhye/Desktop/Projects/smart-doorbell/firebase.json')
firebase_admin.initialize_app(cred)

# Get a reference to the KnownFaces document in the User1 collection
db = firestore.client()
doc_ref = db.collection('User1').document('KnownFaces')

# Get the imgDet array from the KnownFaces document
img_det_arr = doc_ref.get().to_dict()['imgDet']

# Download each image in the imgDet array
for img_det in img_det_arr:
    img_link = img_det['imgLink']
    img_name = img_det['name'] # Extract the image name from the imgDet map
    img_path = f'/Users/rohanpadhye/Desktop/Projects/smart-doorbell/TrainImages/faces/{img_name}.jpg' # Set the path to the local folder
    response = requests.get(img_link)
    with open(img_path, 'wb') as f:
        f.write(response.content)