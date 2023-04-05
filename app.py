import cv2 as cv

vid = cv.VideoCapture('./imran1.mp4') # just pass your video path here
vid.set(3, 640)
vid.set(4, 480)
cv.namedWindow('Video Edit', cv.WINDOW_NORMAL)
cv.resizeWindow('Video Edit', 800, 600)


def handler(a):
    pass


cv.namedWindow('canny')
cv.resizeWindow('canny', 640, 480)
cv.createTrackbar('canny 1', 'canny', 0, 1000, handler)
cv.createTrackbar('canny 2', 'canny', 0, 1000, handler)
cv.createTrackbar('blur', 'canny', 0, 100, handler)
cv.createTrackbar('brightness', 'canny', 0, 100, handler)
cv.createTrackbar('contrast', 'canny', 1, 127, handler)
cv.createTrackbar('saturation', 'canny', 0, 10, handler)
while True:
    success, image = vid.read()
    thrs1 = cv.getTrackbarPos('canny 1', 'canny')
    thrs2 = cv.getTrackbarPos('canny 2', 'canny')
    blur = cv.getTrackbarPos('blur', 'canny')
    brightness = cv.getTrackbarPos('brightness', 'canny')
    contrast = cv.getTrackbarPos('contrast', 'canny')
    saturation = cv.getTrackbarPos('saturation', 'canny')
    if success:
        if thrs1:
            image = cv.Canny(image, thrs1, thrs2)
        if (blur % 2) != 1:
            blur += 1
        image = cv.blur(image, (blur, blur), 0)
        image = out = cv.addWeighted(image, contrast, image, 0, brightness)
        if saturation:
            hsv_img = cv.cvtColor(image, cv.COLOR_BGR2HSV)
            hsv_img[:, :, 1] = hsv_img[:, :, 1] * 1.2
            image = cv.cvtColor(hsv_img, cv.COLOR_HSV2BGR)
        cv.imshow('Video Edit', image)
    else:
        vid.set(cv.CAP_PROP_POS_FRAMES, 0)
        continue

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
