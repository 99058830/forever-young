from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
robotArm.speed = 2
for x in range(5):
    for i in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for y in range(2):
        robotArm.moveRight()
robotArm.wait()