# 0. ejecutamos pip install flask flask-sqlalchemy flask-migrate flask-cors
# 1. Crear modelos
# 2. importamos las librerias de flask
#from crypt import methods
#import email
#from os import access
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from sqlalchemy import desc
from models import db, Usuario, Usuario_car, Region, Comuna, Descuento, Descuento_producto, Producto, Producto_carrito 
from models import Provincias, Suscripcion, Donacion, Detalle, Venta, Vendedor, Despacho

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
#@app.jwt_required()
def index():
    return 'Hola desde gitpod'

# 7. Ruta para consultar todos los Usuarios
@app.route('/usuarios', methods=['GET'])
#@app.jwt_required()
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
#@app.jwt_required()
def addUsuario():
    try:
        user = Usuario()
       
        # asignar a variables lo que recibo mediante post
        user.correo = request.json.get('correo')
        user.password = request.json.get('password')
        user.estado = request.json.get('estado')    
        user.primer_nombre = request.json.get('primer_nombre')
        user.segundo_nombre = request.json.get('segundo_nombre')
        user.apellido_paterno = request.json.get('primer_apellido')
        user.apellido_materno = request.json.get('segundo_apellido')
        user.direccion = request.json.get('direccion')
        user.comuna_id = request.json.get('comuna')
        user.fono = request.json.get('fono')
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
#@app.jwt_required()
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
#@app.jwt_required()
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
#@app.jwt_required()
def updateUsuario(id):
    try:
        user = Usuario.query.get(id)
        user.correo = request.json.get('correo')
        user.password = request.json.get('password')
        user.estado = request.json.get('estado')    
        user.primer_nombre = request.json.get('primer_nombre')
        user.segundo_nombre = request.json.get('segundo_nombre')
        user.apellido_paterno = request.json.get('primer_apellido')
        user.apellido_materno = request.json.get('segundo_apellido')
        user.direccion = request.json.get('direccion')
        user.comuna_id = request.json.get('comuna')
        user.fono = request.json.get('fono')
        
        Usuario.save(user)
        return jsonify(user.serialize()),200
        
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#----------------------------------------------------------------------

# Ruta para agregar productos
@app.route('/producto', methods=['POST'])
#@app.jwt_required()
def addProducto():
    try:
        product = Producto()
       
        # asignar a variables lo que recibo mediante post
        product.id_producto = request.json.get('id_producto')
        product.codigo = request.json.get('codigo')   
        product.nombre = request.json.get('nombre')
        product.valor_venta = request.json.get('valor_venta')
        product.stock = request.json.get('stock')
        product.descripcion = request.json.get('descripcion')
        product.imagen = request.json.get('imagen')
        product.estado = request.json.get('estado')
        #if not user:
        Producto.save(product)
        return jsonify(product.serialize()),200
        #else:
        #    return jsonify({"msg": "El usuario ya existe"}), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

# Ruta para consultar todos los productos
@app.route('/producto', methods=['GET'])
#@app.jwt_required()
def getProductos():
    try:
        
        product = Producto.query.all()
        #user = list(map(lambda x: x.serialize(), user))
        toreturn = [usi.serialize() for usi in product]
        #return jsonify(user),200 # Es ok y codifica a tipo Json
        return jsonify(toreturn),200 # Es ok y codifica a tipo Json
    except Exception:
        exception ("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un ERROR"}), 500

# Borrar Producto
@app.route('/producto/<id_producto>', methods=['DELETE'])
#@app.jwt_required()
def deleteProducto(id_producto):
    try:
        product = Producto.query.get(id_producto)
        if not product:
            return jsonify({"msg": "El ID de producto no existe"}), 200
        else:
            Producto.delete(product)
            return jsonify(product.serialize()),200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#Modificar Producto
