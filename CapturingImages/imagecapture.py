from djitellopy import tello
import cv2

me = tello.Tello()
me.connect()
print(me.get_battery())
""" streaming """

me.streamon()

while True:
    img = me.get_frame_read().frame

    img = cv2.resize(img, (360, 240))
    """ size of an image"""
    cv2.imshow("image", img)

    cv2.waitkey(1)
    """Delaying so that the frame can not shut down """

    # This script is used to connect to a Tello drone and start its video stream.
    # The script uses the djitellopy library to connect to the drone and the cv2 library to display the video stream.
    # The script first connects to the drone and prints the battery level.
    # Then it calls the stream() function to start the video stream.
