import numpy as np
import cv2


def get_contour():
    """
       Gives a fixed contour
    """
    contours = np.array([[[600, 320]], [[563, 460]],
                         [[460, 562]], [[320, 600]],
                         [[180, 563]], [[78, 460]],
                         [[40, 320]], [[77, 180]],
                         [[179, 78]],
                         [[319, 40]], [[459, 77]], [[562, 179]]]
                        )

    return contours


def draw_contours(img, contours, colour):
    """
        Draws the contour points
    """
    for contour in contours:
        sqz = np.squeeze(contour)

        for pixel in sqz:
            pixel = tuple(pixel.reshape(1, -1)[0])
            cv2.circle(img, pixel, 10, colour, -1)
