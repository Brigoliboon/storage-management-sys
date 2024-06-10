from typing import Union
from pydantic import BaseModel
from secrets import token_hex
def add_user(Name,Email,Is_admin,data):
    if Email not in data:
        data[token_hex(16)]= user(name=Name,email=Email,is_admin=Is_admin)
class user(BaseModel):
    name: str
    email: str
    is_admin: Union[bool,None] = None
user_info = {
    '9a881f1624d50dbad2af51e9919b72e7': user(name='test1',email='test1@gmail.com', is_admin= False)
}