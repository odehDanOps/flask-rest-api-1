from flask import jsonify

from flask_restful import Resource

import models

class CourseList(Resource):
    def get(self):
        return jsonify({'courses': [{'Python Basics'}]})

class Course(Resource):
    def get(self, id):
        return jsonify({'title': 'Python Basics'})

    def put(self, id):
        return jsonify({'title': 'Python Basics'})

    def delete(self, id):
        return jsonify({'title': 'Python Basics'})
