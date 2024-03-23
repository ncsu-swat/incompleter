#Source: https://stackoverflow.com/questions/68691767/mediapipe-pose-estimation-typeerror-type-list-doesnt-define-round-method
import cv2
import mediapipe as mp
import numpy as np
import time
import pyautogui
import mouse

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


# display screen resolution, get it from your OS settings
SCREEN_SIZEX = (1920)
SCREEN_SIZEY = (1080)
# define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# create the video write object
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZEX, SCREEN_SIZEY))

with mp_pose.Pose(min_detection_confidence=0.1, min_tracking_confidence=0.9) as pose:
    while True:
        # make a screenshot
        img = pyautogui.screenshot()
        # convert these pixels to a proper numpy array to work with OpenCV
        frame = np.array(img)
        # convert colors from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Make detection
        results = pose.process(image)

        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


        landmarks = results.pose_landmarks.landmark
        lndmark = landmarks[mp_pose.PoseLandmark.NOSE.value]
        x = [landmarks[mp_pose.PoseLandmark.NOSE.value].x]
        y = [landmarks[mp_pose.PoseLandmark.NOSE.value].y]

        #xx = ''.join(str(e) for e in x)
        #yy = ''.join(str(e) for e in y)

        #xx = [int(i) for i in xx]
        #yy = [int(i) for i in yy]

        test_coord = (x, y)

        SCREEN_DIMENSIONS = (1920, 1080)


        def to_pixel_coords(relative_coords):
            return tuple(round(coord * dimension) for coord, dimension in zip(relative_coords, SCREEN_DIMENSIONS))


        print(to_pixel_coords(test_coord))




        #print(xxx)
        #print(yyy)

        #mouse.move(xxx, yyy)


        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                 )

        # write the frame
        out.write(frame)

        pTime = 0

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(image, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
        (255, 0, 0), 3)



        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    out.release()
    cv2.destroyAllWindows()


    #for lndmark in mp_pose.PoseLandmark:
        #print(lndmark)