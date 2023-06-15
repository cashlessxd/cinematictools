import json

f = open('input/input.json')
input = json.load(f)

leftStickX = input['controllerInput']['leftStickX']
leftStickY = input['controllerInput']['leftStickY']
rightStickX = input['controllerInput']['rightStickX']
rightStickY = input['controllerInput']['rightStickY']

f.close()