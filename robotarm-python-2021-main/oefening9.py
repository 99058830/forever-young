from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
robotArm.speed = 2

for i in range(4):
    robotArm.grab()
    for y in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(4):
        robotArm.moveLeft()
robotArm.wait()