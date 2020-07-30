import numpy as np
import PIL.Image as image
from sklearn.cluster import KMeans


#Define loadData to solve my image

def loadData(filePath):
    f=open(filePath,'rb')
    data=[]
    img=image.open(f)
    m,n=img.size
    for i in range(m):
        for j in range(n):
            x,y,z=img.getpixel((i,j))
            data.append([x/256.0,y/256.0,z/256.0])

    f.close()
    return np.mat(data),m,n


def vertical(img):
    """传入二值化后的图片进行垂直投影"""
    pixdata = img.load()
    w,h = img.size
    ver_list = []
    # 开始投影
    for x in range(w):
        black = 0
        for y in range(h):
            if pixdata[x,y] == 0:
                black += 1
        ver_list.append(black)
    # 判断边界
    l,r = 0,0
    flag = False
    cuts = []
    for i,count in enumerate(ver_list):
        # 阈值这里为0
        if flag is False and count > 0:
            l = i
            flag = True
        if flag and count == 0:
            r = i-1
            flag = False
            cuts.append((l,r))
    return cuts

imgData, row, col=loadData("Images/2.png")
print(row,col,imgData)

label=KMeans(n_clusters=6).fit_predict(imgData)
label=label.reshape([row,col])
pic_new=image.new("L",(row,col))
for i in range(row):
    for j in range(col):
        print(256/label[i][j]+1)
        pic_new.putpixel((i,j),int(256/(label[i][j]+1)))
img1=np.array(pic_new)
print(img1)

pic_new.show()
pic_new.save("Images/kmeans2.jpg","JPEG")