@app.route('/producto/<id_producto>', methods=['PUT'])
#@app.jwt_required()
def updateProducto(id_producto):
    try:
        product = Producto.query.get(id_producto)
        product.id_producto = request.json.get('id_producto')
        product.codigo = request.json.get('codigo')   
        product.nombre = request.json.get('nombre')
        product.valor_venta = request.json.get('valor_venta')
        product.stock = request.json.get('stock')
        product.descripcion = request.json.get('descripcion')
        product.imagen = request.json.get('imagen')
        product.estado = request.json.get('estado')
        
        Producto.save(product)
        return jsonify(product.serialize()),200
        
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#--------------------------------------------------------------------------------
#Agregar regiones
@app.route('/region', methods=['POST'])
#@app.jwt_required()
def addRegiones():
    try:
        regionx = Region()
       
        # asignar a variables lo que recibo mediante post
        regionx.id_region = request.json.get('id_region')
        regionx.nombre = request.json.get('nombre')
        regionx.numero= request.json.get('numero')   
        
        Region.save(regionx)
        return jsonify(regionx.serialize()),200
        #else:
        #    return jsonify({"msg": "El usuario ya existe"}), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#------------------------------------------------------------------
#para consultar una region  en especifico por ID
@app.route('/region/<id_region>', methods=['GET'])
#@app.jwt_required()
def getRegion(id_region):
    try:
        rgx = Region.query.get(id_region)
                 
        if not rgx:
            return jsonify({"msg": "El ID de usuario no existe"}), 200
        else:
            return jsonify(rgx.serialize()),200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500


#----------------------
#Consultar todas las regiones
@app.route('/region', methods=['GET'])
#@app.jwt_required()
def getRegiones():
    try:
        
        rgx = Region.query.all()
        #user = list(map(lambda x: x.serialize(), user))
        toreturn = [usi.serialize() for usi in rgx]
        
        return jsonify(toreturn),200 # Es ok y codifica a tipo Json
    except Exception:
        exception ("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un ERROR"}), 500

#--------------------------------------------
# Borrar Región por ID
@app.route('/region/<id_region>', methods=['DELETE'])
#@app.jwt_required()
def deleteRegion(id_region):
    try:
        rgx = Region.query.get(id_region)
        if not rgx:
            return jsonify({"msg": "El ID de Region no existe"}), 200
        else:
            Region.delete(rgx)
            return jsonify(rgx.serialize()),200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#---------------------------------------------------

#Modificar Región
@app.route('/region/<id_region>', methods=['PUT'])
#@app.jwt_required()
def updateRegion(id_region):
    try:
        rgx = Region.query.get(id_region)
        rgx.id_region = request.query.get('id_region')
        rgx.nombre = request.json.get('nombre')
        rgx.numero = request.json.get('numero')
        
        Region.save(rgx)
        return jsonify(rgx.serialize()),200
        
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500


#-----------------------------------------------------------
#Agregar Comuna
@app.route('/comuna', methods=['POST'])
#@app.jwt_required()
def addComunas():
    try:
        comu = Comuna()
       
        # asignar a variables lo que recibo mediante post
        comu.id_comuna = request.json.get('id_comuna')
        comu.nombre = request.json.get('nombre')   
        comu.provincia_id = request.json.get('provincia_id')
        Comuna.save(comu)
        return jsonify(comu.serialize()),200
        #else:
        #    return jsonify({"msg": "El usuario ya existe"}), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#-------------------------------------------------------------
#Consultar todas las comunas
@app.route('/comuna', methods=['GET'])
#@app.jwt_required()
def getComuna():
    try:
        
        comu = Comuna.query.all()
        #user = list(map(lambda x: x.serialize(), user))
        toreturn = [usi.serialize() for usi in comu]
        
        return jsonify(toreturn),200 # Es ok y codifica a tipo Json
    except Exception:
        exception ("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un ERROR"}), 500

#----------------------------------------------------------
# Borrar Comuna por ID
@app.route('/comuna/<id_comuna>', methods=['DELETE'])
#@app.jwt_required()
def deleteComuna(id_comuna):
    try:
        comu = Comuna.query.get(id_comuna)
        if not comu:
            return jsonify({"msg": "El ID de comuna no existe"}), 200
        else:
            Comuna.delete(comu)
            return jsonify(comu.serialize()),200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#-----------------------------------------------------------------------
