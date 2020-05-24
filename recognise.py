# USAGE
# With default parameters
#     python3 03_recognise.py
# OR specifying the encodings, screen resolution
#     python3 03_recognise.py -e encodings.pickle -r 240

## Acknowledgement
## This code is adapted from:
## https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/

# import the necessary packages
from imutils.video import VideoStream
import face_recognition
import argparse
import imutils
import pickle
import time
import cv2
import socket_utils
import socket, json, sqlite3, sys
from datetime import datetime

HOST = "220.244.177.218"         # The server's hostname or IP address.
PORT = 63000               # The port used by the server.
ADDRESS = (HOST, PORT)
carid = 16

def main():
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-e", "--encodings", default="encodings.pickle",
    help="path to serialized db of facial encodings")
    ap.add_argument("-r", "--resolution", type=int, default=240,
        help="Resolution of the video feed")
    ap.add_argument("-d", "--detection-method", type=str, default="hog",
        help="face detection model to use: either `hog` or `cnn`")
    args = vars(ap.parse_args())

    # load the known faces and embeddings
    print("[INFO] loading encodings...")
    data = pickle.loads(open(args["encodings"], "rb").read())

    # initialize the video stream and then allow the camera sensor to warm up
    print("[INFO] starting video stream...")
    vs = VideoStream(src = 0).start()
    time.sleep(2.0)

    # loop over frames from the video file stream
    if True:
        # grab the frame from the threaded video stream
        #frame = vs.read()
        frame = cv2.imread('dataset//search.jpg')

        # convert the input frame from BGR to RGB then resize it to have
        # a width of 750px (to speedup processing)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb = imutils.resize(frame, width = args["resolution"])

        # detect the (x, y)-coordinates of the bounding boxes
        # corresponding to each face in the input frame, then compute
        # the facial embeddings for each face
        boxes = face_recognition.face_locations(rgb, model = args["detection_method"])
        encodings = face_recognition.face_encodings(rgb, boxes)
        names = []

        # loop over the facial embeddings
        for encoding in encodings:
            # attempt to match each face in the input image to our known
            # encodings
            matches = face_recognition.compare_faces(data["encodings"], encoding)
            name = "Unknown"

            # check to see if we have found a match
            if True in matches:
                # find the indexes of all matched faces then initialize a
                # dictionary to count the total number of times each face
                # was matched
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}

                # loop over the matched indexes and maintain a count for
                # each recognized face face
                for i in matchedIdxs:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0) + 1

                # determine the recognized face with the largest number
                # of votes (note: in the event of an unlikely tie Python
                # will select first entry in the dictionary)
                name = max(counts, key = counts.get)

            # update the list of names
            names.append(name)

    # loop over the recognized faces
        for name in names:
            # print to console, identified person
            print("Person found: {}".format(name))
            # Set a flag to sleep the cam for fixed time
            time.sleep(3.0)
            user = { "username": name, "password": "none", "carid": carid, "finish": 0, "date": str(datetime.now())}
            login(user)

            vs.stop()

def login(user):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Connecting to {}...".format(ADDRESS))
        s.connect(ADDRESS)
        print("Connected.")

        print("Logging in as {}".format(user["username"]))

        print("Waiting for Master Pi...")
        while(True):
            print()
            choice = input("""
Please choose to either:
 1: Unlock Car
 2: Return Car

 Please enter your choice: """)
            if choice == "1":  
                user["finish"] = 0
                break             
            elif choice == "2":
                
                user["finish"] = 1
                break
                
            else:
                print("\n You must only select either 1 or 2")
                print(" Please try again\n")
                print()

        socket_utils.sendJson(s, user)
        while(True):
            
            object = socket_utils.recvJson(s)
            if("authenticated" in object):
                print("Car Unlocked")
                print()
                break
                
            elif("returned" in object):
                print("Car Returned")
                print()
                break
            elif("nope" in object):
                print("Not Authorized")
                print()
                break
            elif("nobooking" in object):
                print("No Booking Found")
                print()
                break

# Execute program.
if __name__ == "__main__":
    main()
