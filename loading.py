import cv2
image = cv2.imread("cv.png")

if image is not None:
    cv2.imshow("Image showing", image) #opens the image window
    cv2.waitKey(0) #waits for a key press
    cv2.destroyAllWindows() #close the window
else:
    print("Error: Could not read the image.")