#Modificar comuna
@app.route('/comuna/<id_comuna>', methods=['PUT'])
#@app.jwt_required()
def updateComuna(id_comuna):
    try:
        comu = Comuna.query.get(id_comuna)
        comu.id_region = request.query.get('id_comuna')
        comu.nombre = request.json.get('nombre')
        comu.provincia_id = request.json.get('provincia_id')
        
        Comuna.save(comu)
        return jsonify(comu.serialize()),200
        
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#--------------------------------------------------------------------
#Agregar Descuento
@app.route('/descuento', methods=['POST'])
#@app.jwt_required()
def addDescuento():
    try:
        desc = Descuento()
       
        # asignar a variables lo que recibo mediante post
        desc.id_descuento = request.json.get('id_descuento')
        desc.nombre = request.json.get('nombre')   
        desc.fecha = request.json.get('fecha')
        desc.porcentaje = request.json.get('porcentaje')
        desc.estado = request.json.get('estado')
        
        Descuento.save(desc)
        return jsonify(desc.serialize()),200
        #else:
        #    return jsonify({"msg": "El usuario ya existe"}), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#-------------------------------------------------------------
#Consultar todas los descuentos
@app.route('/descuento', methods=['GET'])
#@app.jwt_required()
def getDescuento():
    try:
        
        desc = Descuento.query.all()
        #user = list(map(lambda x: x.serialize(), user))
        toreturn = [usi.serialize() for usi in desc]
        
        return jsonify(toreturn),200 # Es ok y codifica a tipo Json
    except Exception:
        exception ("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un ERROR"}), 500

#-------------------------------------------------------------
# Borrar Descuento por ID
@app.route('/descuento/<id_descuento>', methods=['DELETE'])
#@app.jwt_required()
def deleteDescuento(id_descuento):
    try:
        desc = Descuento.query.get(id_descuento)
        if not desc:
            return jsonify({"msg": "El ID de comuna no existe"}), 200
        else:
            Descuento.delete(desc)
            return jsonify(desc.serialize()),200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#--------------------------------------------------------------
#Modificar Descuento
@app.route('/descuento/<id_descuento>', methods=['PUT'])
#@app.jwt_required()
def updateDescuento(id_descuento):
    try:
        desc = Descuento.query.get(id_descuento)       
        # asignar a variables lo que recibo mediante post
        desc.id_descuento = request.json.get('id_descuento')
        desc.nombre = request.json.get('nombre')   
        desc.fecha = request.json.get('fecha')
        desc.porcentaje = request.json.get('porcentaje')
        desc.estado = request.json.get('estado')
        
        Descuento.save(desc)
        return jsonify(desc.serialize()),200
        #else:
        #    return jsonify({"msg": "El usuario ya existe"}), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500
    
#----------------------------------------------------------
#Agregar Detalle de venta
@app.route('/detalle', methods=['POST'])
#@app.jwt_required()
def addDetalle():
    try:
        det = Detalle()
       
        # asignar a variables lo que recibo mediante post
        det.id_detalle = request.json.get('id_detalle')
        det.cantidad = request.json.get('cantidad')  
        det.valor = request.json.get('valor')
        det.descuento = request.json.get('descuento')
        det.estado = request.json.get('estado')
        det.venta_id = request.json.get('venta_id')
        det.producto_id = request.json.get('producto_id')
        
        Detalle.save(det)
        return jsonify(det.serialize()),200
        #else:
        #    return jsonify({"msg": "El usuario ya existe"}), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#----------------------------------------------------------------------
#Consultar detalle por ID
@app.route('/detalle/<id_detalle>', methods=['GET'])
#@app.jwt_required()
def getDetalle(id_detalle):
    try:
        det = Detalle.query.get(id_detalle)
                 
        if not det:
            return jsonify({"msg": "El ID del detalle no existe"}), 200
        else:
            return jsonify(det.serialize()),200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#---------------------------------------------------
# Borrar Detalle por ID
@app.route('/detalle/<id_detalle>', methods=['DELETE'])
#@app.jwt_required()
def deleteDetalle(id_detalle):
    try:
        det = Detalle.query.get(id_detalle)
        if not det:
            return jsonify({"msg": "El ID del detalle no existe"}), 200
        else:
            Detalle.delete(det)
            return jsonify(det.serialize()),200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#----------------------------------------------------
