import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str

    def __init__(self, name, age):
        self.name = name
        self.age = age


roma = User(first_name='Roman Koshkin', last_name='Koshkin')
