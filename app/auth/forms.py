from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField ,SubmitField
from wtforms.validators import InputRequired,NumberRange
from  flask_wtf.file import FileField, FileRequired, FileRequired, FileAllowed
from wtforms.validators import InputRequired, Email
from wtforms import PasswordField, StringField, validators




class LoginForm(FlaskForm):
    username = StringField(
                label ='nombre de usuario :',
                         validators=[InputRequired(
                             message="Nombre requerido")
                             ])
    
    password = PasswordField(
                label = 'Ingrese una contraseña segura:', 
                validators=[
                InputRequired(
                    message="La contraseña es obligatoria"),
            
    ])
    
    submit = SubmitField("Iniciar Sesión")

