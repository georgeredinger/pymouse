#http://pythonhosted.org/evdev/
from evdev import InputDevice
from select import select
dev = InputDevice('/dev/input/event9') 
while True:
  r,w,x = select([dev], [], [])
  for event in dev.read():
    if event.code == 1: #y movement
      print(event.code,event.value)

