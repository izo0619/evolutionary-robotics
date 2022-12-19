import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath()) # find data that comes with pybullet
p.setGravity(0,0,-9.8) # add gravitational force
planeId = p.loadURDF("plane.urdf") # add floor plane
p.loadSDF("world.sdf")
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print("forloop iteration: " + str(i)) 
p.disconnect()