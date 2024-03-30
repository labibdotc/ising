import algorithms
import matplotlib.pyplot as plt
import MatrixLattice as matrix
import numpy as np

param_N = 10
param_T = 0.000001
param_kB = 1#1.380649E-23
param_J = 1
param_ncycles = 150

algorithms.clonesOn = False
algorithms.plotsOn = False

# Create the lattice using the parameters
globalLattice = matrix.MatrixLattice(param_J, param_N)

# Initialize arrays for plotting
magnetizationArr = []
energiesArr = []
tempArr = []

#
# Run the algorithms on the lattice
#

# energies_m, mag_m = algorithms.runMetropolis(globalLattice, plt, param_ncycles, param_T, param_kB)
# energies_w, mag_w = algorithms.runWolff(globalLattice, plt, param_ncycles, param_T, param_J)

## Metropolis ##
# for n in range(5):
#   energies_m, mag_m = algorithms.runMetropolis(globalLattice, plt, param_ncycles, param_T, param_kB)
#   mag_m = np.absolute(mag_m[10:])
#   print(np.std(mag_m))
#   magnetizationArr.append(np.std(mag_m))
#   tempArr.append(param_T)
#   param_T = param_T + 0.01

## Wolff ##
for n in range(50):
  energies_w, mag_w, _ = algorithms.runWolff(globalLattice, plt, param_ncycles, param_T, param_J)
  mag_w = np.absolute(mag_w[100:])
  energies_w = np.absolute(energies_w[100:])
  print(np.std(mag_w))
  print(np.std(energies_w))
  magnetizationArr.append(np.std(mag_w))
  energiesArr.append(np.std(energies_w))
  tempArr.append(param_T)
  param_T = param_T + 0.1

plt.plot(tempArr, magnetizationArr)
plt.xlabel('Temperature (Nondimensionalized)')
plt.ylabel('Average Abs Val Std Dev Magnetization (Stable Zone)')
plt.title('Std Dev Magnetization vs. Temperature')
plt.show()

plt.plot(tempArr, energiesArr)
plt.xlabel('Temperature (Nondimensionalized)')
plt.ylabel('Average Abs Val Std Dev Energy (Stable Zone)')
plt.title('Std Dev Energy vs. Temperature')
plt.show()

print("Done")