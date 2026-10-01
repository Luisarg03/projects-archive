# Libreria para formularios
# objetos para definir tipo de campos
from wtforms import Form, validators
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.fields.html5 import EmailField
from .models import User

# Campos y validaciones
# Mi clase debe heredar de Form
class LoginForm(Form):
    # Mis campos, deben resivir sus label si o si
    cuit = StringField('Cuit')

    id = StringField('Id')

class RegisterForm(Form):
    user = StringField(
        'Nombre',
        [validators.InputRequired(message='Usiario requerido'),
         validators.Length(min=2, max=50, message='Usuario error')]
         )
    
    name2 = StringField(
        'Apellido',
        [validators.InputRequired(message='Usiario requerido'),
         validators.Length(min=2, max=50, message='Usuario error')]
         )

    email = EmailField('Correo electronico', [
                        validators.Length(min=11, max=90),
                        validators.InputRequired(message='Email requerido'),
                        validators.Email(message='Ingrese un email valido')
    ])

    cuit = StringField('CUIT', [
        validators.InputRequired(message='CUIT requerido'), validators.Length(min=4, message='Clave demasiada corta')
    ])

    accept = BooleanField('', [
        validators.InputRequired()])

    # Varificaion de datos duplicados
    def validate_cuit(self, cuit):
        if User.get_cuit(cuit.data):
            raise validators.ValidationError('Este CUIT ya existe')

    def validate_email(self, email):
        if User.get_email(email.data):
            raise validators.ValidationError('Email en uso')