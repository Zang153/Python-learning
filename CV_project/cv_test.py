import cv2
import numpy as np

# Open the camera (use 0 for the built-in camera, 1 for an external camera, etc)
cap = cv2.VideoCapture(0)

# # Create a black image
# image = np.zeros((512,512,3), np.uint8)

# # Show the image in a window
# cv2.imshow('Window', image)

# # Wait for a key press and handle GUI events
# cv2.waitKey(1000)

# # Destroy the window
# cv2.destroyAllWindows()


while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # If the frame was successfully read
    if ret:
        # Display the frame in a window
        cv2.imshow('Camera', frame)

        # If the 'q' key is pressed, break the loop
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    else:
        break

# Release the camera
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
