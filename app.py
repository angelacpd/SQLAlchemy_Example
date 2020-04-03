from flask import Flask, request
from flask_restful import Resource, Api
from models import People, Activities

app = Flask(__name__)
api = Api(app)


class Person(Resource):
    def get(self, name):
        person = People.query.filter_by(name=name).first()
        try:
            response = {
                'name': person.name,
                'age': person.age,
                'id': person.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'message': 'Person not found.'
            }
        return response

    def put(self, name):
        person = People.query.filter_by(name=name).first()
        data = request.json
        if 'name' in data:
            person.name = data['name']
        if 'age' in data:
            person.age = data['age']
        person.save()
        response = {
            'id': person.id,
            'name': person.name,
            'age': person.age
        }
        return response

    def delete(self, name):
        person = People.query.filter_by(name=name).first()
        message = 'Person {} was successfully deleted.'.format(person.name)
        person.delete()
        return {'status': 'success', 'mesaage': message}


class ListPeople(Resource):
    def get(self):
        people = People.query.all()
        response = [{'id': i.id, 'name': i.name, 'age': i.age} for i in people]
        return response

    def post(self):
        data = request.json
        person = People(name=data['name'], age=data['age'])
        person.save()
        response = {
            'id': person.id,
            'name': person.name,
            'age': person.age
        }
        return response


class ListActivities(Resource):
    def get(self):
        activities = Activities.query.all()
        response = [{'id': i.id, 'name': i.name, 'people': i.people.name} for i in activities]
        return response

    def post(self):
        data = request.json
        people = People.query.filter_by(name=data['people']).first()
        activity = Activities(name=data['name'], people=people)
        activity.save()
        response = {
            'people': activity.people.name,
            'name': activity.name,
            'id': activity.id
        }
        return response


api.add_resource(Person, '/person/<string:name>/')
api.add_resource(ListPeople, '/people/')
api.add_resource(ListActivities, '/activities/')

if __name__ == '__main__':
    app.run(debug=True)
