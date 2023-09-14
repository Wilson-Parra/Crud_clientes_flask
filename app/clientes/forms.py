from flask_wtf import FlaskForm 
from wtforms import StringField ,SubmitField,PasswordField
from wtforms.validators import InputRequired, Email
from wtforms import PasswordField, StringField, validators

class ClientForm(FlaskForm):

    username = StringField('Ingrese el nombre del cliente:', validators=[
        InputRequired(message="El nombre del cliente es obligatorio")
    ])
    
    email = StringField('Ingrese su correo electrónico:', validators=[
                                    InputRequired(message="El correo electrónico es obligatorio"),
                                    Email(message="Ingrese un correo electrónico válido")
])
    
    password = PasswordField('Ingrese una contraseña segura:', validators=[
        InputRequired(message="La contraseña es obligatoria"),
        validators.Length(min=8, message="La contraseña debe tener al menos 8 caracteres"),
        validators.Regexp(
            regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$",
            message="La contraseña debe contener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial"
        )
    ])

    submit = SubmitField("Registrar")
    

class EditClientForm(FlaskForm):
        username = StringField('Ingrese el nombre del cliente:', validators=[
        InputRequired(message="El nombre del cliente es obligatorio")
    ])
    
        email = StringField('Ingrese su correo electrónico:', validators=[
                                    InputRequired(message="El correo electrónico es obligatorio"),
                                    Email(message="Ingrese un correo electrónico válido")
])
    
        password = PasswordField('Ingrese una contraseña segura:', validators=[
        InputRequired(message="La contraseña es obligatoria"),
        validators.Length(min=8, message="La contraseña debe tener al menos 8 caracteres"),
        validators.Regexp(
            regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$",
            message="La contraseña debe contener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial"
        )
    ])
 

        submit = SubmitField("Registrar")