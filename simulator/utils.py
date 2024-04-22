from typing import Dict, Literal, Tuple, Union
import numpy as np
from numpy.typing import NDArray


class FluidCube:
    def __init__(
        self, size: int, dt: float, diffusion_rate: float, viscosity: float
    ) -> None:
        self.size = size
        self.dt = dt
        self.diffusion_rate = diffusion_rate
        self.viscosity = viscosity
        self.velocity: NDArray = np.zeros((size, size, size))
        self.tempVelocity: NDArray = np.zeros((size, size, size))
        self.smoke: NDArray = np.zeros((size, size, size))
        self.density: NDArray = np.zeros((size, size, size))

    def addDensity(self, coordinate: Tuple[int, int, int], amount: float) -> None:
        self.density[coordinate] += amount

    def addVelocity(self, coordinate: Tuple[int, int, int], amount: float) -> None:
        self.velocity[coordinate] += amount

    def diffuse(
        self,
        b: int,
    ) -> None: ...
