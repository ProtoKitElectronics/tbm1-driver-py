from machine import Pin, PWM

class Buzzer:
  """
  A class representing the buzzer

  The buzzer is controller by one pin using PWM (pulse width modulation).
  """

  def __init__(self, pin):
    self.pwm = PWM(Pin(pin, Pin.OUT))
  
  def play(self, duty):
    """
    Plays the buzzer at a specified PWM duty cycle (0 - 65535)
    """
    self.pwm.duty_u16(duty)