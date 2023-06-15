import json

f = open('input/input.json')
input = json.load(f)

coolDownDuration = input['cameraSettings']['coolDownDuration']
movementLength = input['cameraSettings']['movementLength']
refocusEnabled = input['cameraSettings']['refocusEnabled']

f.close()