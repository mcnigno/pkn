from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
class Matrix(Model):
    id = Column(Integer, primary_key=True)
    base = Column(String(255), nullable=True)
    counter = Column(Integer)


class Codes(Model):
    id = Column(Integer, primary_key=True)
    code = Column(String(255), nullable=True)


class Discipline(Model):
    id = Column(Integer, primary_key=True)
    code = Column(Integer)
    name = Column(String(255), nullable=True)

class DocType(Model):
    id = Column(Integer, primary_key=True)
    code = Column(String(255), nullable=True)
    name = Column(String(255), nullable=True)

class Unit(Model):
    id = Column(Integer, primary_key=True)
    code = Column(String(255), nullable=True)
    name = Column(String(255), nullable=True)

    def __repr__(self):
        return self.code


class Request(Model):
    id = Column(Integer, primary_key=True)
    #unit = # picklist from unit table
    unit_id = Column(Integer, ForeignKey('unit.id'), nullable=False)
    unit = relationship("Unit") 
