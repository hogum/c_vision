import numpy as np
import cv2
import matplotlib.pyplot as plt


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


def output_plot(img, pos, title='image'):
    """
        Plots image
    """
    rgb_img = img[:, :, :: -1]
    plt.subplot(1, 3, pos)
    plt.imshow(rgb_img)
    plt.title(title)
    plt.axis('off')


def create_figure():
    """
        Specifies the figure dimensions and creates its canvas
    """
    fig = plt.figure(figsize=(12, 5))
    plt.suptitle('contours', fontsize=12)
    fig.patch.set_facecolor('silver')

    canvas = np.zeros([640, 640, 3], dtype=np.uint8)

    return fig, canvas


def draw_cont_outline(image, contours, colour, thickness=1):
    """
        Draws outlines of each contour
    """
    for ct in contours:
        cv2.drawContours(image, [ct], 0, colour, thickness)


def draw_outlines():
    """
        Draws contour outlines on images
    """
    fig, canvas = create_figure()
    contours = get_contour()[0]

    img_points = canvas.copy()
    img_outline = canvas.copy()
    img_points_outline = canvas.copy()

    # Points
    draw_contours(img_points, contours(255, 0, 255))

    # Outline
    draw_cont_outline(img_outline, contours, (0, 255, 255), 3)

    # Points + Outline
    draw_cont_outline(img_points_outline, contours, (255, 0, 0), 3)
    draw_contours(img_points_outline, contours, (0, 0, 255))

    for i, img in enumerate([img_points, img_outline, img_points_outline]):
        output_plot(img, i)
    plt.show()
