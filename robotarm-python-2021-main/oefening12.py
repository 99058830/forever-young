from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
robotArm.speed = 2
for x in range(36):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for i in range(9):
            check = robotArm.moveRight()
            if check == False:
                robotArm.drop()
            print(check)
        for z in range(90):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
robotArm.wait()