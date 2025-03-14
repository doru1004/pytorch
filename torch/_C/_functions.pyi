from typing import AnyStr, overload

from torch import Tensor

class UndefinedGrad:
    def __init__(self) -> None: ...
    def __call__(self, *inputs: Tensor) -> list[Tensor]: ...

class DelayedError:
    def __init__(self, msg: AnyStr, num_inputs: int) -> None: ...

    # __call__ should really be a higher-kinded type:
    # def __call__(self, arg: Tensor) -> Tensor: ...
    # def __call__(self, *args: Tensor * num_inputs) -> Tuple[Tensor * num_inputs]: ...

    @overload
    def __call__(self, i0: Tensor) -> Tensor: ...
    @overload
    def __call__(self, *args: Tensor) -> tuple[Tensor, ...]: ...
