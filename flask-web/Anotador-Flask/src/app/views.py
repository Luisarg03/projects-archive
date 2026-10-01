# Blueprint nos permite trabajar con apps modulables
# render_t renderiza los html
# Importo mi clase formulario de forms
from flask import Blueprint, render_template, request
from flask import flash, redirect, url_for, abort
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Task
from .forms import LoginForm, RegisterForm, TaskForm
from . import login_manage
from . email import welcome_mail

# instancia de blueprint
page = Blueprint('page', __name__)


@login_manage.user_loader
def load_user(id):
    return User.get_by_id(id)

# Funcion que se activa a travez de un error
@page.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404
# el segundo valor es convencion para notificar el error


@page.route('/', methods=['POST', 'GET'])
def index():

    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User.get_user(form.username.data)

        if user and user.verify_password(form.password.data):
            login_user(user)
            flash('Usuario autenticado')
            return redirect(url_for('.tasks'))
        else:
            flash('Usuario y/o clave erroneas', 'error')

    return render_template(
                           'index.html',
                           title='index',
                           form=form,
                           active='index')


# Mi ruta recibe peticiones por GET y POST
@page.route('/login/', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('.tasks'))

    # recibo los datos del form
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User.get_user(form.username.data)

        if user and user.verify_password(form.password.data):
            login_user(user)
            flash('Usuario autenticado')
            return redirect(url_for('.tasks'))
        else:
            flash('Usuario y/o clave erroneas', 'error')  # 2°arg = categoria

    return render_template(
                            'auth/login.html',
                            title='login',
                            form=form,
                            active='login')


@page.route('/register/', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('.tasks'))

    # recibo los datos del form
    form = RegisterForm(request.form)

    # validacion de la petición
    if request.method == 'POST' and form.validate():
        user = User.create_element(
            form.username.data,
            form.email.data,
            form.password.data
        )

        print('Usuario creado exitosamente')
        print(user.id)
        flash('Usuario registrado.')
        login_user(user)
        welcome_mail(user)
        return redirect(url_for('.tasks'))

    return render_template(
                            'auth/register.html',
                            title='register',
                            form=form,
                            active='register')


@page.route('/logout/')
def logout():
    logout_user()
    flash('Session terminada')
    return redirect(url_for('.login'))


@page.route('/tasks/')
@page.route('/tasks/<int:page>')
@login_required
def tasks(page=1, per_page=4):
    paginations = current_user.tasks.paginate(page, per_page=per_page)
    tasks = paginations.items

    return render_template(
                            'task/list.html',
                            title='task',
                            tasks=tasks,
                            paginations=paginations,
                            page=page,
                            active='tasks')


@page.route('/tasks/show/<int:task_id>/')
def get_task(task_id):
    task = Task.query.get_or_404(task_id)

    return render_template('task/show.html', title='Tarea', task=task)


@page.route('/tasks/new/', methods=['GET', 'POST'])
@login_required
def new_task():
    form = TaskForm(request.form)

    if request.method == 'POST' and form.validate():
        task = Task.create_element(form.title.data,
                                   form.description.data,
                                   current_user.id)

        if task:
            flash('Tarea creada exitosamente')
            return redirect(url_for('.tasks'))

    return render_template(
                            'task/new.html',
                            title='nueva tarea',
                            form=form,
                            active='new_task')


@page.route('/tasks/edit/<int:task_id>/', methods=['POST', 'GET'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)

    if task.user_id != current_user.id:
        abort(404)

    form = TaskForm(request.form, obj=task)

    if request.method == 'POST' and form.validate():
        task = Task.update_element(task.id,
                                   form.title.data,
                                   form.description.data)

        if task:
            flash('Tarea editada correctamente')
            return redirect(url_for('.tasks'))

    return render_template('task/edit.html', title='editar tarea', form=form)


@page.route('/tasks/delete/<int:task_id>/', methods=['POST', 'GET'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)

    if task.user_id != current_user.id:
        abort(404)

    if Task.delete_element(task_id):
        flash('Tarea elminada exitosamente')

    return redirect(url_for('.tasks'))