#Modificar Detalle
@app.route('/detalle/<id_detalle>', methods=['PUT'])
#@app.jwt_required()
def updateDetalle(id_detalle):
    try:
        det = Detalle.query.get(id_detalle)       
        # asignar a variables lo que recibo mediante post
        det.id_detalle = request.json.get('id_detalle')
        det.cantidad = request.json.get('cantidad')  
        det.valor = request.json.get('valor')
        det.descuento = request.json.get('descuento')
        det.estado = request.json.get('estado')
        det.venta_id = request.json.get('venta_id')
        det.producto_id = request.json.get('producto_id')   
        Detalle.save(det)
        return jsonify(det.serialize()),200
        #else:
        #    return jsonify({"msg": "El usuario ya existe"}), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#--------------------------------------------------------
#Agregar venta
@app.route('/venta', methods=['POST'])
#@app.jwt_required()
def addVenta():
    try:
        ven = Venta()
       
        # asignar a variables lo que recibo mediante post
        ven.id_venta = request.json.get('id_venta')
        ven.fecha = request.json.get('fecha')  
        ven.descuento = request.json.get('descuento')
        ven.sub_total = request.json.get('sub_total')
        ven.iva = request.json.get('iva')
        ven.total = request.json.get('total')
        ven.estado = request.json.get('estado')
        ven.vendedor_id = request.json.get('vendedor_id')
        ven.cliente_id = request.json.get('cliente_id')
        ven.despacho_id = request.json.get('despacho_id')
        
        Venta.save(ven)
        return jsonify(ven.serialize()),200
        #else:
        #    return jsonify({"msg": "El usuario ya existe"}), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#------------------------------------------------------------------
#Consultar Venta por ID
@app.route('/venta/<id_venta>', methods=['GET'])
#@app.jwt_required()
def getVenta(id_venta):
    try:
        ven = Venta.query.get(id_venta)
                 
        if not ven:
            return jsonify({"msg": "El ID del detalle no existe"}), 200
        else:
            return jsonify(ven.serialize()),200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#---------------------------------------------------------
# Borrar Venta por ID
@app.route('/venta/<id_venta>', methods=['DELETE'])
#@app.jwt_required()
def deleteVenta(id_venta):
    try:
        ven = Venta.query.get(id_venta)
        if not ven:
            return jsonify({"msg": "El ID de la venta no existe"}), 200
        else:
            Venta.delete(ven)
            return jsonify(ven.serialize()),200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#----------------------------------------------------------
#Modificar Venta
@app.route('/venta/<id_venta>', methods=['PUT'])
#@app.jwt_required()
def updateVenta(id_venta):
    try:
        ven = Venta.query.get(id_venta)       
        # asignar a variables lo que recibo mediante post
        ven.id_venta = request.json.get('id_venta')
        ven.fecha = request.json.get('fecha')  
        ven.descuento = request.json.get('descuento')
        ven.sub_total = request.json.get('sub_total')
        ven.iva = request.json.get('iva')
        ven.total = request.json.get('total')
        ven.estado = request.json.get('estado')
        ven.vendedor_id = request.json.get('vendedor_id')
        ven.cliente_id = request.json.get('cliente_id')
        ven.despacho_id = request.json.get('despacho_id')  
        Venta.save(ven)
        return jsonify(ven.serialize()),200
        #else:
        #    return jsonify({"msg": "El usuario ya existe"}), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#-------------------------------------------------------------------
#Agregar Despacho
@app.route('/despacho', methods=['POST'])
#@app.jwt_required()
def addDespacho():
    try:
        desp = Despacho()
       
        # asignar a variables lo que recibo mediante post
        desp.id_despacho = request.json.get('id_despacho')
        desp.direccion = request.json.get('direccion')
        desp.fecha_entrega = request.json.get('fecha_entrega')
        desp.hora_entrega = request.json.get('hora_entrega')
        desp.rut_recibe = request.json.get('rut_recibe')
        desp.nombre_recibe = request.json.get('nombre_recibe')
        desp.esto_despacho = request.json.get('esto_despacho')
        desp.venta_id = request.json.get('venta_id')
        desp.comuna_id = request.json.get('comuna_id')
        
        
        Despacho.save(desp)
        return jsonify(desp.serialize()),200
        #else:
        #    return jsonify({"msg": "El usuario ya existe"}), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500


