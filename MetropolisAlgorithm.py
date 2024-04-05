import LatticeInterface
import numpy as np
import random

def metropolisAlgorithm(lattice: LatticeInterface, kB: float, T: float, nCycles: int, animate: bool) -> tuple[list[float], list[float]]:
  energies = []
  avgMag = []
  clones = []
  if (animate):
    clones.append(lattice.clone())

  E = lattice.getE()
  energies.append(E)
  for n in range(nCycles):
    # for i in range(lattice.getN()):# Pick a lattice site i
    #   lattice.flipSpin(i)# Flip the spin at that site
    #   E1 = lattice.getE()
    #   deltaE = E1 - E# Calculate the change in energy ΔE
    #   if (deltaE < 0 or (random.random() < np.exp(-deltaE/(kB*T)))):
    #     E = E1
    #   else:
    #     lattice.flipSpin(i)# Swap the spin back
    i = random.randint(0, lattice.getN() - 1)
    lattice.flipSpin(i)# Flip the spin at that site
    E1 = lattice.getE()
    deltaE = E1 - E# Calculate the change in energy ΔE
    if (deltaE < 0 or (random.random() < np.exp(-deltaE/(kB*T)))):
      E = E1
    else:
      lattice.flipSpin(i)# Swap the spin back  
    energies.append(E)
    avgMag.append(lattice.getM())
    if (animate):
      clones.append(lattice.clone())
  return energies, avgMag, clones