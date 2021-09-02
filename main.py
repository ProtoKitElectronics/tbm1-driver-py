from lib.driver import Motors, IRSensorArray, Buzzer, Button
from time import sleep

motors = Motors()
sensor_array = IRSensorArray()
bzz = Buzzer()
btn = Button()

def main():
  bzz.on()
  sleep(0.3)
  bzz.off()
  
  motors.forward()

  while sensor_array.read("front") > 3000:
    sleep(0.1)
  
  motors.stop_break()
  sleep(1)
  motors.stop_release()

btn.setOnPress(main)