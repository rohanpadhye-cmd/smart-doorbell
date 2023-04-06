import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import base64
import os 

# Use a service account
cred = credentials.Certificate('/Users/rohanpadhye/Desktop/Projects/smart-doorbell/firebase.json')
firebase_admin.initialize_app(cred)

# Initialize Firestore database
db = firestore.client()

# Retrieve image string from Firebase
doc_ref = db.collection(u'User1').document(u'KnownFaces')
doc = doc_ref.get()
image_str = doc.to_dict()['imgDet']
img2=image_str[0]["imgLink"]

data_url = img2

# Extract the base64-encoded image data from the data URL
image_data = data_url.split(',')[1]

# Decode the base64-encoded image data into a bytes object
image_bytes = base64.b64decode(image_data)
directory = r'/Users/rohanpadhye/Desktop/Projects/smart-doorbell/TrainImages/faces'
os.chdir(directory)
# Save the image to a file
with open(image_str[0]["name"]+'.jpg', 'wb') as f:
    f.write(image_bytes)
    