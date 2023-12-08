import logging
from datetime import datetime

from connexion import NoContent
from nguylinc_python_utils.sqlalchemy import deserialize_body, sanitize_body
from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError

from api.app import session
from models.resources.pet import Pet


def get_items(limit, user, animal_type=None, after_datetime=datetime.min):
    if isinstance(after_datetime, str):
        after_datetime = datetime.fromisoformat(after_datetime)
    q = session.query(Pet).filter(Pet.created_at > after_datetime)
    if animal_type:
        q = q.filter(Pet.animal_type == animal_type)
    q = q.filter(Pet.user_id == user)
    q = q.order_by(desc(Pet.created_at)).limit(limit)
    return [p.dump() for p in q], 200


def get(pet_id, user):
    q = session.query(Pet).filter(Pet.id == pet_id).filter(Pet.user_id == user).one_or_none()
    if q:
        return q.dump(), 200
    else:
        return NoContent, 404


def put(body, user):
    try:
        pet: Pet = deserialize_body(Pet, body)
        pet.created_at = datetime.now()
        pet.user_id = user
        session.add(pet)
        session.commit()
        session.refresh(pet)
        return pet.dump(), 201
    except IntegrityError as e:
        logging.error(e)
        session.rollback()
        return NoContent, 409


def patch(pet_id, body, user):
    body = sanitize_body(Pet, body)
    session.query(Pet).filter(Pet.id == pet_id).filter(Pet.user_id == user).update(body)
    session.commit()
    return NoContent, 200


def delete(pet_id, user):
    session.query(Pet).filter(Pet.id == pet_id).filter(Pet.user_id == user).delete()
    session.commit()
    return NoContent, 204
