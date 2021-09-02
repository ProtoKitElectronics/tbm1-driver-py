from machine import Pin, ADC

class Motors:
  """
  Communicates with the motor driver to opperate the motors
  """

  def __init__(self):
    self.pins = {
      "1,2EN": Pin(5, Pin.OUT),
      "1A": Pin(4, Pin.OUT),
      "2A": Pin(3, Pin.OUT),
      "3,4EN": Pin(6, Pin.OUT),
      "3A": Pin(7, Pin.OUT),
      "4A": Pin(8, Pin.OUT),
    }
    
  def enable(self):
    self.pins["1,2EN"].high()
    self.pins["3,4EN"].high()

  def disable(self):
    self.pins["1,2EN"].low()
    self.pins["3,4EN"].low()

  def forward(self):
    self.pins["1A"].high()
    self.pins["2A"].low()
    self.pins["3A"].high()
    self.pins["4A"].low()
  
  def backward(self):
    self.pins["1A"].low()
    self.pins["2A"].high()
    self.pins["3A"].low()
    self.pins["4A"].high()
  
  def stop_break(self):
    self.pins["1A"].high()
    self.pins["2A"].high()
    self.pins["3A"].high()
    self.pins["4A"].high()
  
  def stop_release(self):
    self.pins["1A"].low()
    self.pins["2A"].low()
    self.pins["3A"].low()
    self.pins["4A"].low()
  

class Button:
  """
  We'll use the IRQ (interrupt request) API to have a function
  called whenever our button is pressed.
  """

  def __init__(self):
    
    # Value of the button
    self.pressed = False

    # Set pin, IRQ
    self._pin = Pin(2, Pin.IN)
    self._pin.irq(self.IRQHandler, Pin.IRQ_RISING)

  def isPressed(self):
    return self._pin.value()
  
  def IRQHandler(self, pinObject):
    """
    This function is called by micropython when the value of the button pin changes.
    We'll use it to update our self.pressed variable.
    """
    self.pressed = pinObject.value()

  def registerIRQHandler(self, handler):
    """
    If we need to add another basic handler, we'll use this method.
    """
    self._pin.irq(handler, Pin.IRQ_RISING)

  def setOnPress(self, onPress):
    """
    The function passed to this method will only be called if the button is being
    pressed.
    """

    # Here's our handler function...
    def handler(pinObject):
      # Only call onPressed if the button was actually pressed
      if pinObject.value(): 
        onPress()

    # Register the handler
    self.registerIRQHandler(handler)


class Buzzer:
  """
  For controlling the buzzer.
  The buzzer is active, so all it needs is a digital input
  """

  def __init__(self):
    self.pin = Pin(22)
  
  def on(self):
    self.pin.high()
  
  def off(self):
    self.pin.low()


class IRSensor:
  """
  A class representing an infrared sensor
  """

  def __init__(self, pin):
     self.pin = ADC(pin)
  
  def read(self):
    return self.pin.read_u16()

class IRSensorArray:
  """
  Communicates with the array of sensors on the TBM1
  """
  
  def __init__(self):
    self.sensors = {
      "left": IRSensor(28),
      "front": IRSensor(27),
      "right": IRSensor(26)
    }
  
  def read_all(self):
    out = {}
    for key in self.sensors:
      out[key] = self.sensors[key].read()
  
  def read(self, key):
    return self.sensors[key].read()