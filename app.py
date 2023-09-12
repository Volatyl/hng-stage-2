from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///persons.db'
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attributes = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f'Attributes: {self.attributes}'

    @validates('attributes')
    def validate_attributes(self, key, attributes):
        if not isinstance(attributes, dict):
            raise ValueError("Attributes must be a dictionary")

        if not all(isinstance(value, str) for value in attributes.values()):
            raise ValueError("All values in attributes must be strings")

        return attributes


@app.route('/api', methods=['POST'])
def create_person():
    try:
        data = request.get_json()
        attributes = data.get('attributes')

        if not attributes:
            return jsonify({'error': 'Attributes not provided'}), 400

        new_person = Person(attributes=attributes)
        db.session.add(new_person)
        db.session.commit()

        return jsonify({'message': 'Person created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def person(id):
    person = Person.query.filter_by(id=id).first()

    if request.method == 'GET':
        if not person:
            return jsonify({'error': 'Person not found'}), 404

        return jsonify({'id': person.id, 'attributes': person.attributes})

    if request.method == 'PUT':
        if not person:
            return jsonify({'error': 'Person not found'}), 404
        try:
            data = request.get_json()
            new_attributes = data.get('attributes')

            if not new_attributes:
                return jsonify({'error': 'Attributes not provided'}), 400

            person.attributes = new_attributes
            db.session.commit()

            return jsonify({'message': 'Person updated successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    if request.method == 'DELETE':
        if not person:
            return jsonify({'error': 'Person not found'}), 404

        db.session.delete(person)
        db.session.commit()
        return jsonify({'message': 'Person deleted successfully'}), 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
