from functools import wraps
from timeit import default_timer as timer
from typing import Callable, ParamSpec, TypeVar

Params = ParamSpec("Params")
Ret = TypeVar("Ret")

TIME_UNITS: tuple[str, ...] = ("s", "ms", "ns",)

def format_time(time_s: float) -> str:
    current_unit: int = 0
    while True:
        if time_s >= 1.:
            break
        if current_unit < (len(TIME_UNITS) - 1):
            current_unit += 1
            time_s *= 1000
        else:
            break
    return f"{time_s}{TIME_UNITS[current_unit]}"

def timethis(fn: Callable[Params, Ret]) -> Callable[Params, Ret]:
    @wraps(fn)
    def _fn_with_timing(*args: Params.args, **kwargs: Params.kwargs) -> Ret:
        time_before: float = timer()
        ret: Ret = fn(*args, **kwargs)
        time_after: float = timer()
        print(f"Function '{fn.__name__}' args={args}, kwargs={kwargs}\n\t" +
              f"took: {format_time(time_after-time_before)}")
        return ret
    return _fn_with_timing
