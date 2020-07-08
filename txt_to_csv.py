
#### convert txt annotation file to csv ####
# Author: Galsaeedi1@gmail.com
# Date: 4/5/20

import os 
import cv2
import csv
import pandas as pd 

root = os.getcwd()
labelpath = 'OID/Label/'
imagepath= 'OID/'

labeldir=os.path.join(root,labelpath)
imgdir=os.path.join(root,imagepath)

annotationlist =[]
for filename in os.listdir(labeldir):
  if filename.endswith('txt'):
    filename_with_jpg=filename.split('.txt')[0]+'.jpg'
      
      
    if filename_with_jpg in os.listdir(imgdir):
      cvimage=cv2.imread(os.path.join(imgdir,filename_with_jpg))
      h,w,c=cvimage.shape 
               
    with open (os.path.join(labeldir,filename),'r') as txtfile:
      for line in txtfile:
        word= line.split(' ')
        if len(word)>5:
          annotationlist.append([filename_with_jpg,w,h,word[0]+' '+word[1],word[2],word[3],word[4],word[5]])
        else : 
          annotationlist.append([filename_with_jpg,w,h,word[0],word[1],word[2],word[3],word[4]])
          

df=pd.DataFrame(annotationlist,columns=['filename','width','height','class','xmin','ymin','xmax','ymax'])     
df.to_csv('humandataset.csv')


