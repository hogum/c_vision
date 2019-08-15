"""
    Capture video frames
"""

import cv2


def get_frame():
    """
        Reads frames from camera
    """
    capture = cv2.VideoCapture(0)  # Camera index

    while capture.isOpened():
        ret, frame = capture.read()

        if ret:
            cv2.imshow('Input frame', frame)
            gray_scaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('gray scaled', gray_scaled)
            save(frame, gray_scaled)
            if cv2.waitKey(20) & 0xff == ord('q'):
                break
        else:
            break

    capture.release()
    cv2.destroyAllWindows()


def save(frame, gray_frame):
    """
        Saves captued frames
    """
    idx = 0
    if cv2.waitKey(20) & 0xff == ord('s'):
        name = f'cature_{idx}.png'
        gray_frame_n = 'grayscale_capture_{idx}.png'
        cv2.imwrite(name, frame)
        cv2.imwrite(gray_frame_n, gray_frame)


if __name__ == '__main__':
    get_frame()
