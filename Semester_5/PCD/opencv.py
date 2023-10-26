import cv2 as cv
import matplotlib.pyplot as mp
import numpy as np

img = cv.imread('img/MicrosoftTeams-image.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("src", gray)

mp.hist(gray.ravel(), 256, [0, 256]); mp.show()

ret, thresh1 = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
# cv.imshow("threshold img", thresh1)
mp.imshow(thresh1)

res = cv.equalizeHist(gray)
cv.imshow('Equalized Image', res)

mp.hist(res.ravel(), 256, [0, 256]); mp.show()

cv.waitKey(0)
cv.destroyAllWindows()

