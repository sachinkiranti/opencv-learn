# Computer Vision and OpenCV

OpenCV is an image processing library created by intel and later supported by Willow Garage and now maintained by Itseez.

Works in C, C++ and python.

Opensource and free.

# Image vs Matrix

Digital images are typically stored in a matrix.

PPI : Pixel per inch (Display resolution )

Two Types of images computer see :

- Gray scale images
- Colored images (RGB)

# Numpy

- Numpy is a highly optimized library for numerical operations.
- Array structure is important because digital images are 2D arrays of P-I-X-E-L-S
- All the OpenCV array structures are converted to and from Numpy arrays.
- You can use more convenient indexing system rather than using for loops.

When we install OpenCV, Numpy will be automatically installed.

## Checking openCV version
```
import cv2

print(cv2.__version__)
```