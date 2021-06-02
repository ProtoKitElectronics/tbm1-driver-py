from machine import Pin

class IRSensor:
  """
  A class representing the infrared sensors
  
  In TBM1, the IR sensors are always powered. The only pin we need to access
  is the output pin of those sensors, which will be pulled to 0v when the sensor
  is triggered (it's normally at 3.3v).

  Thanks to the IRQ (interrupt request) API that micropython provides, we can tell
  our robot to call a function (or "handler") whenever the value of a pin changes.
  We'll use this to update 

  """
  def __init__(self, output_pin):
    
    # The value of the sensor
    self.isBlocked = False

    # Set pin and IRQ
    self.pin = Pin(output_pin, Pin.IN)
    self.pin.irq(self.IRQHandler, Pin.IRQ_RISING)
  
  def IRQHandler(self, pinObject):
    """
    This function will be called by micropython when the sensor's value changes.
    When this happens, micropython will pass a new pin object. We'll use that to
    get the new value of our sensor.
    """

    # pinObject.value() is true if the output pin is 3.3v
    # I.e. the sensor is not blocked
    self.isBlocked = not pinObject.value()
  
  def registerIRQHandler(self, handler):
    """
    If we need to set a custom IRQ handler later on, we'll use this method.
    """
    self.pin.irq(handler, Pin.IRQ_RISING)
