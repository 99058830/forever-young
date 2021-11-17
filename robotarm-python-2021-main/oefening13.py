from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)
robotArm.speed = 2

for i in range(7):
   pak = robotArm.grab()
   if pak == True:
       print(pak)
       for x in range(1+i):
           robotArm.moveRight()
       for z in range(1+i):
           robotArm.drop()
           robotArm.moveLeft()
   else:
       break