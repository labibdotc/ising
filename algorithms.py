## WolffAlgorithm.py - Husam Adam, Trevor Wallace, Ryan Afzal, Labib Afia
## This file implements the animation functions, test algorithms, and runs Metropolis/Wolff

import LatticeInterface as li
import MetropolisAlgorithm as m_a
import WolffAlgorithm as w_a
from matplotlib import animation, rc
from IPython.display import HTML
import numpy as np

#Decide if you want clones and plots
clonesOn = True
plotsOn = True

#Test the algorithm on a lattice
def testAlgorithm(name, lattice: li.LatticeInterface, algorithm, plot) -> tuple[list[float],list[float],list[li.LatticeInterface]]:
  #Runs the algorithm on the lattice
  energies, avgMag, clones = algorithm(lattice)

  #Plot the results when necessary
  if (plotsOn):
    energiesPlot = plot
    magPlot = plot

    energiesPlot.plot(energies)
    energiesPlot.xlabel('Step')
    energiesPlot.ylabel('Energy (J)')
    energiesPlot.title(f'{name} Energy vs Step')
    energiesPlot.show()

    magPlot.plot(avgMag)
    magPlot.xlabel('Step')
    magPlot.ylabel('Average Magnetization')# A/m?
    magPlot.title(f'{name} Average Magnetization vs Step')
    magPlot.show()

  return energies, avgMag, clones

#Runs Metropolis on our lattice
def runMetropolis(lattice: li.LatticeInterface, plot, N, T, kB) -> tuple[list[float],list[float],list[li.LatticeInterface]]:
  name = f'Metropolis (T={T}K)'
  return testAlgorithm(name, lattice.clone(), lambda x: m_a.metropolisAlgorithm(x, kB, T, N, clonesOn), plot)

#Runs Wolff on our lattice
def runWolff(lattice: li.LatticeInterface, plot, N, T, J) -> tuple[list[float],list[float]]:
  name = f'Wolff (T={T}K)'
  return testAlgorithm(name, lattice.clone(), lambda x: w_a.wolffAlgorithm(x, J, T, N, clonesOn), plot)

#Animate the lattice using its clones
def animate(clones, plot):
    fig, ax = plot.subplots()
    i = 0

    #Update a specific frame of the animation
    def update(frame):
        nonlocal i
        #Make sure we're not out of range
        if i < len(clones):
          ax.clear()
          ax.imshow(clones[i]._lattice.copy(), cmap='binary', interpolation='nearest')
          ax.set_title(f"Step {frame}")
          i += 1
          return ax

    #Make and return our animation
    ani = animation.FuncAnimation(fig, update, frames=len(clones), interval=20, repeat=False)
    return ani