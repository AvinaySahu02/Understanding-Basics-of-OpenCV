import cv2
image = cv2.imread("cv.png")

if image is not None:
    success = cv2.imwrite("output_pythob.png", image)
    if success:
        print("Image saved successfully.")
    else:
        print("Failed to save an image")
else:
    print("Error: Could not read the image.")