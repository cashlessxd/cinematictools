import json

f = open('input/input.json')
input = json.load(f)

framesPerSecond = input['videoSettings']['framesPerSecond']
videoLength = input['videoSettings']['videoLength']

f.close()