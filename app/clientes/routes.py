from . import clientes
from flask import render_template,redirect, flash
from .forms import EditClientForm
from .forms import ClientForm  

import app
import os 

#Crear las rutas del blueprint
@clientes.route('/crear', methods =["GET", "POST"])
def crear():
    c = app.models.Cliente()
    form = ClientForm()
    if form.validate_on_submit():
        #el formulario va a llenar 
        #el nuevo objeto cliente
        #automaticamente
        form.populate_obj(c)
        app.db.session.add(c)
        app.db.session.commit()
        flash("registro exitoso")
        return redirect("/clientes/listar")
    return render_template('new_cliente.html', form = form)

@clientes.route('/listar')
def listar():
    #Traer los productos que este en database
    clientes = app.Cliente.query.all()
    #Mostrar la vista de listar, enviandole los productos seleccionados 
    return render_template('listar_clientes.html' ,
                           clientes=clientes)


@clientes.route('/editar/<cliente_id>',
                methods =['GET' , 'POST'])
def editar(cliente_id):

    #seleccionar el producto
    #con el id
    c = app.models.Cliente.query.get(cliente_id)
    #cargo el fomrulario
    #con los atributos del producto
    form_edit = EditClientForm(obj = c)
    if form_edit.validate_on_submit():
        form_edit.populate_obj(c) 
        app.db.session.commit()
        flash("cliente editado")
        return redirect("/clientes/listar")
    return render_template('new_cliente.html',
                    form = form_edit)

@clientes.route('/eliminar/<cliente_id>',
                methods =['GET' , 'POST'])
def eliminar(cliente_id):
   
    #sellecionar elemento a eliminar
    c = app.models.Cliente.query.get(cliente_id)
    #eliminar producto
    app.db.session.delete(c)
    app.db.session.commit()
    flash ("cliente eliminado")
    return redirect("/clientes/listar")

 