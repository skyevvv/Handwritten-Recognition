import numpy as np
import queue
from tqdm import tqdm
import cv2
import os
from tqdm import tqdm
import pickle

def getListFiles(path):
    ret = []
    for root, dirs, files in os.walk(path):  
        for filespath in files:
            ret.append(os.path.join(root,filespath)) 
    return ret

def get_images_labels():
    operators = ['plus', 'sub', 'mul', 'div', '(', ')']
    images = None
    labels = None
    pickle_images = open('../data/images','wb')
    pickle_labels = open('../data/labels','wb')

    for i, op in enumerate(operators):
        image_file_list = getListFiles('./cfs/' + op + '/')
        print('Loading the ' + op + ' operator...')
        for filename in tqdm(image_file_list):
            image = cv2.imread(filename, 2)
            if image.shape != (28, 28):
                image = cv2.resize(image, (28, 28))
            image = np.resize(image, (1, 28 * 28))
            image = (255 - image) / 255
            label = np.zeros((1, 10 + len(operators)))
            label[0][10 + i] = 1
            if images is None:
                images = image
                labels = label
            else:
                images = np.r_[images, image]
                labels = np.r_[labels, label]
    pickle.dump(images, pickle_images)
    pickle.dump(labels, pickle_labels)
    pickle_images.close()
    pickle_labels.close()

get_images_labels()

