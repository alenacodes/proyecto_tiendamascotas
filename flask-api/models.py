
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, String, Column
from sqlalchemy.orm import relationship
db = SQLAlchemy()

# Tabla Usuario/Cliente
#Creación de tabla usuario
class Usuario(db.Model):
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(250), nullable= False)
    password = db.Column(db.String(250), nullable= True)
    estado = db.Column(db.Integer, nullable= False)
    primer_nombre = db.Column(db.String(250), nullable= False)
    segundo_nombre = db.Column(db.String(250))
    apellido_paterno = db.Column(db.String(250), nullable= False)
    apellido_materno = db.Column(db.String(250))
    direccion = db.Column(db.String(250), nullable= False)
    comuna_id = db.Column(db.Integer, db.ForeignKey('Comuna.id_comuna'))
    fono = db.Column(db.Integer, nullable= False)

    def __str__(self):
        return "\nID: {}. Correo {}. Password {}. Estado {}. Primer Nombre: {}. Segundo Nombre: {}. Apellido Paterno: {}. Apellido Materno: {}. Dirección: {}. comuna id: {}. Fono: {}\n".format(
            self.id,
            self.correo,
            self.password,
            self.estado,
            self.primer_nombre,
            self.segundo_nombre,
            self.apellido_paterno,
            self.apellido_materno,
            self.direccion,
            self.comuna_id,
            self.fono
        )
    def serialize(self):
        return{
            "id": self.id,
            "correo":self.correo,
            "password":self.password,
            "estado":self.estado,
            "primer_nombre": self.primer_nombre,
            "segundo_nombre": self.segundo_nombre,
            "apellido_paterno": self.apellido_paterno,
            "apellido_materno": self.apellido_materno,
            "direccion": self.direccion,
            "comuna": self.comuna_id,
            "fono": self.fono
        }
    
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

#Creación de tabla usuario-Carrito
class Usuario_car(db.Model):
    __tablename__ = 'Usuario_car'
    id_car = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(250), nullable= False)
    password = db.Column(db.String(250), nullable= True)
    estado = db.Column(db.Integer, nullable= False)
    primer_nombre = db.Column(db.String(250), nullable= False)
    segundo_nombre = db.Column(db.String(250))
    apellido_paterno = db.Column(db.String(250), nullable= False)
    apellido_materno = db.Column(db.String(250))
    direccion = db.Column(db.String(250), nullable= False)
    comuna_id = db.Column(db.Integer, nullable=False)
    fono = db.Column(db.Integer, nullable= False)

    def __str__(self):
        return "\nid: {}. correo {}. password {}. estado {}. primer Nombre: {}. segundo Nombre: {}. apellido_paterno: {}. apellido_materno: {}. direccion: {}. comuna_id: {}. fono: {}\n".format(
            self.id_car,
            self.correo,
            self.password,
            self.estado,
            self.primer_nombre,
            self.segundo_nombre,
            self.apellido_paterno,
            self.apellido_materno,
            self.direccion,
            self.comuna_id,
            self.fono
        )
    def serialize(self):
        return{
            "id": self.id_car,
            "correo":self.correo,
            "password":self.password,
            "estado":self.estado,
            "primer_nombre": self.primer_nombre,
            "segundo_nombre": self.segundo_nombre,
            "apellido_paterno": self.apellido_paterno,
            "apellido_materno": self.apellido_materno,
            "direccion": self.direccion,
            "comuna": self.comuna_id,
            "fono": self.fono
        }
    
       
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

#creación de tabla Region
class Region (db.Model):
    __tablename__ = 'Region'
    id_region = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre = db.Column(db.String(250), nullable= False)
    numero = db.Column(db.String(10), nullable=False)
    def __str__(self):
        return "\nid_region: {}. nombre Region: {}. numero: {}.\n".format(
            self.id_region,
            self.nombre,
            self.numero
        )
    
    def serialize(self):
        return{
            "id_region": self.id_region,
            "nombre": self.nombre,
            "numero": self.numero
            }
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

