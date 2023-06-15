import time
import vgamepad
from initializer import cameraSettings as cam, controllerInput as ctr, videoSettings as vid

def run():
    amountFrames = vid.videoLength * vid.framesPerSecond
    gamepad = vgamepad.VX360Gamepad()

    for frame in range(amountFrames):
        moveCameraOneFrame(gamepad)
        if cam.refocusEnabled:
            focusCamera(gamepad)

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

    time.sleep(0.1) #not very pretty

    gamepad.release_button(button=vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X)
    gamepad.update()

run()