from enum import Enum
from dataclasses import dataclass, field

@dataclass
class Settings():
    password: str = field(default="1234")
    two_factor: bool = field(default=False)
    volume: int = field(default=7)
