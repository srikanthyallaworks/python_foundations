from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    """Represents a system user.
    """
    id: int
    login: str
    given_name: str
    surname: str
