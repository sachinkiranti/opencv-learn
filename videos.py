import cv2

cap = cv2.VideoCapture(0)  # 0 i.e default device(camera) as an argument


# Saving : arguments (Video name, fourcc codecs, Number of frame per second, size (as tuple))
# Getting the fourcc codecs
# fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Check if the device is open
print(cap.isOpened())

# Getting the frame properties in the video stream for now height and width
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# while loop for capturing the frame continuously
while cap.isOpened():
    ret, frame = cap.read()

    # ret will hold boolean value, True if frame is available else False
    if ret:
        # Save Frame
        out.write(frame)

        # Convert the image to gray style image else give frame as a second argument in imshow
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Video Frame', gray)
        # cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# release the capture frame
cap.release()
out.release()
cv2.destroyAllWindows()