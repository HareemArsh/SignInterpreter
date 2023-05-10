from HandTrackingModule import HandDetector
import cv2
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
detector = HandDetector(detectionCon=0.8, maxHands=2)
upCount=0 # Count of Index Fingure UPs
checkAgain=True
while True:
    success, img = cap.read()
    img=cv2.flip(img, 1)
    hands, img = detector.findHands(img,flipType=False)  # with draw
    # hands = detector.findHands(img, draw=False)  # without draw

    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        tipy=lmList1[8][1] #8 for tip of index finger, 1 for y coordinate
        pipy=lmList1[6][1] #6 for pip of index finger, 1 for y coordinate
        if tipy<pipy and checkAgain:
            upCount+=1
            checkAgain=False
        if pipy<tipy:
            checkAgain=True
    # Display
    cv2.putText(img,f'{upCount}',(10,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)