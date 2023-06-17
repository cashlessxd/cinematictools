import os
import shutil
import time
import vgamepad
from initializer import cameraSettings as cam, controllerInput as ctr, videoSettings as vid
from mss import mss

import moviepy.video.io.ImageSequenceClip

def run():
    amountFrames = vid.videoLength * vid.framesPerSecond
    gamepad = vgamepad.VX360Gamepad()

    clipPath = os.environ['USERPROFILE'] + '/Documents/Cinematictools/clips'

    os.makedirs('frames')

    if not os.path.exists(clipPath):
        os.makedirs(clipPath)

    with mss() as sct:
        for frame in range(amountFrames):
            moveCameraOneFrame(gamepad)
            if cam.refocusEnabled:
                focusCamera(gamepad)
            createFrame(sct, frame)
            print ('Frame Created: ' + str(frame + 1) + ' of ' + str(amountFrames))
    createVideo(amountFrames, clipPath)

    shutil.rmtree('frames')

def moveCameraOneFrame(gamepad):
    gamepad.left_joystick_float(x_value_float=ctr.leftStickX, y_value_float=ctr.leftStickY)
    gamepad.right_joystick_float(x_value_float=ctr.rightStickX, y_value_float=ctr.rightStickY)
    gamepad.update()

    time.sleep(cam.movementLength)

    gamepad.left_joystick_float(x_value_float=0, y_value_float=0)
    gamepad.right_joystick_float(x_value_float=0, y_value_float=0)
    gamepad.update()

    time.sleep(cam.coolDownDuration)

def focusCamera(gamepad):
    gamepad.press_button(button=vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X)
    gamepad.update()

    time.sleep(0.01) #TODO: make this bit prettier

    gamepad.release_button(button=vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X)
    gamepad.update()

def createFrame(sct, frame):
    sct.shot(output='frames/frame' + str(frame) + '.png')

def createVideo(amountFrames, clipPath):
    frames = []
    clipNumber = 1

    for file in os.listdir(clipPath):
        clipNumber += 1

    for frameNumber in range(amountFrames):
        frames.append('frames/frame' + str(frameNumber) + '.png')

    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(frames, fps=vid.framesPerSecond)
    clip.write_videofile(clipPath + '/clip' + str(clipNumber) + '.mp4', bitrate='1000000k')

run()