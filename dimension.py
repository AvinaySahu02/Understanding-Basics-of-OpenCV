import cv2
image = cv2.imread("cv.png")

if image is not None:
    h, w, c = image.shape
    print(f"Image Loaded: \nHeight: {h}\nWidth: {w}\nChannels: {c}")
else:
    print("Error: Could not read the image.")