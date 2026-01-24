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
    u1.computers.append(Computer(name='Xiaomi Pad', price=500))

    jj = u1.model_dump_json()
    print(jj)
    # jj = '{"name":"John","birth_date":"1990-12-01T00:00:00","computers":[{"name":"MacBook","price":1000.0},{"name":"Xiaomi Pad","price":500.0}]}'
    uu = User.model_validate_json(jj)
    print(uu)
    print(u1 == uu)
