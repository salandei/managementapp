from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import user
from .forms import DepartmentForm, UserAssignForm, RoleForm
from .. import db
from ..models import Department, User, Role


# Department Views

@user.route('/departments', methods=['GET', 'POST'])
@login_required
def list_departments():
    """
    List all departments
    """
    departments = Department.query.all()

    return render_template('departments.html',
                           departments=departments, title="Departments")

@user.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    """
    Add a department to the database
    """
    add_department = True

    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(name=form.name.data,
                                description=form.description.data)
        try:
            # add department to the database
            db.session.add(department)
            db.session.commit()
            flash('You have successfully added a new department ', 'success')
        except:
            # in case department name already exists
            flash('Department name already exists', 'error')

        # redirect to departments page
        return redirect(url_for('user.list_departments'))

    # load department template
    return render_template('department.html', action="Add",
                           add_department=add_department, form=form,
                           title="Add Department")

@user.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    """
    Edit a department
    """
    add_department = False

    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the department', 'success')

        # redirect to the departments page
        return redirect(url_for('user.list_departments'))

    form.description.data = department.description
    form.name.data = department.name
    return render_template('department.html', action="Edit",
                           add_department=add_department, form=form,
                           department=department, title="Edit Department")

@user.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    """
    Delete a department from the database
    """
    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash('You have successfully deleted the department', 'success')

    # redirect to the departments page
    return redirect(url_for('user.list_departments'))

    return render_template(title="Delete Department")  # this return statement is redundant

# Role Views

@user.route('/roles')
@login_required
def list_roles():
    """
    List all roles
    """
    roles = Role.query.all()
    return render_template('roles.html',
                           roles=roles, title='Roles')

@user.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
    """
    Add a role to the database
    """
    add_role = True

    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data,
                    description=form.description.data)

        try:
            # add role to the database
            db.session.add(role)
            db.session.commit()
            flash('You have successfully added a new role', 'success')
        except:
            # in case role name already exists
            flash('Role name already exists', 'error')

        # redirect to the roles page
        return redirect(url_for('user.list_roles'))

    # load role template
    return render_template('role.html', add_role=add_role,
                           form=form, title='Add Role')

@user.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):
    """
    Edit a role
    """
    add_role = False

    role = Role.query.get_or_404(id)
    form = RoleForm(obj=role)
    if form.validate_on_submit():
        role.name = form.name.data
        role.description = form.description.data
        db.session.add(role)
        db.session.commit()
        flash('You have successfully edited the role', 'success')

        # redirect to the roles page
        return redirect(url_for('user.list_roles'))

    form.description.data = role.description
    form.name.data = role.name
    return render_template('role.html', add_role=add_role,
                           form=form, title="Edit Role")

@user.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
    """
    Delete a role from the database
    """
    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have successfully deleted the role', 'success')

    # redirect to the roles page
    return redirect(url_for('user.list_roles'))

    return render_template(title="Delete Role")  # this return statement is redundant

# User Views

@user.route('/users')
@login_required
def list_users():
    """
    List all users
    """
    users = User.query.all()
    return render_template('users.html',
                           users=users, title='Users')

@user.route('/users/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_user(id):
    """
    Assign a department and a role to a user
    """
    user = User.query.get_or_404(id)

    form = UserAssignForm(obj=user)

    if form.validate_on_submit():
        user.department = form.department.data
        user.role = form.role.data
        db.session.add(user)
        db.session.commit()
        flash('You have successfully assigned a department and role', 'success')

        # redirect to the roles page
        return redirect(url_for('user.list_users'))

    return render_template('user.html',
                           user=user, form=form,
                           title='Assign User')
