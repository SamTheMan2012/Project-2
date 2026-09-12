# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       genio                                                        #
# 	Created:      9/12/2026, 12:11:35 PM                                       #
# 	Description:  IQ2 project                                                  #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

brain.screen.print("Hello IQ2")

rm = Motor(Ports.PORT4,True)
lm = Motor(Ports.PORT2)

dt = DriveTrain(rm,lm)

arm = Motor(Ports.PORT7)

hand = Motor(Ports.PORT1)

dt.drive_for(FORWARD,10)