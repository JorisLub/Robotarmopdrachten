from typing import TextIO
from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
for x in range(7):
    robotArm.moveRight()
for p in range(8):
    for j in range(1):
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
        for j in range(2):
            robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()