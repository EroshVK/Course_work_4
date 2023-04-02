from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режисер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Стив Энтин'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True),
    'description': fields.String(required=True),
    'trailer': fields.String(required=True),
    'year': fields.Integer(required=True),
    'rating': fields.Float(required=True),
    'genre_id': fields.Integer(required=True),
    'director_id': fields.Integer(required=True),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director),
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True),
    'email': fields.String(required=True, max_length=100),
    'name': fields.String(max_length=100),
    'surname': fields.String(max_length=100),
    'favorite_genre': fields.String(max_length=100),
    'favorite_movie': fields.String(max_length=100)
})

auth: Model = api.model('Авторизация', {
    'email': fields.String(required=True, example='tets@test.com'),
    'password': fields.String(required=True, example='qwerty'),
})

auth_result: Model = api.model('', {
    'access_token': fields.String(required=True),
    'refresh_token': fields.String(required=True),
})