#---------------------------------------------------------
#Consultar Despacho por ID
@app.route('/despacho/<id_despacho>', methods=['GET'])
#@app.jwt_required()
def getDespacho(id_despacho):
    try:
        desp = Despacho.query.get(id_despacho)
                 
        if not desp:
            return jsonify({"msg": "El ID del despacho no existe"}), 200
        else:
            return jsonify(desp.serialize()),200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#--------------------------------------------------------------
# Borrar Despacho por ID
@app.route('/despacho/<id_despacho>', methods=['DELETE'])
#@app.jwt_required()
def deleteDespacho(id_despacho):
    try:
        desp = Despacho.query.get(id_despacho)
        if not desp:
            return jsonify({"msg": "El ID del despacho no existe"}), 200
        else:
            Despacho.delete(desp)
            return jsonify(desp.serialize()),200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#------------------------------------------------------------
#Modificar Despacho
@app.route('/despacho/<id_despacho>', methods=['PUT'])
#@app.jwt_required()
def updateDespacho(id_despacho):
    try:
        desp = Despacho.query.get(id_despacho)       
        # asignar a variables lo que recibo mediante post
        desp.id_despacho = request.json.get('id_despacho')
        desp.direccion = request.json.get('direccion')
        desp.fecha_entrega = request.json.get('fecha_entrega')
        desp.hora_entrega = request.json.get('hora_entrega')
        desp.rut_recibe = request.json.get('rut_recibe')
        desp.nombre_recibe = request.json.get('nombre_recibe')
        desp.esto_despacho = request.json.get('esto_despacho')
        desp.venta_id = request.json.get('venta_id')
        desp.comuna_id = request.json.get('comuna_id') 
        Despacho.save(desp)
        return jsonify(desp.serialize()),200
        #else:
        #    return jsonify({"msg": "El usuario ya existe"}), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500


#Crear métodos Carrito.

# Ruta para agregar productos
@app.route('/producto_car', methods=['POST'])
#@app.jwt_required()
def addProducto_car():
    try:
        product_car = Producto_carrito()
       
        # asignar a variables lo que recibo mediante post
        product_car.id_producto = request.json.get('id_producto')
        product_car.codigo = request.json.get('codigo')   
        product_car.nombre = request.json.get('nombre')
        product_car.valor_venta = request.json.get('valor_venta')
        product_car.stock = request.json.get('stock')
        product_car.descripcion = request.json.get('descripcion')
        product_car.imagen = request.json.get('imagen')
        product_car.estado = request.json.get('estado')
        #if not user:
        Producto_carrito.save(product_car)
        return jsonify(product_car.serialize()),200
        #else:
        #    return jsonify({"msg": "El usuario ya existe"}), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

# Ruta para consultar todos los productos
@app.route('/producto_car', methods=['GET'])
#@app.jwt_required()
def getProductos_car():
    try:
        
        product_car = Producto_carrito.query.all()
        #user = list(map(lambda x: x.serialize(), user))
        toreturn = [usi.serialize() for usi in product_car]
        #return jsonify(user),200 # Es ok y codifica a tipo Json
        return jsonify(toreturn),200 # Es ok y codifica a tipo Json
    except Exception:
        exception ("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un ERROR"}), 500

# Borrar Producto
@app.route('/producto_car/<id_producto>', methods=['DELETE'])
#@app.jwt_required()
def deleteProducto_car(id_producto):
    try:
        product_car = Producto_carrito.query.get(id_producto)
        if not product_car:
            return jsonify({"msg": "El ID de producto no existe"}), 200
        else:
            Producto_carrito.delete(product_car)
            return jsonify(product_car.serialize()),200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#Modificar Producto
@app.route('/producto_car/<id_producto>', methods=['PUT'])
#@app.jwt_required()
def updateProducto_car(id_producto):
    try:
        product_car = Producto_carrito.query.get(id_producto)
        product_car.id_producto = request.json.get('id_producto')
        product_car.codigo = request.json.get('codigo')   
        product_car.nombre = request.json.get('nombre')
        product_car.valor_venta = request.json.get('valor_venta')
        product_car.stock = request.json.get('stock')
        product_car.descripcion = request.json.get('descripcion')
        product_car.imagen = request.json.get('imagen')
        product_car.estado = request.json.get('estado')
        
        Producto_carrito.save(product_car)
        return jsonify(product_car.serialize()),200
        
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

