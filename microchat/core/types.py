from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, AsyncIterator, Generic, Literal, Protocol, TypeVar, overload
from typing import Awaitable, Generator, Iterable, Sequence

# type: ignore
T = TypeVar('T')
T_co = TypeVar('T_co', covariant=True)
T_contra = TypeVar('T_contra', contravariant=True)

MIMEType = Literal[
    "application",
    "audio",
    "image",
    "message",
    "multipart",
    "text",
    "video"
]


class AsyncSequence(Protocol[T_co]):
    @overload
    @abstractmethod
    async def __getitem__(self, index: int) -> T_co: ...
    @overload
    @abstractmethod
    async def __getitem__(self, index: slice) -> Sequence[T_co]: ...
    async def index(self, value: Any, start: int = ..., stop: int = ...) -> int: ...  # noqa
    async def count(self, value: Any) -> int: ...
    async def __aiter__(self) -> AsyncIterator[T_co]: ...


class BoundSequence(ABC, Awaitable[Sequence[T]], AsyncSequence[T], Generic[T]):
    @overload
    @abstractmethod
    def __setitem__(self, index: int, value: T) -> None: ...
    @overload
    @abstractmethod
    def __setitem__(self, index: slice, values: Iterable[T]) -> None: ...
    def __setitem__(self, index, value) -> None: ...
    @overload
    @abstractmethod
    def __delitem__(self, index: int) -> None: ...
    @overload
    @abstractmethod
    def __delitem__(self, index: slice) -> None: ...
    def __delitem__(self, index) -> None: ...
    @abstractmethod
    async def insert(self, index: int, value: T) -> None: ...
    async def append(self, value: T) -> None: ...
    async def extend(self, values: Iterable[T]) -> None: ...
    def __iadd__(self, x: Iterable[T]) -> BoundSequence[T]: ...
    def __await__(self) -> Generator[Any, None, Sequence[T]]: ...


if __name__ == "__main__":
    pass
