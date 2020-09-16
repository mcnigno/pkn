from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi


from . import appbuilder, db
from flask import g

def get_user():
    return g.user
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
from app.models import Unit, Request, Discipline, Doctype, Matrix, Codes
from flask_appbuilder.models.sqla.filters import FilterEqualFunction, FilterStartsWith

class DisciplineView(ModelView):
    datamodel = SQLAInterface(Discipline)
    list_columns = ['code','name','start','stop']

class DoctypeView(ModelView):
    datamodel = SQLAInterface(Doctype)
    list_columns = ['code','name']

class MatrixView(ModelView):
    datamodel = SQLAInterface(Matrix)
    list_columns = ['base', 'counter'] 

class UnitView(ModelView):
    datamodel = SQLAInterface(Unit)
    list_columns = ['code','name']

class CodesView(ModelView):
    datamodel = SQLAInterface(Codes)
    list_columns = ['request.discipline','code', 'contractor_code']
    edit_columns = ['code', 'contractor_code']
    show_columns = ['code', 'contractor_code','internal_note']
  
class MyCodesView(ModelView):
    datamodel = SQLAInterface(Codes)
    list_columns = ['request.discipline','document_code', 'contractor_code']
    base_filters = [['created_by', FilterEqualFunction, get_user]]
    base_order = ('changed_on','desc')

from app.helpers import askcode
from flask import flash
from app import db
from flask import url_for, redirect, g, session
 
class RequestView(ModelView):
    datamodel = SQLAInterface(Request)
    list_columns = ['quantity','unit','discipline','doctype', 'changed_by','changed_on']
    add_columns = ['unit','discipline','doctype', 'quantity']
    #base_permissions = ['can_add']
    related_views = [CodesView] 
    
    def post_add(self, item):
        print("POST ADD FUNCTION IS RUNNING *********************************",item.id)
        #print(item.discipline)
        codes_list = askcode(item.unit, item.discipline, item.doctype, item.quantity)
        
        # Database is alway a single concurrent session
        session = db.session
        for code in codes_list:
            newcode = Codes()
            newcode.code = code
            
            newcode.request = item
            print('block here 2')
            session.add(newcode)
            flash("Your code is: " + code, category="info")
        session.commit()
        g.last_request = item.id
    def post_add_redirect(self):
        try:
            return redirect(url_for('RequestView.show',pk=g.last_request))
        except:
            #return redirect(self.get_redirect())
            return redirect(url_for('MyCodesView.list'))



appbuilder.add_view(
        DisciplineView,
        "Discipline",
        icon="fa-folder-open-o",
        category="Setting",
        category_icon='fa-envelope'
    ) 
appbuilder.add_view(
        DoctypeView,
        "DocType",
        icon="fa-folder-open-o",
        category="Setting",
        category_icon='fa-envelope'
    ) 
appbuilder.add_view(
        MatrixView,
        "Matrix",
        icon="fa-folder-open-o",
        category="Setting",
        category_icon='fa-envelope'
    ) 

appbuilder.add_view(
        UnitView,
        "Units",
        icon="fa-folder-open-o",
        category="Setting",
        category_icon='fa-envelope'
    ) 

appbuilder.add_view(
        RequestView,
        "Requests",
        icon="fa-folder-open-o",
        category="My Codes",
        category_icon='fa-envelope'
    )
appbuilder.add_view(
        CodesView,
        "List of Codes",
        icon="fa-folder-open-o",
        category="Setting",
        category_icon='fa-envelope'
    ) 

appbuilder.add_view(
        MyCodesView,
        "My Codes List",
        icon="fa-folder-open-o",
        category="My Codes",
        category_icon='fa-envelope'
    )
'''
appbuilder.add_link('New Request','http://localhost:5000/requestview/add',icon="fa-folder-open-o",
        category="My Codes",
        category_icon='fa-envelope') 
'''
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
from app.helpers import upload_old_codes

upload_old_codes()