import face_recognition
import time
import cv2
import os
from dotenv import load_dotenv
load_dotenv()

known_image = face_recognition.load_image_file(os.getenv('USER_IMAGE_PATH'))
vid = cv2.VideoCapture(0) 
biden_encoding = face_recognition.face_encodings(known_image)[0]
  
count = 0
while(True): 
    time.sleep(5)
    ret, frame = vid.read()  
    if(ret):
        try:
            unknown_encoding = face_recognition.face_encodings(frame)[0]
            results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
            print(results[0],count)
            if(str(results[0]) == 'False'):
                count += 1
        except:
            count += 1
        if count == 2 :
            count = 0
            os.popen(os.getenv('LOCK_COMMAND'))
            continue

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

  
vid.release() 
cv2.destroyAllWindows() 
