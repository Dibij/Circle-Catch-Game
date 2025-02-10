import cv2 as cv
import numpy as np
import random
import time
import os
import re

cap = cv.VideoCapture(0)
haar_cascade = cv.CascadeClassifier('hand.xml')
''' You want to save a video of you gameplay?
    Uncomment this part of the code and 
'''
# save_dir = r"Hand-Catch-Game\data\videos"
# os.makedirs(save_dir, exist_ok=False)

# # Find the highest existing video number
# existing_videos = [f for f in os.listdir(save_dir) if re.match(r"video(\d+)\.avi", f)]
# video_count = max([int(re.search(r"video(\d+)\.avi", v).group(1)) for v in existing_videos], default=-1) + 1

# video_writer = None
# recording = False
# paused = False
# frame_width, frame_height = 640, 480
# fps = 60


circle_center = (random.randint(50, 550), random.randint(50, 400))
circle_radius = 25

game_duration = 60
score = 0
start_time = time.time()

# Get frame size
ret, frame = cap.read()
frame_height, frame_width = frame.shape[:2]

def log_final_score(score):
    with open("Hand-Catch-Game\data\scores.txt", "a") as file:
        file.write(f"Final Score: {score}\n")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv.flip(frame, 1)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    hand_rects = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)
    
    # Draw the circle
    cv.circle(frame, circle_center, circle_radius, (255, 0, 0), -1)

    for (x, y, w, h) in hand_rects:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Check if the hand is over the circle
        if (x < circle_center[0] < x + w) and (y < circle_center[1] < y + h):
            score += 1
            circle_center = (random.randint(50, 550), random.randint(50, 400))
    # Display Timer
    elapsed_time = int(time.time() - start_time)
    remaining_time = max(0, game_duration - elapsed_time)
    cv.putText(frame, f"Time: {remaining_time}s", (frame_width - 200, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv.putText(frame, f"Score: {score}", (50, frame_height - 20), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    
    cv.imshow("Frame", frame)

    if remaining_time <= 0:
        print(f"Game Over! Final Score: {score}")
        break
    key = cv.waitKey(1) & 0xFF
    '''
        This Part 
    '''
    # if key == ord('q'):
    #     break
    
    # if key == ord('v'):  # Toggle video recording
    #     if not recording:
    #         video_path = os.path.join(save_dir, f"video{video_count}.avi")
    #         video_writer = cv.VideoWriter(video_path, cv.VideoWriter_fourcc(*'XVID'), fps, (frame_width, frame_height))
    #         recording = True
    #         paused = False
    #         print(f"Recording started: {video_path}")
    #         video_count += 1
    #     else:
    #         video_writer.release()
    #         recording = False
    #         print("Recording stopped")

    # elif key == ord('p') and recording:  # Pause/unpause recording
    #     paused = not paused
    #     print("Recording paused" if paused else "Recording resumed")

    # if recording and not paused and video_writer is not None:
    #     video_writer.write(frame)


# Log final score
log_final_score(score)
cap.release()
cv.destroyAllWindows()
