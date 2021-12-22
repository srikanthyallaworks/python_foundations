from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    """Application user
    """
    id: int
    login: str
    given_name: str
    surname: str
