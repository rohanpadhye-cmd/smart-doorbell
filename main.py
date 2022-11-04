# import face_encodings
import cv2 
import os 
import face_encodings as FE
from gtts import gTTS
import oneshot 
# import pyttsx3
import datetime;
  

# cred = credentials.RefreshToken('firebase.json')
# default_app = firebase_admin.initialize_app(cred)



directory = r'/Users/rohanpadhye/Desktop/Projects/smart-doorbell/TestImages'
os.chdir(directory)



def announce(name):
    announcement=''
    if(name=='Unknown' or not name):

        Name =oneshot.predict(0)
        if (Name==None):
            os.system("afplay " + "unknown.mp3")
            return 0
        else:
            announcement=Name+" delivery partner has arrived on your doorstep."
    else: 
        announcement=name+' is on your doorstep.'
    return announcement
    


key = cv2. waitKey(1)
webcam = cv2.VideoCapture(1)
while True:
    try:
      
        check, frame = webcam.read()
        # print(check) #prints true as long as the webcam is running
        # print(frame) #prints matrix values of each framecd 
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'): 
            
            
            
            
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            # webcam.release()
            img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Resizing image to 28x28 scale...")
            img_ = cv2.resize(gray,(28,28))
            print("Resized...")
            img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
            print("Image saved!")
            os.system("afplay " + "bell.mp3")
            a=announce(FE.processImg())
            if a != 0:
                print("Output: ")
                print(a)
                ct = datetime.datetime.now()
                print(ct)
                voice=gTTS(text=a, lang='en', slow=False)
                voice.save("guestName.mp3")
                os.system("afplay " + "guestName.mp3")

            continue
            
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
        
    except(KeyboardInterrupt):
        print("Turning off camera.")


