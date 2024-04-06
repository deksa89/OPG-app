import dataclasses
import datetime
import jwt
from django.conf import settings

from ..models import Farm
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..models import Farm

@dataclasses.dataclass
class UserDataClass:
    ime: str
    prezime: str
    naziv_opg: str
    adresa: str
    telefon: int
    email: str
    password: str = None
    id: int = None
    
    @classmethod
    def from_instance(cls, user: "Farm"):
        return cls(
            ime=user.ime,
            prezime=user.prezime,
            naziv_opg=user.naziv_opg,
            adresa=user.adresa,
            telefon=user.telefon,
            email=user.email,
            id=user.id
            )
        
        
def create_user(user_dc: "UserDataClass"):
    instance = Farm(
        ime = user_dc.ime,
        prezime = user_dc.prezime,
        naziv_opg = user_dc.naziv_opg,
        adresa = user_dc.adresa,
        telefon = user_dc.telefon,
        email = user_dc.email
    )
    
    if user_dc.password is not None:
        instance.set_password(user_dc.password)
    
    instance.save()
    
    return UserDataClass.from_instance(instance)


def user_email_selector(email: str):
    user = Farm.objects.filter(email=email).first()
    
    return user


def create_token(user_id: int):
    payload = dict(
        id=user_id,
        exp=datetime.datetime.now() + datetime.timedelta(hours=24),
        iat=datetime.datetime.now()
    )
    
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")
    
    return token