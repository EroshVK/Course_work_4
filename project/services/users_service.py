from flask import current_app
import jwt

from project.dao.user import UserDAO
from project.tools.security import generate_password_hash


class UsersService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_data: dict[str, str]):
        user_data['password'] = generate_password_hash(user_data['password'])
        return self.dao.create(user_data)

    def update(self, user_data):
        self.dao.update(user_data)
        return self.dao

    def update_password(self, email, new_password):
        self.dao.update_password(email, new_password)

    def delete(self, uid):
        self.dao.delete(uid)

    def get_email_from_token(self, token):
        data = jwt.decode(jwt=token, key=current_app.config['SECRET_KEY'],
                          algorithms=current_app.config['JWT_ALGORITHM'])
        user_email = data.get('email')
        return user_email

    def get_from_token(self, token):
        user_email = self.get_email_from_token(token)
        user = self.get_by_email(email=user_email)
        return user
