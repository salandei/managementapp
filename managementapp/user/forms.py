from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField

from ..models import Department, Role


class DepartmentForm(FlaskForm):
    """
    Form to add or edit a department
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RoleForm(FlaskForm):
    """
    Form to add or edit a role
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UserAssignForm(FlaskForm):
    """
    Form to assign departments and roles to users
    """
    department = QuerySelectField(query_factory=lambda: Department.query.all(),
                                  get_label=lambda x: x.name, get_pk=lambda x: x.id)  # important! prevents "ValueError: too many values to unpack (expected 2)"
    role = QuerySelectField(query_factory=lambda: Role.query.all(),
                            get_label=lambda x: x.name, get_pk=lambda x: x.id)
    submit = SubmitField('Submit')
