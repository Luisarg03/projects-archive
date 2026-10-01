# Blueprint nos permite trabajar con apps modulables
# render_t renderiza los html
# Importo mi clase formulario de forms
from flask import Blueprint, render_template, request
from flask import flash, redirect, url_for, abort
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from .forms import LoginForm, RegisterForm
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
        user = User.get_cuit(form.cuit.data)
        id = User.get_by_id(form.id.data)

        if user:
            login_user(user)
            flash('Usuario encontrado')
            return redirect(url_for('.get_cuit_info'))

        elif id:
            login_user(id)
            flash('Usuario encontrado')
            return redirect(url_for('.get_cuit_info'))

        else:
            flash('CUIT no encontrado', 'error')

    return render_template(
                           'index.html',
                           title='index',
                           form=form,
                           active='index')

@page.route('/register/', methods=['GET', 'POST'])
def register():

    # recibo los datos del form
    form = RegisterForm(request.form)

    # validacion de la petición
    if request.method == 'POST' and form.validate():
        username = User.create_element(
            form.user.data,
            form.name2.data,
            form.email.data,
            form.cuit.data
        )

        print('Usuario creado exitosamente')
        flash('Usuario registrado.')
        login_user(username)
        welcome_mail(username)
        return redirect(url_for('.index'))

    return render_template(
                            'auth/register.html',
                            title='register',
                            form=form,
                            active='register')

@page.route('/cuit/')
def get_cuit_info():
    user = User.get_user(current_user.user)
    name2 = User.get_user_name2(current_user.name2)
    email = User.get_email(current_user.email)
    cuit = User.get_cuit(current_user.cuit)

    return render_template(
        'task/show.html',
        title='CUIT',
        user=user,
        name2=name2,
        email=email,
        cuit=cuit)