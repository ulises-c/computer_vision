import cv2 as cv


def read_image():
    # Read image
    img = cv.imread("Photos/cat.jpg")
    cv.imshow("Cat", img)
    cv.waitKey(0)  # waits for '0' to be pressed


def read_video():
    # Read video
    video_path = "C:/Users/uchavarria/OneDrive - Laza/111824 Porcine Lab/Lab Videos/Passive Rider/Passive Rider_Nov18_09-22-14.mp4"
    capture = cv.VideoCapture(video_path)
    while True:
        isTrue, frame = capture.read()
        frame_resized = rescale_frame(frame)
        # cv.imshow("Video", frame)
        cv.imshow("Video Resized", frame_resized)

        if cv.waitKey(20) & 0xFF == ord("d"):  # if 'd' is pressed
            break
    capture.release()
    cv.destroyAllWindows()


def rescale_frame(frame, scale=0.5):
    # Works with images, videos, and live video feeds
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def change_resolution(width, height):
    # Only works with live video feeds
    capture.set(3, width)
    capture.set(4, height)


if __name__ == "__main__":
    read_video()
