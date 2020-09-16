from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_appbuilder.models.mixins import AuditMixin
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
class Matrix(Model, AuditMixin):
    id = Column(Integer, primary_key=True)
    base = Column(String(255), nullable=False)
    counter = Column(Integer)


class Discipline(Model):
    id = Column(Integer, primary_key=True)
    code = Column(String(255), nullable=False, unique=False)
    name = Column(String(255), nullable=True, unique=True)
    start = Column(Integer, unique=True)
    stop = Column(Integer, unique=True) 
    
    def __repr__(self):
        if self.name:
            return self.code + " " + self.name
        return self.code 
    
class Doctype(Model):
    id = Column(Integer, primary_key=True)
    code = Column(String(255), nullable=False, unique=True)
    name = Column(String(255), nullable=True, unique=True)
    
    def __repr__(self):
        return self.code
    

class Unit(Model):
    id = Column(Integer, primary_key=True)
    code = Column(String(255), nullable=True, unique=True)
    name = Column(String(255), nullable=True, unique=True)
    
    def __repr__(self):
        return self.code 
    
class Request(Model, AuditMixin):
    id = Column(Integer, primary_key=True)
    #unit = # picklist from unit table
    unit_id = Column(Integer, ForeignKey('unit.id'), nullable=False)
    unit = relationship("Unit") 

    discipline_id = Column(Integer, ForeignKey('discipline.id'), nullable=False)
    discipline = relationship("Discipline")

    doctype_id = Column(Integer, ForeignKey('doctype.id'), nullable=False)
    doctype = relationship("Doctype")

    quantity = Column(Integer, nullable=False, default=1)

from flask import Markup
class Codes(Model, AuditMixin):
    id = Column(Integer, primary_key=True)

    code = Column(String(255), nullable=True, unique=True)
    contractor_code = Column(String(255), nullable=True, unique=True)

    request_id = Column(Integer, ForeignKey('request.id'), nullable=False)
    request = relationship("Request")

    internal_note = Column(String(255), nullable=True)

    def document_code(self):

        p_code = '<span class=code_code>'+self.code+'<span>' 
        if self.internal_note:
            p_code = '<span class=code_code>'+self.code+'<span>'+'<span class=code_note>Note<span>'
        '''
        if self.contractor_code and self.internal_note:
            return Markup('<strong class=code_note>'+self.code+'<strong>')
        '''
        if self.contractor_code:
            return Markup('<span class=code_contractor>'+p_code+'<span>')
        
        return Markup(p_code) 
   
