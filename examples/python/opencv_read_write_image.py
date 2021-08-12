import cv2 as cv
import sys
import io

if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} IN_FILENAME OUT_FILENAME")

in_filename = sys.argv[1]
out_filename = sys.argv[2]

img = cv.imread(in_filename)
print(type(img))  # numpy.array
print(img.shape)

# Draw a rectangle in the middle in some color:
y_top = img.shape[0] // 4
x_top = img.shape[1] // 4
y_bottom = img.shape[0] - y_top
x_bottom = img.shape[1] - x_top
blue = 80
green = 70
red = 90
cv.rectangle(img, (x_top, y_top), (x_bottom, y_bottom), color=(blue, green , red), thickness=2)

# save the image to a file on the disk
cv.imwrite(out_filename, img)


# Convert the numpy array to a binary object in memory
def numpy_to_binary(arr):
    is_success, buffer = cv.imencode(".jpg", arr)
    io_buf = io.BytesIO(buffer)
    print(type(io_buf))
    return io_buf.read()

binary_image = numpy_to_binary(img)

print(type(binary_image))  # bytes
