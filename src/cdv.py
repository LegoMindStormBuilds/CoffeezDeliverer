from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

#>INFO:
#
#
#
#
#
#
# Create your objects here.
cdv = MSHub()
mm = MotorPair('A','B')
ds = DistanceSensor('D')


# Write your program here.
cdv.speaker.beep()
