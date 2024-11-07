import cv2
import face_recognition

def capture_face():
    """
    Captures a face using the camera and returns the frame and the location of the face detected.
    """
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('Capture Face', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            face_locations = face_recognition.face_locations(frame)
            if face_locations:
                cap.release()
                cv2.destroyAllWindows()
                return frame, face_locations[0]  # Return the first face detected for simplicity
            print("No face detected. Try again.")
    cap.release()
    cv2.destroyAllWindows()
    return None, None

if __name__ == "__main__":
    frame, location = capture_face()
    if frame is not None:
        print("Face captured.")
    else:
        print("No face captured.")
