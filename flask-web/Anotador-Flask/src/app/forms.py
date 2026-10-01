# Libreria para formularios
# objetos para definir tipo de campos
from wtforms import Form, validators
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.fields.html5 import EmailField
from .models import User


# Mis validaciones
def pokemon_validator(form, field):
    if field.data == 'pokemon' or field.data == 'Pokemon':
        raise validators.ValidationError('Este usuario no esta permitido')


# Campos y validaciones
# Mi clase debe heredar de Form
class LoginForm(Form):
    # Mis campos, deben resivir sus label si o si
    username = StringField('Usuario', [
        validators.InputRequired(message='Debes ingresar un usuario'),
        pokemon_validator
    ])

    password = PasswordField('Clave', [
        validators.InputRequired(message='Debes ingresar una clave')
    ])


class RegisterForm(Form):
    username = StringField(
        'Usuario',
        [validators.InputRequired(message='Usiario requerido'),
         validators.Length(min=4, max=50, message='Usuario error'),
         pokemon_validator]
         )

    email = EmailField('Correo electronico', [
                        validators.Length(min=11, max=90),
                        validators.InputRequired(message='Email requerido'),
                        validators.Email(message='Ingrese un email valido')
    ])

    password = PasswordField('Clave', [
        validators.InputRequired(message='Clave requerida'), validators.Length(min=4, message='Clave demasiada corta'), validators.EqualTo('confirm_pass', message='Las claves no coinciden')
    ])

    confirm_pass = PasswordField('Confirma tu contraseña')

    accept = BooleanField('', [
        validators.InputRequired()])

    # Varificaion de datos duplicados
    def validate_username(self, username):
        if User.get_user(username.data):
            raise validators.ValidationError('Usuario en uso')

    def validate_email(self, email):
        if User.get_email(email.data):
            raise validators.ValidationError('Email en uso')


class TaskForm(Form):
    title = StringField('Titulo', [
        validators.InputRequired(message='Campo requerido'),
        validators.Length(min=4, max=50, message='min 4 max 50')
    ])

    description = TextAreaField('Descripción', [
        validators.InputRequired(message='Campo requerido')
    ], render_kw={'rows': 5})
