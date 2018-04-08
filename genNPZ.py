from PIL import Image
import numpy as np
from cv2 import *
import os

rootpath='.\\samples\\'
classes=('bus','dinasour','elephant','flower','horse')
width = 64
height = 64

def pre(img):
    return img

def resize_img(img):
    return resize(img,(width,height))

def trans2gray(img):
    return cvtColor(img,COLOR_BGR2GRAY)

def trans2array(img):
    return np.array(img)

def data_processing(img):
    img=pre(img)
    img=resize_img(img)
    img=trans2gray(img)
    return img

def img3ch_array(img):
    img=pre(img)
    img=resize_img(img)
    tmp=trans2array(img)
    ans =  np.array(np.zeros(3*width*height))
    ans.shape=1,3,width,height
    for i in range(width):
        for j in range(height):
            for k in range(3):
                ans[0][k][j][i]=tmp[i][j][k]
    return ans

def gen_data(root=rootpath+classes[0]+'\\',len=1,start=0):
    
    for i in range(len):
        path = root + str(i+start)+'.JPEG'
        print(path)
        img=imread(path)
        if i == 0:
            ans = trans2array(data_processing(img))
            ans.shape=1,width,height
        else:
            next_array = trans2array(data_processing(img))
            next_array.shape=1,width,height
            ans=np.concatenate((ans,next_array),axis=0)
        #ans.shape=len,width,height
        #print (ans)
    return ans

def gen_3chdata(root=rootpath+classes[0]+'\\',len=1,start=0):
    for i in range(len):
        path = root + str(i+start)+'.JPEG'
        print(path)
        img=imread(path)
        if i == 0:
            ans = img3ch_array(img)
        else:
            next_array = img3ch_array(img)
            ans=np.concatenate((ans,next_array),axis=0)
        #ans.shape=len,width,height
        #print (ans)
    return ans



def gen_output(num,l):
        ans = []
        for i in range(l):
                ans.append(num)
        return ans

def gen_dataset(n_train=100,n_test=10,n_class=len(classes)):
        y_test=[]
        y_train=[]
        for i in range(n_class):
                p = rootpath + classes[i] + '\\'
                if i==0:
                        x_test=gen_data(p,n_test,n_train)
                        x_train=gen_data(p,n_train)
                else:
                        x_test=np.concatenate((x_test,gen_data(p,n_test,n_train)))
                        x_train=np.concatenate((x_train,gen_data(p,n_train)))
 
                y_test.append(gen_output(i,n_test))
                y_train.append(gen_output(i,n_train))
                
                
        y_test=np.array(y_test,dtype=np.uint8)
        y_test.shape=n_test*n_class
        y_train=np.array(y_train,dtype=np.uint8)
        y_train.shape=n_train*n_class

        np.savez("data.npz",x_test=x_test,x_train=x_train,y_test=y_test,y_train=y_train)
        return None
    
def gen_3chdataset(n_train=100,n_test=10,n_class=len(classes)):
        y_test=[]
        y_train=[]
        for i in range(n_class):
                p = rootpath + classes[i] + '\\'
                if i==0:
                        x_test=gen_3chdata(p,n_test,n_train)
                        x_train=gen_3chdata(p,n_train)
                else:
                        x_test=np.concatenate((x_test,gen_3chdata(p,n_test,n_train)))
                        x_train=np.concatenate((x_train,gen_3chdata(p,n_train)))
 
                y_test.append(gen_output(i,n_test))
                y_train.append(gen_output(i,n_train))
                
                
        y_test=np.array(y_test,dtype=np.uint8)
        y_test.shape=n_test*n_class
        y_train=np.array(y_train,dtype=np.uint8)
        y_train.shape=n_train*n_class

        np.savez("data.npz",x_test=x_test,x_train=x_train,y_test=y_test,y_train=y_train)
        return None

def save_image():
        for i in range(len(classes)):
                path = rootpath + classes[i] + '\\'
                for j in range(100):
                        img=imread(path+str(j)+'.JPEG')
                        img=data_processing(img)
                        p='.\\saved_img\\'+classes[i]+'\\'+str(j)+'.jpg'
                        imwrite(p,img)
        return


gen_3chdataset(80,20)
#gen_dataset(80,20,5)
#save_image()
