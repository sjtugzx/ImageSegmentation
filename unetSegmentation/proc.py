import cv2
import os

def resize_keep_aspectratio(image_src, dst_size):
    src_h, src_w = image_src.shape[:2]
    print(src_h, src_w)
    dst_h, dst_w = dst_size

    # 判断应该按哪个边做等比缩放
    h = dst_w * (float(src_h) / src_w)  # 按照ｗ做等比缩放
    w = dst_h * (float(src_w) / src_h)  # 按照h做等比缩放

    h = int(h)
    w = int(w)

    if h <= dst_h:
        image_dst = cv2.resize(image_src, (dst_w, int(h)))
    else:
        image_dst = cv2.resize(image_src, (int(w), dst_h))

    h_, w_ = image_dst.shape[:2]
    print(h_, w_)

    top = int((dst_h - h_) / 2);
    down = int((dst_h - h_ + 1) / 2);
    left = int((dst_w - w_) / 2);
    right = int((dst_w - w_ + 1) / 2);

    value = [0, 0, 0]
    borderType = cv2.BORDER_CONSTANT
    print(top, down, left, right)
    image_dst = cv2.copyMakeBorder(image_dst, top, down, left, right, borderType, None, value)

    return image_dst


if __name__ == "__main__":
    # path='data/train/label/c1.png'
    # img = cv2.imread(path)
    # dst_size = (512, 512)
    # image = resize_keep_aspectratio(img, dst_size)
    # print(image.shape)
    # cv2.imwrite('data/train/labelR/c1.png', image)
    path1='data/test/'
    files1 = os.listdir(path1)
    # path2='data/train/label/'
    # files2 = os.listdir(path2)
    dst_size = (512, 512)
    for f1 in files1:
        newp=path1+f1
        img = cv2.imread(newp)
        image = resize_keep_aspectratio(img, dst_size)
        cv2.imwrite('data/testR/'+f1, image)

    # for f2 in files2:
    #     newl=path2+f2
    #     print(newl)
    #     img = cv2.imread(newl)
    #     image = resize_keep_aspectratio(img, dst_size)
    #     cv2.imwrite('data/train/labelR/'+f2, image)

