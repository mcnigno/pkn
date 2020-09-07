from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi

from . import appbuilder, db

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""
from app.models import Unit, Request, Discipline, Doctype, Matrix
class DisciplineView(ModelView):
    datamodel = SQLAInterface(Discipline)

class DoctypeView(ModelView):
    datamodel = SQLAInterface(Doctype)

class MatrixView(ModelView):
    datamodel = SQLAInterface(Matrix)

class UnitView(ModelView):
    datamodel = SQLAInterface(Unit)

from app.helpers import askcode
from flask import flash

class RequestView(ModelView):
    datamodel = SQLAInterface(Request)

    def post_add(self, item):
        print("POST ADD FUNCTION IS RUNNING *********************************")
        #print(item.discipline)
        code = askcode(item.unit, item.discipline, item.doctype)
        flash("Your code is: " + code, category="info")


appbuilder.add_view(
        DisciplineView,
        "Discipline",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    ) 
appbuilder.add_view(
        DoctypeView,
        "DocType",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    ) 
appbuilder.add_view(
        MatrixView,
        "Matrix",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    ) 

appbuilder.add_view(
        UnitView,
        "Units",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    ) 

appbuilder.add_view(
        RequestView,
        "Requests",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    ) 

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
