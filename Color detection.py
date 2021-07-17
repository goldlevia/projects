import cv2
import numpy as np


cap = cv2.VideoCapture(0)

width_frame = 640
height_frame = 480
brightness = 140

cap.set(3, width_frame)
cap.set(4, height_frame)
cap.set(10, brightness)


defined_colors = [[5, 107, 0, 19, 255, 255],
                  [133, 56, 0, 159, 156, 255],
                  [57, 76, 0, 100, 255, 255]]


my_color_values = [[51, 153, 255], # blue RGB
                   [255, 0, 255], # pink RGB
                   [0, 255, 0]] # green RGB


def find_color(find_color_def_img, my_colors):
    img_hsv = cv2.cvtColor(find_color_def_img, cv2.COLOR_BGR2HSV)
    count = 0
    for color in my_colors:
        lower_value = np.array(color[0:3])
        upper_value = np.array(color[3:6])
        mask = cv2.inRange(img_hsv, lower_value, upper_value)
        x, y = get_contours(mask)
        cv2.circle(img_result, (x, y), 10, my_color_values[count], cv2.FILLED)
        count += 1


def get_contours(contours_img):
    contours, hierarchy = cv2.findContours(contours_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(img_result, cnt, -1, (255, 0, 0), 3)
            per = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*per, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y


while True:
    success, img = cap.read()
    img_result = img.copy()
    find_color(img, defined_colors)
    cv2.imshow("Result", img_result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
