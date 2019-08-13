"""
    Read and get file information
"""
import cv2
import matplotlib.pyplot as plt

import numpy as np


def read_img():
    """
        Reads image file and change color format
    """
    img = cv2.imread('media/learn-colors.jpg')
    # print(img.shape)
    # cv2.imshow('ImageWindow', img)
    # cv2.waitKey()

    # covert to rgb
    b, g, r = cv2.split(img)
    rgb_img = cv2.merge([r, g, b])

    # show both images in matplotlib
    plt.subplot(121)
    plt.imshow(img)
    plt.subplot(122)
    plt.imshow(rgb_img)
    plt.show()

    # show both images in cv2
    bgr_rgb_img = np.concatenate([img, rgb_img], axis=1)
    cv2.imshow('bgr and rgb', bgr_rgb_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    read_img()
