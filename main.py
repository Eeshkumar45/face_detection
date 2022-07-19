import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)        #"./one.mp4")#"C:\\Users\\soumy\\Desktop\\22\\dbms\\vids\\two.mp4")
pTime=1

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()


while True:
  success,img = cap.read()

  imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
  results = faceDetection.process(imgRGB)
  
  if results.detections:
    for id,detection in enumerate(results.detections):
      mpDraw.draw_detection(img,detection)

  cTime = time.time()
  fps = 1/(cTime-pTime)
  pTime = cTime
  cv2.putText(img,f'FPS : {int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),2)
  cv2.imshow("image",img)
  F = cv2.waitKey(1)

  if F == ord('q') or F == ord('Q'): #Wait for the user to press 'q' key to stop the recording
      break