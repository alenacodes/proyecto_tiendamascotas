
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

#Creación de tabla usuario
class Usuario(db.Model):
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key=True)
    primer_nombre = db.Column(db.String(250), nullable= False)
    segundo_nombre = db.Column(db.String(250), nullable= True)
    apellido_paterno = db.Column(db.String(250), nullable= False)
    apellido_materno = db.Column(db.String(250), nullable= True)
    direccion = db.Column(db.String(250), nullable= False)

    def __str__(self):
        return "\nID: {}. Primer Nombre: {}. Segundo Nombre: {}. Apellido Paterno: {}. Apellido Materno: {}. Dirección: {}.\n".format(
            self.id,
            self.primer_nombre,
            self.segundo_nombre,
            self.apellido_paterno,
            self.apellido_materno,
            self.direccion
        )
    def serialize(self):
        return{
            "id": self.id,
            "primer_nombre": self.primer_nombre,
            "segundo_nombre": self.segundo_nombre,
            "apellido_paterno": self.apellido_paterno,
            "apellido_materno": self.apellido_materno,
            "direccion": self.direccion
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
    id_region = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(250), nullable= False)
    
    def __str__(self):
        return "\nID: {}. Nombre Región: {}. \n".format(
            self.id_region,
            self.nombre,
        )
    
    def serialize(self):
        return{
            "id": self.id_region,
            "Nombre": self.nombre,
            
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
    id_comuna = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(250), nullable= False)
    Region_id_region = db.Column(db.Integer, db.ForeignKey('Region.id_region'), nullable = False)
    
    
    def __str__(self):
        return "\nID Comuna: {}. Nombre Comuna: {}. ID Región: {}.\n".format(
            self.id_comuna,
            self.nombre,
            self.Region_id_region
        )
    
    def serialize(self):
        return{
            "id": self.id_comuna,
            "Nombre": self.nombre,
            "id_Region":self.Region_id_region
            
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
    __tablename__ = 'descuento'
    id_descuento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(250), nullable= False)
    fecha = db.Column(db.Date)
    porcentaje = db.Column(db.Float(3), nullable = False)
    estado = db.Column(db.Integer(), nullable= False)
    #Region_id_region = db.Column(db.Integer, db.ForeignKey('Region.id_region'), nullable = False)
    
    
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
    producto_id = db.Column(db.Integer, db.Foreignkey('producto.id_producto'), nullable = False)
    descuento_id = db.Column(db.Integer, db.Foreignkey('descuento.id_descuento'), nullable = False)
    fecha_inicio = db.Column(db.Date, nullable = False)
    fecha_termino = db.Column(db.Integer, nullable = False)
    #Region_id_region = db.Column(db.Integer, db.ForeignKey('Region.id_region'), nullable = False)
    
    
    def __str__(self):
        return "\nProducto_ID: {}. Descto ID: {}. Fecha Inicio: {}. Fecha Termino: {}. \n".format(
            self.producto_id,
            self.descuento_id,
            self.fecha_inicio,
            self.fecha_termino
           
        )
    
    def serialize(self):
        return{
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
    id_producto = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
            "estyado": self.estado
                      
                       
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()