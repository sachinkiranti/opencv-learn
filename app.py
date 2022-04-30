# import cv2.cv2 as cv2 // For loading cv2
import cv2

img = cv2.imread('lena.jpg', cv2.IMREAD_UNCHANGED)

print(img)

# Read the image
cv2.imshow('image', img)
# For 5 sec
# cv2.waitKey(5000)  # accepts milliseconds else 0 i.e. need to exit
k = cv2.waitKey(0)  # Won't exit itself

# if escape key press close and if s key pressed then copy the image
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    # Write the image
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()
