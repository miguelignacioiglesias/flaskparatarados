#--------------------------------------------------------------------
# Importamos el framework Flask
from flask import Flask

# Importamos la función que nos permit el render de los templates,
# recibir datos del form, redireccionar, etc.
from flask import render_template, request,redirect, send_from_directory, flash

# Importamos el módulo que permite conectarnos a la BS
from flaskext.mysql import MySQL

# Importamos las funciones relativas a fecha y hora
from datetime import datetime

# Importamos paquetes de interfaz con el sistema operativo.
import os
#--------------------------------------------------------------------

# Creamos la aplicación
app = Flask(__name__)

#--------------------------------------------------------------------

#--------------------------------------------------------------------
# Creamos la conexión con la base de datos:
mysql = MySQL()
# Creamos la referencia al host, para que se conecte a la base
# de datos MYSQL utilizamos el host localhost
app.config['MYSQL_DATABASE_HOST']='localhost'
# Indicamos el usuario, por defecto es user
app.config['MYSQL_DATABASE_USER']='miguel'
# Sin contraseña, se puede omitir
app.config['MYSQL_DATABASE_PASSWORD']='1234'
# Nombre de nuestra BD
app.config['MYSQL_DATABASE_BD']='gastos'
# Creamos la conexión con los datos
mysql.init_app(app)

#-------------------------------------------------------------------
## Pantalla de login ##
@app.route('/')
def index():
    global validacion
    validacion = False
    return render_template('index.html')

@app.route('/ingresar', methods=['POST'])
def ingresar():
    _usuario  = request.form["txtUsuario"]
    _password = request.form["txtPassword"]
    sql     = "SELECT * FROM `usuarios` WHERE `usu_name` LIKE %s"
    conn    = mysql.connect()
    cursor  = conn.cursor()
    cursor.execute(sql,_usuario)
    global usuario
    usuario = cursor.fetchall()

    # Si el usuario está logueado, lo redirijo a la pagina solicitada
    if usuario!=() and _password==usuario[0][1]:
        global validacion
        validacion=True
        return redirect("inicio")
    else: 
        return render_template("index.html")



#--------------------------------------------------------------------
# Estas líneas de código las requiere python para que 
# se pueda empezar a trabajar con la aplicación
if __name__=='__main__':
    #Corremos la aplicación en modo debug
    app.run(debug=True, port=8000)
#--------------------------------------------------------------------
