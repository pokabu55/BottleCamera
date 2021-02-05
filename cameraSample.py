# config:utf-8
import cv2
import os
from bottle import route, run, static_file, abort

@route("/camera")
def camera():
	cap = cv2.VideoCapture(1)

	cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

	if cap.isOpened() is False:
		abort(500, 'Camera cannot enabled.')
		return

	ret, frame = cap.read()

	if ret == False:
		abort(500, 'Camera could not capture an image.')
		return

	cv2.imwrite(os.path.join(os.getcwd(), '.captured.jpg'), frame)
	cap.release()

	return static_file('.captured.jpg', root=os.getcwd())

if __name__ == "__main__":
	run(host="localhost", port=8080, debug=True)