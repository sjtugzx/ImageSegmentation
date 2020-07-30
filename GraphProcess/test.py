import cv2 as cv
import numpy as np

# canny边缘检测
def canny_demo(image):
    t = 100
    canny_output = cv.Canny(image, t, t * 2)
    cv.imshow("canny_output", canny_output)
    # cv.imwrite("test/canny_output.png", canny_output)
    return canny_output

# 读取图像
src = cv.imread("Images/kmeans2.jpg")
print(src.shape)
rows=src.shape[0]
columns=src.shape[1]
reshape=src[2:rows,2:columns]


cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", reshape)

# 调用
binary = canny_demo(reshape)
k = np.ones((5, 5), dtype=np.uint8)
binary = cv.morphologyEx(binary, cv.MORPH_DILATE, k)

# 轮廓发现
contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for c in range(len(contours)):
    rect = cv.minAreaRect(contours[c])
    cx, cy = rect[0]
    box = cv.boxPoints(rect)
    box = np.int0(box)
    cv.drawContours(src,[box],0,(0,255,0),2)
    cv.circle(src, (np.int32(cx), np.int32(cy)), 2, (255, 0, 0), 2, 8, 0)
    cv.drawContours(src, contours, c, (0, 0, 255), 2, 8)

# 图像显示
cv.imshow("contours_analysis", src)
cv.imwrite("test/ko2.png", src)
cv.waitKey(0)
cv.destroyAllWindows()
