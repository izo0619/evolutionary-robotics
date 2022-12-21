import numpy as np
import matplotlib.pyplot as plt

# backLegSensorValues = np.load('data/backLegSensorValues.npy')
# frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
# plt.plot(backLegSensorValues, lineWidth=2)
# plt.plot(frontLegSensorValues)
# plt.legend(["backLeg", "frontLeg"])
bl_targetAngles = np.load('data/bl_targetAngles.npy')
fl_targetAngles = np.load('data/fl_targetAngles.npy')
plt.plot(bl_targetAngles)
plt.plot(fl_targetAngles)
plt.legend(["backLeg", "frontLeg"])
plt.show()