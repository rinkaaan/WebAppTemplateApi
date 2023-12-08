from api.app import session
from models.resources.user import User


def get(user):
    q: User = session.query(User).filter(User.id == user).one_or_none()
    print(q.email)
    return q.dump()
