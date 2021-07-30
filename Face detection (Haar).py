import cv2

# have downloaded file containing pre-trained date on face frontal from
# github https://github.com/opencv/opencv/tree/master/data/haarcascades
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# to capture video from webcam
web_cam = cv2.VideoCapture(0)

# iterate forever over frames
while True:
    # reading the current frame
    successful_face_read, frame = web_cam.read()

    # converting to grayscale
    gray_scaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detects faces by identifying coordinates from the
    # upper side of the face and says size if rectangle
    face_coordinates = trained_face_data.detectMultiScale(gray_scaled_img)

    # draws rectangle around faces by using detected point
    # by sizes are defined by last variable
    for x, y, width, height in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)

    # shows a window
    cv2.imshow('Face detection', frame)
    key = cv2.waitKey(1)

    # stop loop if "q" is pressed
    if key == 81 or key == 113:
        break

web_cam.release()
