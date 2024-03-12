from LatticeInterface import LatticeInterface
import numpy as np

class MatrixLattice(LatticeInterface):

  _rows = None
  _cols = None
  _J = None
  _lattice = None

  def __init__(self, J: float, r: int, c: int = None):
    """constructor"""
    self._J = J
    self._rows = r
    self._cols = r if (c == None) else c
    self.generateLattice()

  def getN(self) -> int:
    """Returns the number of lattice points"""
    return self._rows * self._cols

  def getJ(self) -> float:
    """Returns the parameter J"""
    return self._J

  def getSpin(self, i: int) -> int:
    """Returns the spin state [-1, 1] of the specified lattice point"""
    r, c = self._rc(i)
    return self._lattice[r][c]

  def setSpin(self, i: int, spin: int):
    """Sets the spin state [-1, 1] of the specified lattice point"""
    r, c = self._rc(i)
    self._lattice[r][c] = spin

  def getNeighbors(self, i: int) -> list[int]:
    """Returns a list of indices of the neighbors of the specified lattice point"""
    r,c = self._rc(i)

    n_out = []
    if (r > 0):
      n_out.append(self._index(r - 1, c))
    else:
      n_out.append(self._index(self._rows - 1, c))
    if (r < self._rows - 1):
      n_out.append(self._index(r + 1, c))
    else:
      n_out.append(self._index(0, c))
    if (c > 0):
      n_out.append(self._index(r, c - 1))
    else:
      n_out.append(self._index(r, self._cols - 1))
    if (c < self._cols - 1):
      n_out.append(self._index(r, c + 1))
    else:
      n_out.append(self._index(r, 0))

    return n_out

  def clone(self) -> LatticeInterface:
    newLattice = MatrixLattice(self._J, self._rows, c=self._cols)

    for i in range(self.getN()):
      r,c=self._rc(i)
      newLattice.setSpin(i, self.getSpin(i))

    return newLattice

  def _rc(self, i: int) -> tuple[int, int]:
    return int(np.floor(i / self._cols)), int(np.floor(i % self._cols))

  def _index(self, row: int, col: int) -> int:
    return int((self._cols * row) + col)

  def _exists(self, r: int, c: int) -> bool:
    return r >= 0 and r < self._rows and c >= 0 and c < self._cols

  def generateLattice(self):
    """Generates the lattice with size n by n with each lattice point being 1 or -1"""
    self._lattice = np.random.choice([-1,1], size = (self._rows, self._cols))