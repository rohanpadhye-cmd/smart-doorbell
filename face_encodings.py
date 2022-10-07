import face_recognition
import cv2
import os
import numpy as np

rohan_image = face_recognition.load_image_file("TrainImages/rohan.jpg")
rohan_face_encoding = face_recognition.face_encodings(rohan_image)[0]

# Load a second sample picture and learn how to recognize it.
raghu_image = face_recognition.load_image_file("TrainImages/raghu.png")
raghu_face_encoding = face_recognition.face_encodings(raghu_image)[0]


# Load a second sample picture and learn how to recognize it.
omkar_image = face_recognition.load_image_file("TrainImages/omkar.jpeg")
omkar_face_encoding = face_recognition.face_encodings(omkar_image)[0]



known_face_encodings = [
  
    rohan_face_encoding,
    raghu_face_encoding,
    omkar_face_encoding,
   
    
]
known_face_names = [
  
    "Rohan Padhye",
    "Raghuttam Parvatikar",
    "Omkar Pawar",

]


face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


directory = r'/Users/rohanpadhye/Desktop/Projects/smart-doorbell/TestImages'
os.chdir(directory)

frame = cv2.imread('saved_img.jpg', cv2.IMREAD_UNCHANGED)

def processImg():
    frame = cv2.imread('saved_img.jpg', cv2.IMREAD_UNCHANGED)
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        face_names.append(name)
    if face_names:
        return face_names[0]
    return face_names