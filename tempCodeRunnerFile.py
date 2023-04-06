cred = credentials.Certificate('/Users/rohanpadhye/Desktop/Projects/DSA/doorbell decode/firebase.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'smartdoorbell-5c897.appspot.com'
})
firebase_admin.initialize_app(cred)