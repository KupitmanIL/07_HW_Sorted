from dataclasses import dataclass, field

class Student:
    id: int
    name: str = field(compare=False)
    score: int = field(compare=False)