import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

# Create a video capture object
cap = cv2.VideoCapture(0)

# Loop through frames
while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Find QR codes in the frame
    decodedObjects = pyzbar.decode(frame)

    # Loop through the decoded objects
    for obj in decodedObjects:
        # Print the data contained in the QR code
        print("Data:", obj.data.decode())

        # Draw a rectangle around the QR code
        points = obj.polygon
        if len(points) > 4:
            hull = cv2.convexHull(
                np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points
        n = len(hull)
        for j in range(n):
            cv2.line(frame, hull[j], hull[(j+1) % n], (0, 255, 0), 3)

    # Show the frame
    cv2.imshow("QR Scanner", frame)
    # Wait for the user to press 'q' or 'esc' to quit
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
