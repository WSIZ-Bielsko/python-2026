from pydantic import BaseModel, Field


class User(BaseModel):
    name: str
    age: int = Field(..., gt=0)
    occupation: str | None = None


if __name__ == '__main__':
    # instancje klasy User
    u1 = User(name='John', age=30)
    u2 = User(name='Alice', age=29, occupation='teacher')

    print(u1)
    print(u2)

    print(u1.name)  # John

    # instance --> dict --> instance

    ff = u1.model_dump()  # <class 'dict'> {'name': 'John', 'age': 30, 'occupation': None}
    print(type(ff), ff)

    uu = User.model_validate(ff)  # dict --> instance
    print(uu)
    print(u1 == uu)

    print('-'*60)
    # instance --> str (napis; json) ---> instance
    ss = u1.model_dump_json()
    print(type(ss), ss)

    ww = User.model_validate_json(ss)
    print(ww)
    print(u1 == ww)
