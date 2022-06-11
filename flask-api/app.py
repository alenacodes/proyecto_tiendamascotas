# 0. ejecutamos pip install flask flask-sqlalchemy flask-migrate flask-cors
# 1. Crear modelos
# 2. importamos las librerias de flask
#from crypt import methods
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Usuario, Region, Comuna, Descuento, Descuento_producto, Producto
from flask_cors import CORS, cross_origin
from logging import exception

# 3. instanciamos la app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Conten-Type'
app.url_map.strict_slashes = False
app.config['DEBUG'] = False
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

Migrate(app, db)

# 5. Creamos la ruta por defecto para saber si mi app esta funcionado
# 6. ejecutamos el comando en la consola: python app.py o python3 app.py y revisamos nuestro navegador
@app.route('/')
def index():
    return 'Hola desde gitpod'

# 7. Ruta para consultar todos los Usuarios
@app.route('/usuarios', methods=['GET'])
def getUsuarios():
    try:
        
        user = Usuario.query.all()
        #user = list(map(lambda x: x.serialize(), user))
        toreturn = [usi.serialize() for usi in user]
        #return jsonify(user),200 # Es ok y codifica a tipo Json
        return jsonify(toreturn),200 # Es ok y codifica a tipo Json
    except Exception:
        exception ("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un ERROR"}), 500

# 12. Ruta para agregar usuario
@app.route('/usuarios', methods=['POST'])
def addUsuario():
    try:
        user = Usuario()
       
        # asignar a variables lo que recibo mediante post
        user.primer_nombre = request.json.get('primer_nombre')
        user.segundo_nombre = request.json.get('segundo_nombre')
        user.apellido_paterno = request.json.get('apellido_paterno')
        user.apellido_materno = request.json.get('apellido_materno')
        user.direccion = request.json.get('direccion')
        #if not user:
        Usuario.save(user)
        return jsonify(user.serialize()),200
        #else:
        #    return jsonify({"msg": "El usuario ya existe"}), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500
    
   

# 13. Creamos metodo para consultar un usuario en especifico por ID
@app.route('/usuarios/<id>', methods=['GET'])
def getUsuario(id):
    try:
        user = Usuario.query.get(id)
                 
        if not user:
            return jsonify({"msg": "El ID de usuario no existe"}), 200
        else:
            return jsonify(user.serialize()),200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500


# 14. Borrar usuario
@app.route('/usuarios/<id>', methods=['DELETE'])
def deleteUsuario(id):
    try:
        user = Usuario.query.get(id)
        if not user:
            return jsonify({"msg": "El ID de usuario no existe"}), 200
        else:
            Usuario.delete(user)
            return jsonify(user.serialize()),200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500
        
# 15. Modificar Usuario
@app.route('/usuarios/<id>', methods=['PUT'])
def updateUsuario(id):
    try:
        user = Usuario.query.get(id)
        
        user.primer_nombre = request.json.get('primer_nombre')
        user.segundo_nombre = request.json.get('segundo_nombre')
        user.apellido_paterno = request.json.get('apellido_paterno')
        user.apellido_materno = request.json.get('apellido_materno')
        user.direccion = request.json.get('direccion')
        
        Usuario.save(user)
        return jsonify(user.serialize()),200
        
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500




# 8. comando para iniciar mi app flask: flask db init
# 9. comando para migrar mis modelos:   flask db migrate
# 10. comando para crear nuestros modelos como tablas : flask db upgrade
# 11. comando para iniciar la app flask: flask run

# 4. Configurar los puertos nuestra app 
if __name__ == '__main__':
    app.run(port=5000, debug=True)