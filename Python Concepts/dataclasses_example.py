"""
Dataclasses mostly contains data.
__dict__
no initialization.
has dunder methods.
"""

from dataclasses import dataclass, field


@dataclass
class Post:
    id: int
    content: str
    comments: list = field(default_factory=list)
    likes: int = 0


post = Post(1, "First Post")
print(post)

@dataclass(frozen=True)
class Tweet:
    id: int
    Tweet: str


t = Tweet(1, "Fist tweek")
# t.id = 2
print(t)
