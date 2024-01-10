from flask import Blueprint, jsonify, request
from sqlalchemy.orm import sessionmaker

from app import engine
from models import Base, Position

position_routes = Blueprint('position_routes', __name__)

Session = sessionmaker(bind=engine)


@position_routes.route('/position', methods=['GET'])
def get_positions():
    session = Session()
    id = request.args.get('id')
    if id is not None:
        position = session.query(Position).get(id)
        if position is None:
            return jsonify({'message': 'Position not found'}), 404
        return jsonify(str(position))
    positions = session.query(Position).all()
    session.close()
    return jsonify([position.to_dict() for position in positions])


@position_routes.route('/position', methods=['POST'])
def add_position():
    session = Session()
    theta1 = request.json.get('theta1')
    theta2 = request.json.get('theta2')
    theta3 = request.json.get('theta3')
    position = Position(theta1=theta1, theta2=theta2, theta3=theta3)
    session.add(position)
    session.commit()
    return jsonify(str(position)), 201


@position_routes.route('/position/<int:id>', methods=['DELETE'])
def delete_position(id):
    session = Session()
    position = session.query(Position).get(id)
    if position is None:
        return jsonify({'message': 'Position not found'}), 404
    session.delete(position)
    session.commit()
    return jsonify({'message': 'Position deleted'}), 200
