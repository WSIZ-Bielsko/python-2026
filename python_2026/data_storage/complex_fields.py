from datetime import datetime

from pydantic import BaseModel


class Computer(BaseModel):
    name: str
    price: float


class User(BaseModel):
    name: str
    birth_date: datetime
    computers: list[Computer] = []


if __name__ == '__main__':
    u1 = User(name='John', birth_date=datetime(1990, 1, 1), computers=[Computer(name='MacBook', price=1000)])
    print(u1)
    print(u1.birth_date.time())

    jj = u1.model_dump_json()
    print(jj)
    uu = User.model_validate_json(jj)
    print(uu)
    print(u1 == uu)
