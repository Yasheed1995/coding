#!/usr/bin/env python
""" crack.py: breaks captcha."""

__author__ = "Yasheed"

import numpy as np
import cv2
from scipy.stats import mode


def read_img(path):
    img = np.array(cv2.imread(path, 0))
    rowNum, colNum = img.shape
    BACKGROUND = mode(img.ravel())[0][0]

    # find upper and lower boundary
    upperBound, lowerBound = 0, 0
    for i in range(rowNum):
        if np.average(img[i, :]) == BACKGROUND:
            upperBound = i
        else:
            break
    for i in range(rowNum - 1, 0, -1):
        if np.average(img[i, :]) == BACKGROUND:
            lowerBound = i
        else:
            break
    return img[upperBound:lowerBound, :], BACKGROUND


def find_seg(img, path):
    ret, thresh = cv2.threshold(img, BACKGROUND, 255, 0)
    cv2.imwrite("binary.png", thresh)
    im2, contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )
    contours_size = list()
    for contour in contours:
        contours_size.append(contour.shape[0])
    four_countours = np.array(contours_size).argsort()[-4:][::-1]
    for i in range(len(contours)):
        if i not in four_countours:
            continue
        l = np.min(contours[i], 0)[0][0]
        r = np.max(contours[i], 0)[0][0]
        cv2.imwrite('{0}_test_char_{1}.png'.format(path, i), img[:, l:r])

if __name__ == '__main__':
    while 1:
        path = raw_input("input a number, type exit to quit.\n")
        if path == 'exit':
            break
        img, BACKGROUND = read_img(path + ".png")
        find_seg(img, path)
