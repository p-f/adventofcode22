from typing import Generator

def read_lines(file_path: str) -> Generator[str, None, None]:
    with open(file_path, "r") as handle:
        while l := handle.readline():
            yield l.strip()