#Crear usuario-Boleta

# 7. Ruta para consultar todos los Usuarios
@app.route('/usuario_car', methods=['GET'])
#@app.jwt_required()
def getUsuarios_car():
    try:
        
        user = Usuario_car.query.all()
        #user = list(map(lambda x: x.serialize(), user))
        toreturn = [usi.serialize() for usi in user]
        #return jsonify(user),200 # Es ok y codifica a tipo Json
        return jsonify(toreturn),200 # Es ok y codifica a tipo Json
    except Exception:
        exception ("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un ERROR"}), 500

# 12. Ruta para agregar usuario_car
@app.route('/usuario_car', methods=['POST'])
#@app.jwt_required()
def addUsuario_car():
    try:
        user = Usuario_car()
       
        # asignar a variables lo que recibo mediante post
        user.id_car = request.json.get('id_car')
        user.correo = request.json.get('correo')
        user.password = request.json.get('password')
        user.estado = request.json.get('estado')    
        user.primer_nombre = request.json.get('primer_nombre')
        user.segundo_nombre = request.json.get('segundo_nombre')
        user.apellido_paterno = request.json.get('primer_apellido')
        user.apellido_materno = request.json.get('segundo_apellido')
        user.direccion = request.json.get('direccion')
        user.comuna_id = request.json.get('comuna')
        user.fono = request.json.get('fono')
        #if not user:
        Usuario_car.save(user)
        return jsonify(user.serialize()),200
        #else:
        #    return jsonify({"msg": "El usuario ya existe"}), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500
    
   

# 13. Creamos metodo para consultar un usuario en especifico por ID
@app.route('/usuario_car/<id_car>', methods=['GET'])
#@app.jwt_required()
def getUsuario_car(id_car):
    try:
        user = Usuario_car.query.get(id_car)
                 
        if not user:
            return jsonify({"msg": "El ID de usuario no existe"}), 200
        else:
            return jsonify(user.serialize()),200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500


# 14. Borrar usuario_car
@app.route('/usuario_car/<id_car>', methods=['DELETE'])
#@app.jwt_required()
def deleteUsuario_car(id_car):
    try:
        user = Usuario_car.query.get(id_car)
        if not user:
            return jsonify({"msg": "El ID de usuario no existe"}), 200
        else:
            Usuario_car.delete(user)
            return jsonify(user.serialize()),200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500
        
# 15. Modificar Usuario_car
@app.route('/usuario_car/<id_car>', methods=['PUT'])
#@app.jwt_required()
def updateUsuario_car(id_car):
    try:
        user = Usuario_car.query.get(id_car)
        user.correo = request.json.get('correo')
        user.password = request.json.get('password')
        user.estado = request.json.get('estado')    
        user.primer_nombre = request.json.get('primer_nombre')
        user.segundo_nombre = request.json.get('segundo_nombre')
        user.apellido_paterno = request.json.get('primer_apellido')
        user.apellido_materno = request.json.get('segundo_apellido')
        user.direccion = request.json.get('direccion')
        user.comuna_id = request.json.get('comuna')
        user.fono = request.json.get('fono')
        
        Usuario_car.save(user)
        return jsonify(user.serialize()),200
        
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un Error"}), 500

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# Agregar usuario al registro.
#-----------------------------------------------------------------------

#---------------------------------------------------------------
#Consultar todas las Comunas
@app.route('/comunas', methods=['GET'])
#@app.jwt_required()
def getComunas():
    try:
        
        comu = Comuna.query.all()
        #user = list(map(lambda x: x.serialize(), user))
        toreturn = [usi.serialize() for usi in comu]
        
        return jsonify(toreturn),200 # Es ok y codifica a tipo Json
    except Exception:
        exception ("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un ERROR"}), 500

# 8. comando para iniciar mi app flask: flask db init
# 9. comando para migrar mis modelos:   flask db migrate
# 10. comando para crear nuestros modelos como tablas : flask db upgrade
# 11. comando para iniciar la app flask: flask run

# 4. Configurar los puertos nuestra app 
if __name__ == '__main__':
    app.run(port=5000, debug=True)


