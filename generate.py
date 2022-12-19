import pyrosim.pyrosim as pyrosim


def Create_World():
    # tell pyrosim the name of the file where information about the world you're about to create should be stored
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1, 1, 1])
    pyrosim.End()

Create_World()