
import pyttsx3
import os
# import face_encodings
import cv2 


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
                engine = pyttsx3.init() 
                volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
                print (volume)                        #printing current volume level
                engine.setProperty('volume',1.0) 
                rate = engine.getProperty('rate')   # getting details of current speaking rate
                print (rate)                        #printing current voice rate
                engine.setProperty('rate', 70) 
                engine.say("Rohan")
                engine.runAndWait()
                engine.stop()
                print("sss")

            
            
            
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
        
    except(KeyboardInterrupt):
        print("Turning off camera.")














# for x in range(3):
#     engine = pyttsx3.init() 
#     volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#     print (volume)                        #printing current volume level
#     engine.setProperty('volume',1.0) 
#     rate = engine.getProperty('rate')   # getting details of current speaking rate
#     print (rate)                        #printing current voice rate
#     engine.setProperty('rate', 70) 
#     engine.say("Rohan")
#     engine.runAndWait()
#     engine.stop()
#     print("sss")

