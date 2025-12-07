from enum import Enum
from typing import Callable, Generator, Generic, TypeVar

from helpers.io import read_lines

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

T = TypeVar('T')
class Grid(Generic[T]):
    columns: int
    lines: int
    values: list[list[T]]

    def __init__(self, columns: int, lines: int, default: T) -> None:
        super().__init__()
        self.columns = columns
        self.lines = lines
        self.values = [
            [default for _ in range(lines)] for _ in range(columns)
        ]

    def _get_coord_xy(self, c: CoordinateLike) -> tuple[int, int]:
        x: int
        y: int
        x, y = to_xy(c)
        assert 0 <= x < self.columns, f"x out of range: {x} (0 to {self.columns})"
        assert 0 <= y < self.lines, f"y out of range: {y} (0 to {self.lines})"
        return x,y

    def __setitem__(self, index: CoordinateLike, value: T):
        x, y = self._get_coord_xy(index)
        self.values[x][y] = value

    def __getitem__(self, index: CoordinateLike) -> T:
        x, y = self._get_coord_xy(index)
        return self.values[x][y]

    def update_rect(self, corner1: CoordinateLike, corner2: CoordinateLike,
                    updater: Callable[[T], T]) -> None:
        x1, y1 = self._get_coord_xy(corner1)
        x2, y2 = self._get_coord_xy(corner2)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self[x, y] = updater(self[x, y])

    def all_values(self) -> Generator[T, None, None]:
        for c in self.values:
            for v in c:
                yield v

    def count_all(self, value: T) -> int:
        return sum(
            sum(1 for v in col if v == value)
            for col in self.values
        )

    def all_coordinates(self) -> Generator[CoordinateLike, None, None]:
        for y in range(self.lines):
            for x in range(self.columns):
                yield to_coordinate(x, y)

    def is_in_grid(self, coordinate: CoordinateLike) -> bool:
        return is_in_grid(self.columns, self.lines, coordinate)

    def neighbors_with_values(self, center: CoordinateLike
                              ) -> Generator[tuple[Coordinate, T], None, None]:
        for d in Directions:
            c: Coordinate = to_coordinate(*to_xy(center)) + d.value
            if self.is_in_grid(c):
                yield c, self[c]

    def print(self, format: Callable[[T], object] | None = None):
        _format: Callable[[T], object] = format or (lambda x: x)
        for y in range(self.lines):
            print(*(_format(self[x, y]) for x in range(self.columns)))

    def __str__(self) -> str:
        return str(self.values)

    @classmethod
    def read(cls, path: str) -> Grid[str]:
        lines: list[str] = list(read_lines(path))
        grid: Grid[str] = Grid(len(lines[0]), len(lines), '')
        for l_nr, line in enumerate(lines):
            for c_nr, ch in enumerate(line):
                grid[c_nr, l_nr] = ch
        return grid
