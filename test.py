import cv2

camera = cv2.VideoCapture(0)


while True:
    # Grab the webcameras image.
    ret, image = camera.read()
    image = cv2.flip(image, 1)

    # print(image[20][50][0],int(num_to_range(image[20][50][0],0,255,255,0)))

    textCol = (0, 0, 0)
    label = 'Volume down'
    x1, y1 = 15, 50

    (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)

    # Prints the text.
    cv2.rectangle(image, (x1-5, y1 - 20), (x1 + w+5, y1), (255,255,255), -1)
    cv2.putText(image, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, textCol, 1)



    # cv2.rectangle(image, (x1, y1), (185, 30), (255, 255, 0), -1)
    # cv2.putText(image, "Volume down", (20, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, textCol)

    cv2.imshow('Webcam Image', image)

    keyboard_input = cv2.waitKey(1)
    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break

camera.release()
cv2.destroyAllWindows()
