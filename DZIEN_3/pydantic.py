import dataclasses
from typing import List,Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

@dataclass
class User:
    id:int
    name:str = "Jan Kowalski"
    friends: List[int] = dataclasses.field(default_factory=lambda : [0])
    age: Optional[int] = dataclasses.field(default=None,
                                           metadata=dict(title='Wiek użytkownika',description='nie kłam!'))
    height: Optional[int] = Field(None,title="wzrost w cm",ge=50,le=250)


user = User(id='33')
print(user)

us1 = User(55,"Ala Kot",[2,],56,200)
print(us1)
