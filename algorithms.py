import LatticeInterface as li
import MetropolisAlgorithm as m_a
import WolffAlgorithm as w_a
from matplotlib import animation, rc
from IPython.display import HTML
import numpy as np

clonesOn = True
plotsOn = True

def testAlgorithm(name, lattice: li.LatticeInterface, algorithm, plot) -> tuple[list[float],list[float],list[li.LatticeInterface]]:
  energies, avgMag, clones = algorithm(lattice)

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

def runMetropolis(lattice: li.LatticeInterface, plot, N, T, kB) -> tuple[list[float],list[float],list[li.LatticeInterface]]:
  name = f'Metropolis (T={T}K)'
  return testAlgorithm(name, lattice.clone(), lambda x: m_a.metropolisAlgorithm(x, kB, T, N, clonesOn), plot)

def runWolff(lattice: li.LatticeInterface, plot, N, T, J) -> tuple[list[float],list[float]]:
  name = f'Wolff (T={T}K)'
  return testAlgorithm(name, lattice.clone(), lambda x: w_a.wolffAlgorithm(x, J, T, N, clonesOn), plot)

def animate(clones, plot):
    fig, ax = plot.subplots()
    i = 0

    def update(frame):
        nonlocal i
        if i < len(clones):
          ax.clear()
          ax.imshow(clones[i]._lattice.copy(), cmap='binary', interpolation='nearest')
          ax.set_title(f"Step {frame}")
          i += 1
          return ax

    ani = animation.FuncAnimation(fig, update, frames=len(clones), interval=1, repeat=False)
    return ani