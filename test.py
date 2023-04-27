from cv2 import *
def take_photo(name_of_the_photo):
	cam_port = 0
	cam = VideoCapture(cam_port)
	result, image = cam.read()
	if result:
		imshow(name_of_the_photo, image)
		imwrite(name_of_the_photo, image)
		waitKey(0)
		destroyWindow(name_of_the_photo)
	else:
		print("No image detected. Please! try again")
