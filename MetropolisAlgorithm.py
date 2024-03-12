import LatticeInterface
import numpy as np
import random

def metropolisAlgorithm(lattice: LatticeInterface, kB: float, T: float, nCycles: int) -> tuple[list[float], list[float]]:
  energies = []
  avgMag = []

  E = lattice.getE()
  energies.append(E)
  for n in range(nCycles):
    for i in range(lattice.getN()):# Pick a lattice site i
      lattice.flipSpin(i)# Flip the spin at that site
      E1 = lattice.getE()
      deltaE = E1 - E# Calculate the change in energy ΔE
      if (deltaE < 0 or (random.random() < np.exp(-deltaE/(kB*T)))):
        pass# Accept the move
      else:
        lattice.flipSpin(i)# Swap the spin back

      E = E1
    energies.append(E)
    avgMag.append(lattice.getM())
  return energies, avgMag