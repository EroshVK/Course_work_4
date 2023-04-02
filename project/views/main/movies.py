from flask import request
from flask_restx import Namespace, Resource

from project.container import movie_service
from project.setup.api.models import movie
from project.setup.api.parsers import page_parser, status_page_parser

movies_ns = Namespace('movies')


@movies_ns.route('/')
class GenresView(Resource):
    @movies_ns.expect(status_page_parser)
    @movies_ns.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all genres.
        """
        status = request.args.get('status')
        return movie_service.get_all(status=status, **page_parser.parse_args())


@movies_ns.route('/<int:genre_id>/')
class GenreView(Resource):
    @movies_ns.response(404, 'Not Found')
    @movies_ns.marshal_with(movie, code=200, description='OK')
    def get(self, director_id: int):
        """
        Get genre by id.
        """
        return movie_service.get_item(director_id)
