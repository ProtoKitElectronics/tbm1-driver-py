from machine import Pin

class Button:
  """
  As with the IR Sensor, we'll use the IRQ (interrupt request) API to have a function
  called whenever our button is pressed.
  """
  def __init__(self, pin):
    
    # Value of the button
    self.pressed = False

    # Set pin, IRQ
    self._pin = Pin(pin, Pin.IN)
    self._pin.irq(self.IRQHandler, Pin.IRQ_RISING)
  
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