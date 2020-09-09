def sequencer():  
    # main setting
    separator = "-"
    serial_digits = 4
    # projects table
    prj = {}
    # main codec elements table for prj
    prj_fields = {
        "unit": 3,
        "doctype": 3,
        "matclass": 3
    }
    # any element has many sub elements

    # extra codec information table for prj
    # this options will be added to the matrix.
    prj_extra_fields = {
        "partner": 3,
        "mr": 0,
    }

    # matrix table
    matrix = {}

from app.models import Matrix
from app import db

def askcode(unit, discipline, doctype):
    #p = unit
    session = db.session
    
    project_number = "A8RX"
    entity = "TSC"
    
    params = [project_number, entity, str(unit.code), str(doctype.code), str(discipline.code)]

    base_data = "-".join(params)

    matrix = session.query(Matrix).filter(Matrix.base == base_data).first()

    if matrix:
        matrix.counter += 1
    else:
        matrix = Matrix()
        matrix.base = base_data
        matrix.counter = 1
        session.add(matrix)
    session.commit()
    return base_data + "-" + str(matrix.counter).zfill(4)
    

