import pyrosim.pyrosim as pyrosim

# tell pyrosim the name of the file where information about the world you're about to create should be stored
pyrosim.Start_SDF("boxes.sdf")
# stores a box with initial position x=0, y=0, z=0.5, and length, width and height all equal to 1 meter
length = 1
width = 1
height = 1
x=0
y=0
z=0.5
# pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])
# pyrosim.Send_Cube(name="Box", pos=[x+1,y,z+1] , size=[length, width, height])
for x_pos in range (5):
    for y_pos in range(5):
        cm_height = 0
        z=0.5
        for i in range(10):
            i_length = length*(0.9**(i+1))
            i_width =  width*(0.9**(i+1))
            i_height = height*(0.9**(i+1))
            # z = cm_height + 0.5*i_height
            pyrosim.Send_Cube(name="Box", pos=[x_pos,y_pos,z+i] , size=[i_length, i_width, i_height])
            # cm_height += i_height
# tells pyrosim to close the sdf file
pyrosim.End()