import numpy as np
from WaterStoredInPlatform import WaterStoredInPlatform

print('case.1')
a=np.array([[2,2,2],[2,2,2],[2,2,2]])
amount=WaterStoredInPlatform(a)
print(a)
print('%d units of water can be stored in the above platform configuration' %amount)

print('case.2')
a=np.array([[2,2,2,2],[2,1,2,1],[2,2,2,1]])
amount=WaterStoredInPlatform(a)
print(a)
print('%d units of water can be stored in the above platform configuration' %amount)

print('case.3')
a=np.array([[3,3,3,3,3,3],[3,1,2,3,1,3],[3,1,2,3,1,3],[3,3,3,1,3,3]])
amount=WaterStoredInPlatform(a)
print(a)
print('%d units of water can be stored in the above platform configuration' %amount)

print('case.4')
a=np.array([[3,3,3,5,3,3],[3,0,1,3,1,3],[3,2,2,3,1,5],[3,3,3,3,3,3]])
amount=WaterStoredInPlatform(a)
print(a)
print('%d units of water can be stored in the above platform configuration' %amount)

print('case.5')
a=np.array([[3,3,3,5,3,3],[3,0,1,3,1,3],[3,2,2,3,1,5],[3,3,3,3,3,3]])
amount=WaterStoredInPlatform(a)
print(a)
print('%d units of water can be stored in the above platform configuration' %amount)

print('case.6')
a=np.array([[5,5,5,5,5],[9,1,1,1,5],[5,1,5,1,5],[5,1,1,1,5],[5,5,5,5,5]])
amount=WaterStoredInPlatform(a)
print(a)
print('%d units of water can be stored in the above platform configuration' %amount)