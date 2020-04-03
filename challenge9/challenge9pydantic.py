from typing import list
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: datetime = None
    friends: List[int] = []
    

json = {
    'id':'123',
    'signup_ts': '2019-06-01',
    'friends': [1, 2, '3']

}
user = user(**json)
print(user.id)
print(repr(user.sighup_ts))
print(user.sighup_ts)
print(user.friends)
print(user.dict())

class Admin(user):
    rights: str

json = {
    'id':'123',
    'signup_ts': '2019-06-01',
    'friends': [1, 2, '3']
    'rights': 'full'
}
ad = Admin(**json)
print(ad.friends)
print(ad.id)
print(ad.rights)
print(ad.name)