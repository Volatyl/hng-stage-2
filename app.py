from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///persons.db'
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name


@app.route('/api', methods=['POST'])
def create_person():
    try:
        data = request.get_json()
        name = data['name']

        new_person = Person(name=name)
        db.session.add(new_person)
        db.session.commit()

        return jsonify({'message': 'Person created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def person(id):
    person = Person.query.filter_by(id=id).first()

    if not person:
        return jsonify({'error': 'Person not found'}), 404

    if request.method == 'GET':
        return jsonify({'name': person.name})

    if request.method == 'PUT':
        try:
            data = request.get_json()
            new_name = data['name']

            person.name = new_name
            db.session.commit()

            return jsonify({'message': 'Person updated successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    if request.method == 'DELETE':
        db.session.delete(person)
        db.session.commit()
        return jsonify({'message': 'Person deleted successfully'}), 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
