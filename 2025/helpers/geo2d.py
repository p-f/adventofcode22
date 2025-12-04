from enum import Enum

type Coordinate = complex
type CoordinateLike = complex | tuple[int, int]

def to_coordinate(x: int, y: int) -> Coordinate:
    return x + 1j * y

def to_xy(coord: CoordinateLike) -> tuple[int, int]:
    if isinstance(coord, tuple):
        return coord
    else:
        return int(coord.real), int(coord.imag)

def is_in_grid(num_columns: int, num_rows: int, coordinate: CoordinateLike) -> bool:
    x: int
    y: int
    x, y = to_xy(coordinate)
    if x < 0 or x >= num_columns:
        return False
    if y < 0 or y >= num_rows:
        return False
    return True

class Directions(Enum):
    UP = to_coordinate(0, -1)
    DOWN = -UP
    LEFT = to_coordinate(-1, 0)
    RIGHT = -LEFT
