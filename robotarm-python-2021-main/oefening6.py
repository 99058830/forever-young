from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
for i in range(7):
    robotArm.moveRight()
for x in range(8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    for z in range(2):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()