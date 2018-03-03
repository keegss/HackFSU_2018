import cv2
import random
import os
import numpy as np

def createSet(imgFile, setSize):
    degreeOffset = 10
    translationOffset = 5;
    totalImgs = []
    quarterNote = cv2.imread(imgFile, 0)
    quarterNote = cv2.bitwise_not(quarterNote)
    rows,cols = quarterNote.shape
    for i in range(setSize-2):
        M = cv2.getRotationMatrix2D((cols/2,rows/2),random.randint(-degreeOffset,degreeOffset),1)
        curImage = cv2.warpAffine(quarterNote,M,(cols,rows))
        M = np.float32([[1,0,random.randint(-translationOffset,translationOffset)],[0,1,random.randint(-translationOffset,translationOffset)]])
        curImage = cv2.warpAffine(curImage,M,(cols,rows))
        curImage = cv2.bitwise_not(curImage)
        totalImgs.append(curImage)
    M = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
    curImage = cv2.warpAffine(quarterNote,M,(cols,rows))
    M = np.float32([[1,0,random.randint(-translationOffset,translationOffset)],[0,1,random.randint(-translationOffset,translationOffset)]])
    curImage = cv2.warpAffine(curImage,M,(cols,rows))
    curImage = cv2.bitwise_not(curImage)
    totalImgs.append(curImage)
    quarterNote = cv2.bitwise_not(quarterNote)
    totalImgs.append(quarterNote)
    saveImgs(totalImgs)

def drawImgs(imgList, setSize):
    for i in range(setSize):
        cv2.imshow('rotation' + str(i), imgList[i])

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def saveImgs(dataSet):
    folderName = 'DataSet'
    path = os.path.join(os.getcwd(), folderName)
    if not os.path.exists(path):
        os.makedirs(path)    
    for i, frame in enumerate(dataSet):
        fileName = ("image%s" % i)
        filePath = os.path.join(path, fileName)
       	np.save(filePath, frame, allow_pickle=True, fix_imports=True)    
        
def main():
	# filename = input('Enter file for base image: ')
	# size = input('Enter size of data set to generate ')
	createSet('quarterNoLine.png',100)

if __name__ == '__main__':
	main()