#Creación de tabla comuna
class Comuna (db.Model):
    __tablename__ = 'Comuna'
    id_comuna = db.Column(db.Integer, primary_key=True, nullable = False)
    nombre = db.Column(db.String(250), nullable= False)
    provincia_id = db.Column(db.Integer, db.ForeignKey('Provincias.id_prov'), nullable = False)
    provincia = db.relationship('Provincias', backref=db.backref('comuna', lazy='dynamic'))
    
    def __str__(self):
        return "\nID Comuna: {}. Nombre Comuna: {}. ID Provincia: {}.\n".format(
            self.id_comuna,
            self.nombre,
            self.provincia_id
        )
    
    def serialize(self):
        return{
            "id": self.id_comuna,
            "Nombre": self.nombre,
            "id_provincia":self.provincia_id
            
        }
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


#Creación tabla provincias
class Provincias (db.Model):
    __tablename__ = 'Provincias'
    id_prov = db.Column(db.Integer, primary_key=True, nullable = False)
    nombre = db.Column(db.String(250), nullable= False)
    region_id = db.Column(db.Integer, db.ForeignKey('Region.id_region'), nullable = False)
    region = db.relationship('Region', backref=db.backref('provincias', lazy=True))
    
    def __str__(self):
        return "\nID Provincia: {}. Nombre: {}. ID Región: {}.\n".format(
            self.id_prov,
            self.nombre,
            self.region_id
        )
    
    def serialize(self):
        return{
            "id": self.id_prov,
            "Nombre": self.nombre,
            "id_Region":self.region_id
            
        }
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


#Creación tabla Descuento

class Descuento (db.Model):
    __tablename__ = 'Descuento'
    id_descuento = db.Column(db.Integer, primary_key=True, nullable = False)
    nombre = db.Column(db.String(250), nullable= False)
    fecha = db.Column(db.Date)
    porcentaje = db.Column(db.Integer, nullable = False)
    estado = db.Column(db.Integer, nullable= False)
    
    
    
    def __str__(self):
        return "\nID Descuento: {}. Nombre: {}. Fecha: {}. Porcentaje: {}. Estado: {}. \n".format(
            self.id_descuento,
            self.nombre,
            self.fecha,
            self.porcentaje,
            self.estado
        )
    
    def serialize(self):
        return{
            "id": self.id_descuento,
            "Nombre": self.nombre,
            "Fecha": self.fecha,
            "Porcentaje": self.porcentaje,
            "Estado": self.estado
            
        }
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

#Creación tabla Descuento_Producto

class Descuento_producto (db.Model):
    __tablename__ = 'descuento_producto'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id_producto'), nullable = False)
    descuento_id = db.Column(db.Integer, db.ForeignKey('Descuento.id_descuento'), nullable = False)
    fecha_inicio = db.Column(db.Date)
    fecha_termino = db.Column(db.Integer)
    producto_desc_prod= db.relationship('Producto', backref=db.backref('descuento_producto', lazy=True)) 
    desc_prod_descuento= db.relationship('Descuento', backref=db.backref('descuento_producto', lazy=True))  
    
   

    
    def __str__(self):
        return "\nid: {}. Producto_ID: {}. Descto ID: {}. Fecha Inicio: {}. Fecha Termino: {}. \n".format(
            self.id,
            self.producto_id,
            self.descuento_id,
            self.fecha_inicio,
            self.fecha_termino
           
        )
    
    def serialize(self):
        return{
            "id": self.id,
            "Producto_id": self.producto_id,
            "Descuento_id": self.descuento_id,
            "Fecha_inicio": self.fecha_inicio,
            "Fecha_termino": self.fecha_termino
            
            
        }
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    

