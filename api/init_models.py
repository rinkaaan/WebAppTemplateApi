from sqlalchemy.orm import declarative_base

Base = declarative_base()

from api.resources.pet.model import Pet
from api.resources.user.model import User
