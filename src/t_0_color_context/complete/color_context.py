import sys
from types import TracebackType
from typing import Final, Literal, Optional, Type
from color import Color

_write:Final = sys.stdout.write


class ColorContext:
    color: Final[Color]

    def __init__(self, color: Color = Color.Red):
        self.color = color

    def __enter__(self):
        sys.stdout.write = lambda arg: _write(f"{self.color.value}{arg}{Color.Default.value}")
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> Literal[False]:
        """Ensures that resources get released on exiting.

        Args:
            exc_type (Optional[Type[BaseException]]): Type of exception.
            exc_value (Optional[BaseException]): Exception
            exc_tb (Optional[TracebackType]): Traceback

        Returns:
            Literal[False]: Always returns false, indicating that the exception should be re-raised.
        """
        sys.stdout.write = _write
        return False
