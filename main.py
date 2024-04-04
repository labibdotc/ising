import algorithms
import matplotlib.pyplot as plt
import MatrixLattice as matrix
import numpy as np

# Set parameters
param_N = 10
param_T = 0.0000001 # Zero
param_kB = 1
param_J = 1
param_ncycles = 500

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

# energies_m, mag_m, clones_m = algorithms.runMetropolis(globalLattice, plt, param_ncycles, param_T, param_kB)
# energies_w, mag_w, clones_w = algorithms.runWolff(globalLattice, plt, param_ncycles, param_T, param_J)

# ani = algorithms.animate(clones_w, plt)
# plt.show()

# Metropolis ##
# for n in range(250):
#   energies_m, mag_m, clones_m = algorithms.runMetropolis(globalLattice, plt, param_ncycles, param_T, param_kB)
#   mag_m = np.absolute(mag_m[100:])
#   energies_w = np.absolute(energies_m[100:])
#   print(np.std(mag_m))
#   print(np.std(energies_m))
#   magnetizationArr.append(np.std(mag_m))
#   energiesArr.append(np.std(energies_m))
#   tempArr.append(param_T)
#   param_T = param_T + 0.04
#   print('Iteration: ', n)

## Wolff ##
# for n in range(500):
#   energies_w, mag_w, clones_w = algorithms.runWolff(globalLattice, plt, param_ncycles, param_T, param_J)
#   mag_w = np.absolute(mag_w[200:])
#   energies_w = np.absolute(energies_w[200:])
#   print(np.std(mag_w))
#   print(np.std(energies_w))
#   magnetizationArr.append(np.std(mag_w))
#   energiesArr.append(np.std(energies_w))
#   tempArr.append(param_T)
#   param_T = param_T + 0.01

plt.plot(tempArr, magnetizationArr)
plt.xlabel('Temperature (Nondimensionalized)')
plt.xlim(0,10)
plt.ylabel('Average Std Dev Abs Val Magnetization (Stable Zone)')
plt.suptitle('Std Dev Magnetization vs. Temperature', fontsize=14)
plt.title('Metropolis Algorithm | 250 Temperatures, 500 Cycles', fontsize=12)
plt.show()

plt.plot(tempArr, energiesArr)
plt.xlabel('Temperature (Nondimensionalized)')
plt.xlim(0,10)
plt.ylabel('Average Std Dev Abs Val Energy (Stable Zone)')
plt.suptitle('Std Dev Energy vs. Temperature', fontsize=14)
plt.title('Metropolis Algorithm | 250 Temperatures, 500 Cycles', fontsize=12)
plt.show()

print("Done")