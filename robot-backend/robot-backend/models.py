from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Position(Base):
    __tablename__ = 'positions'

    id = Column(Integer, primary_key=True)
    theta1 = Column(Float)
    theta2 = Column(Float)
    theta3 = Column(Float)

    def to_dict(self):
        return {
            'id': self.id,
            'theta1': self.theta1,
            'theta2': self.theta2,
            'theta3': self.theta3,
        }


class Command(Base):
    __tablename__ = 'command'

    id = Column(Integer, primary_key=True)
    command_type = Column(String)
    position_id = Column(Integer, ForeignKey('positions.id'))
    previous_id = Column(Integer, ForeignKey('command.id'))  # if null it is a head
    next_id = Column(Integer, ForeignKey('command.id'))  # if null it is a tail
    previous_node = relationship("Command", remote_side=[id], uselist=False, post_update=True,
                                 foreign_keys=[previous_id])
    next_node = relationship("Command", remote_side=[id], uselist=False, post_update=True,
                             foreign_keys=[next_id])  # new relationship

    def __repr__(self):
        return f'<Command {self.id} {self.command_type} {self.position_id} {self.previous_id} {self.next_id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'command_type': self.command_type,
            'position_id': self.position_id,
            'previous_id': self.previous_id,
            'next_id': self.next_id,  # new field
        }