#Creación tabla Producto
class Producto (db.Model):
    __tablename__ = 'producto'
    id_producto = db.Column(db.Integer, primary_key=True, nullable = False)
    codigo = db.Column(db.String(250), nullable = False ) #SKU
    nombre = db.Column(db.String(250), nullable = False )
    valor_venta = db.Column(db.Integer, nullable = False )
    stock = db.Column(db.Integer)
    descripcion = db.Column(db.String(250))
    imagen = db.Column(db.String(250))
    estado = db.Column(db.String(1), nullable = False)
    
    
        
    def __str__(self):
        return "\nID_Producto: {}. Codigo: {}. Nombre: {}. Valor venta: {}. Stock: {}. Descripcion: {}. Imagen: {}. Estado: {}. \n".format(
            self.id_producto,
            self.codigo,
            self.nombre,
            self.valor_venta,
            self.stock,
            self.descripcion,
            self.imagen,
            self.estado,
            
                       
        )
    
    def serialize(self):
        return{
            "id_producto": self.id_producto,
            "codigo": self.codigo,
            "nombre": self.nombre,
            "valor_venta": self.valor_venta,
            "stock":self.stock,
            "descripcion":self.descripcion,
            "imagen": self.imagen,
            "estado": self.estado
                      
                       
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

#Creación tabla producto-Carrito

#Creación tabla Producto
class Producto_carrito (db.Model):
    __tablename__ = 'producto_carrito'
    id_producto = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(250), nullable = False )
    nombre = db.Column(db.String(250), nullable = False )
    valor_venta = db.Column(db.Integer, nullable = False )
    stock = db.Column(db.Integer)
    descripcion = db.Column(db.String(250))
    imagen = db.Column(db.String(250))
    estado = db.Column(db.String(1), nullable = False)
    
    
        
    def __str__(self):
        return "\nID_Producto: {}. Codigo: {}. Nombre: {}. Valor venta: {}. Stock: {}. Descripcion: {}. Imagen: {}. Estado: {}. \n".format(
            self.id_producto,
            self.codigo,
            self.nombre,
            self.valor_venta,
            self.stock,
            self.descripcion,
            self.imagen,
            self.estado,
            
                       
        )
    
    def serialize(self):
        return{
            "id_producto": self.id_producto,
            "codigo": self.codigo,
            "nombre": self.nombre,
            "valor_venta": self.valor_venta,
            "stock":self.stock,
            "descripcion":self.descripcion,
            "imagen": self.imagen,
            "estado": self.estado
                      
                       
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


#Creación tabla Suscripción
class Suscripcion (db.Model):
    __tablename__ = 'suscripcion'
    id_suscripcion = db.Column(db.Integer, primary_key=True)
    fecha_inicio = db.Column(db.Date, nullable = False )
    fecha_termino = db.Column(db.Date)
    cliente_id = db.Column(db.Integer, db.ForeignKey('Usuario.id'), nullable = False)
    suscripcion_cliente= db.relationship('Usuario', backref=db.backref('suscripcion_cliente', lazy=True))
       
        
    def __str__(self):
        return "\nID_Suscripcion: {}. Fecha_inicio: {}. Fecha_termino: {}. Cliente_id: {}.\n".format(
            self.id_suscripcion,
            self.fecha_inicio,
            self.fecha_termino,
            self.cliente_id
                                  
        )
    
    def serialize(self):
        return{
            "id_suscripcion": self.id_suscripcion,
            "fecha_inicio": self.fecha_inicio,
            "fecha_termino": self.fecha_termino,
            "cliente_id": self.cliente_id
                                  
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


#Creación tabla Donacion
class Donacion (db.Model):
    __tablename__ = 'donacion'
    id_donacion = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Integer, nullable = False)
    fecha = db.Column(db.Date, nullable = False )
    cliente_id = db.Column(db.Integer, db.ForeignKey('Usuario.id'), nullable = False)
    #donacion_cliente= db.relationship('Usuario', backref='donacion_cliente', lazy='dynamic')
        
    def __str__(self):
        return "\nID_Suscripcion: {}. Valor: {}. Fecha: {}. Cliente_id: {}.\n".format(
            self.id_donacion,
            self.valor,
            self.fecha,
            self.cliente_id
                                  
        )
    
    def serialize(self):
        return{
            "id_donacion": self.id_donacion,
            "valor": self.valor,
            "fecha": self.fecha,
            "cliente_id": self.cliente_id
                                  
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


#Creación tabla Detalle
class Detalle (db.Model):
    __tablename__ = 'detalle'
    id_detalle = db.Column(db.Integer, primary_key=True, nullable=False)
    cantidad = db.Column(db.Integer, nullable = False)
    valor = db.Column(db.Integer, nullable = False)
    descuento = db.Column(db.Integer, nullable = False)
    estado = db.Column(db.String(1), nullable = False)
    venta_id = db.Column(db.Integer, db.ForeignKey('venta.id_venta'), nullable = False)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id_producto'), nullable = False)
    venta_detalle= db.relationship('Venta', backref='detalle', lazy=True)
    producto_detalle= db.relationship('Producto', backref='detalle', lazy=True)
        
    def __str__(self):
        return "\nID_detalle: {}. cantidad: {}. Valor: {}. descuento: {}. estado: {}. venta_id: {}. producto_id: {}.\n".format(
            self.id_detalle,
            self.cantidad,
            self.valor,
            self.descuento,
            self.estado,
            self.venta_id,
            self.producto_id
                                  
        )
    
    def serialize(self):
        return{
            "id_detalle": self.id_detalle,
            "cantidad": self.cantidad,
            "valor": self.valor,
            "descuento": self.descuento,
            "estado": self.estado,
            "venta_id": self.venta_id,
            "producto_id":self.producto_id
                                  
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
 #Crear Tabla Vendedor
 
class Vendedor (db.Model):
    __tablename__ = 'vendedor'
    id_vendedor = db.Column(db.Integer, primary_key=True, nullable=False)
    rut = db.Column(db.String(9), nullable = False, unique = True)
    dv = db.Column(db.String(1), nullable = False)
    primer_nombre = db.Column(db.String(250), nullable = False)
    segundo_nombre = db.Column(db.String(250))
    apellido_paterno = db.Column(db.String(250), nullable = False)
    apellido_materno = db.Column(db.String(250))
    direccion = db.Column(db.String(250), nullable = False)
    fono = db.Column(db.Integer, nullable = False)
    correo = db.Column(db.String(250), nullable = False)
    estado = db.Column(db.String(1), nullable = False)
    comuna_id = db.Column(db.Integer, db.ForeignKey('Comuna.id_comuna'), nullable = False)
    comuna_vendedor= db.relationship('Comuna', backref=db.backref('vendedor', lazy='dynamic'))
           
    def __str__(self):
        return "\nID_vendedor: {}. rut: {}. dv: {}. primer_nombre: {}. segundo_nombre: {}. apellido_paterno: {}. apellido_materno: {}. direccion: {}. fono {}. correo: {}. estado: {}. comuna_id: {}.\n".format(
            self.id_vendedor,
            self.rut,
            self.dv,
            self.primer_nombre,
            self.segundo_nombre,
            self.apellido_paterno,
            self.apellido_materno,
            self.direccion,
            self.fono,
            self.correo,
            self.estado,
            self.comuna_id
                                  
        )
    
    def serialize(self):
        return{
            "id_vendedor": self.id_vendedor,
            "rut": self.rut,
            "dv": self.dv,
            "primer_nombre": self.primer_nombre,
            "segundo_nombre": self.segundo_nombre,
            "apellido_paterno": self.apellido_paterno,
            "apellido_materno": self.apellido_materno,
            "direccion": self.direccion,
            "fono": self.fono,
            "correo":self.correo,
            "estado": self.estado,
            "comuna_id":self.comuna_id
                                  
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


#Creación tabla Venta
class Venta (db.Model):
    __tablename__ = 'venta'
    id_venta = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    fecha = db.Column(db.Date, nullable = False)
    descuento = db.Column(db.Integer)
    sub_total = db.Column(db.Integer, nullable = False)
    iva = db.Column(db.Integer, nullable = False)
    total = db.Column(db.Integer, nullable = False)
    estado = db.Column(db.String(1), nullable = False)
    vendedor_id = db.Column(db.Integer, db.ForeignKey('vendedor.id_vendedor'), nullable=False) #Id Vendedor que debería ser foránea
    cliente_id = db.Column(db.Integer, db.ForeignKey('Usuario.id'), nullable = False)
    despacho_id = db.Column(db.Integer, db.ForeignKey('despacho.id_despacho'), nullable = False)
    #vendedor_venta= db.relationship('Vendedor', backref=db.backref('venta', lazy='dynamic'))
    #cliente_venta= db.relationship('Usuario', backref=db.backref('venta', lazy='dynamic'))
    #despacho_venta= db.relationship('Despacho', backref=db.backref('venta', lazy='dynamic'))
        
    def __str__(self):
        return "\nID_venta: {}. fecha: {}. descuento: {}. sub_total: {}. iva: {}. total: {}. estado: {}. cliente_id: {}. vendedor_id: {}.  despacho_id: {}.\n".format(
            self.id_venta,
            self.fecha,
            self.descuento,
            self.sub_total,
            self.iva,
            self.total,
            self.estado,
            self.cliente_id,
            self.vendedor_id,
            self.despacho_id
                                  
        )
    
    def serialize(self):
        return{
            "id_venta": self.id_venta,
            "fecha": self.fecha,
            "descuento": self.descuento,
            "sub_total": self.sub_total,
            "iva": self.iva,
            "total": self.total,
            "estado": self.estado,
            "cliente_id": self.cliente_id,
            "vendedor_id": self.vendedor_id,
            "despacho_id":self.despacho_id
                                  
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
 

#Crear Tabla Despacho
 
class Despacho (db.Model):
    __tablename__ = 'despacho'
    id_despacho = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    direccion = db.Column(db.String(250), nullable = False)
    fecha_entrega = db.Column(db.Date)
    hora_entrega = db.Column(db.Date)
    rut_recibe = db.Column(db.String(10), unique = True)
    nombre_recibe = db.Column(db.String(250))
    esto_despacho = db.Column(db.Integer, nullable = False)
    venta_id = db.Column(db.Integer, db.ForeignKey('venta.id_venta'), nullable = False)
    comuna_id = db.Column(db.Integer, db.ForeignKey('Comuna.id_comuna'), nullable = False)
    #venta = db.relationship('Venta', backref='despacho', lazy='dynamic')
    #comuna = db.relationship('Comuna', backref='despacho', lazy=True)
    
           
    def __str__(self):
        return "\nID_vendedor: {}. rut: {}. dv: {}. primer_nombre: {}. segundo_nombre: {}. apellido_paterno: {}. apellido_materno: {}. direccion: {}. fono {}. correo: {}. estado: {}. comuna_id: {}.\n".format(
            self.id_despacho,
            self.direccion,
            self.fecha_entrega,
            self.hora_entrega,
            self.rut_recibe,
            self.nombre_recibe,
            self.esto_despacho,
            self.venta_id,
            self.comuna_id
                                              
        )
    
    def serialize(self):
        return{
            "id_despacho": self.id_despacho,
            "direccion": self.direccion,
            "fecha_entrega": self.fecha_entrega,
            "hora_entrega": self.hora_entrega,
            "rut_recibe": self.rut_recibe,
            "nombre_recibe": self.nombre_recibe,
            "esto_despacho": self.esto_despacho,
            "venta_id": self.venta_id,
            "comuna_id": self.comuna_id
                                              
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


