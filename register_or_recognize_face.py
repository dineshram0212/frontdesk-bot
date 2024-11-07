import cv2
import face_recognition
import numpy as np
import os
from capture_face import capture_face

# Assume face_data is stored and loaded from a file or a database for persistence
face_data = {}  # Format: {face_id: {"encoding": face_encoding, "coord": coord}}

def register_or_recognize_face():
    """
    Captures a face and either registers it or recognizes it, then performs an action based on the recognition.
    """
    frame, face_location = capture_face()
    if frame is not None and face_location is not None:
        face_encodings = face_recognition.face_encodings(frame, [face_location])
        matches = face_recognition.compare_faces([data["encoding"] for data in face_data.values()], face_encodings[0])
        if True in matches:
            first_match_index = matches.index(True)
            face_id = list(face_data.keys())[first_match_index]
            print(f"Recognized face ID: {face_id}")
            # Perform an action, for example, moving an object associated with the recognized face
            # arm_ctrl(face_data[face_id]["coord"])
        else:
            # Register new face
            face_id = f"person_{len(face_data) + 1}"
            face_data[face_id] = {
                "encoding": face_encodings[0],
                "coord": (0, 0)  # Example coordinates, should be set based on the specific task
            }
            print(f"Registered new face with ID: {face_id}")
            # You might want to save the new face_data structure to a file or database here

if __name__ == "__main__":
    register_or_recognize_face()
