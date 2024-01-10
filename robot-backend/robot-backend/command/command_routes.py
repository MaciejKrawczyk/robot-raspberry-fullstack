from flask import Blueprint, jsonify, request
from sqlalchemy.orm import sessionmaker

from app import engine
from models import Command

command_routes = Blueprint('command_routes', __name__)

Session = sessionmaker(bind=engine)


@command_routes.route('/command', methods=['GET'])
def get_commands():
    session = Session()
    head = session.query(Command).filter(Command.previous_id.is_(None)).first()
    if head is None:
        return jsonify([]), 200
    commands = []
    current = head
    while current is not None:
        commands.append(current.to_dict())
        current = current.next_node
    session.close()
    return jsonify(commands)


@command_routes.route('/command', methods=['POST'])
def add_command():
    session = Session()
    command_type = request.json.get('command_type')
    position_id = request.json.get('position_id')
    tail = session.query(Command).filter(Command.next_id.is_(None)).first()
    command = Command(command_type=command_type, position_id=position_id, previous_id=tail.id if tail else None)
    session.add(command)
    session.flush()  # to get the id of the new command
    if tail:
        tail.next_id = command.id
        session.add(tail)
    session.commit()
    return jsonify(command.to_dict()), 201


@command_routes.route('/command/<int:id>', methods=['DELETE'])
def delete_command(id):
    session = Session()
    command = session.query(Command).get(id)
    if command is None:
        return jsonify({'message': 'Command not found'}), 404
    if command.previous_node:
        command.previous_node.next_id = command.next_id
        session.add(command.previous_node)
    if command.next_node:
        command.next_node.previous_id = command.previous_id
        session.add(command.next_node)
    session.delete(command)
    session.commit()
    return jsonify({'message': 'Command deleted'}), 200
