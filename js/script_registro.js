const API_URL = 'http://127.0.0.1:5000/';
//Iniciar el formulario 
$(document).ready(function(){
    limpiarFormulario();
});

const arrayComunas = [
    {id:1, nombre:'Antartica'},
     {id:273, nombre:'Cerrillos'},
     {id:274, nombre:'Cerro Navia'},
     {id:275, nombre:'Conchalí'},
     {id:276, nombre:'El Bosque'},
     {id:277, nombre:'Estación Central'},
     {id:278, nombre: 'Huechuraba'},
     {id:279, nombre: 'Independencia'},
     {id:280, nombre: 'La Cisterna'},
     {id:281, nombre: 'La Florida'},
     {id:282, nombre: 'La Granja'},
     {id:283, nombre: 'La Pintana'},
     {id:284, nombre: 'La Reina'},
     {id:285, nombre: 'Las Condes'},
     {id:286, nombre: 'Lo Barnechea'},
     {id:287, nombre: 'Lo Espejo'},
     {id:288, nombre: 'Lo Prado'},
     {id:289, nombre: 'Macul'},
     {id:290, nombre: 'Maipú'},
     {id:304, nombre: 'Ñuñoa'},
     {id:291, nombre: 'Pedro Aguirre Cerda'},
     {id:292, nombre: 'Peñalolén'},
     {id:293, nombre: 'Providencia'},
     {id:294, nombre: 'Pudahuel'},
     {id:295, nombre: 'Quilicura'},
     {id:296, nombre: 'Quinta Normal'},
     {id:297, nombre: 'Recoleta'},
     {id:298, nombre: 'Renca'},
     {id:208, nombre:'San Bernardo'},
     {id:299, nombre: 'San Joaquín'},
     {id:129, nombre: 'San José de Maipo'},
     {id:300, nombre: 'San Miguel'},
     {id:228, nombre: 'San Pedro'},
     {id:301, nombre: 'San Ramón'},
     {id:302, nombre: 'Santiago'},
     {id:303, nombre: 'Vitacura'},
     {id:128, nombre: 'Puente Alto'},
     {id:127, nombre: 'Pirque'},
     {id:234, nombre: 'San José de La Costa'},
     {id:84, nombre: 'Lampa'}
     
     
     
];

//para cargar comunas.
function cargar_comunas(){
      
    arrayComunas.sort();
    arrayComunas.forEach(function(comuna){
      $('#comunas').append('<option value="'+comuna.id+'">'+comuna.nombre+'</option>');
    });
}

cargar_comunas();

//Cargar condicion    
$(document).on('click', '#condiciones', function(){ //Evento click en el link de las condiciones
    alert(' Gracias por estar de acuerdo con los términos y condiciones '
    +' Esperamos que disfrute de nuestros servicios');
});


//Registrar un nuevo usuario al hacer click en el boton  (Tabla Usuario Histórico)
$(document).on('click', '#btnRegistrarUsuario', function(){
    //obtener los datos del usuario
        
        var correo = $('#inputCorreo').val();
        var password = $('#inputPassword').val();
        var estado = 1;  //1 = activo, 0 = inactivo
        var nombre1 = $('#inputNombre1').val();
        var nombre2 = $('#inputNombre2').val();
        var apellido1 = $('#inputApellido1').val();
        var apellido2 = $('#inputApellido2').val();
        var direccion = $('#inputDireccion').val();
        var fono = $('#inputFono').val();
        var comuna = $('#comunas').val();
        
    if (correo == '' || password == '' || nombre1 == '' || apellido1 == '' || direccion == '' || fono == '' || comuna == ''){
        alert('Debe llenar todos los campos!');
          
    }
        else{
          alert('Gracias por registrarse!, será redirigido a la página de inicio de sesión');
        //cargar los datos mediante ajax
        $.ajax({
          url: API_URL+'usuarios', 
          type: 'POST',  
          contentType: 'application/json',
          data: JSON.stringify({
            
            correo: correo,
            password: password,
            estado: estado,
            primer_nombre: nombre1,
            segundo_nombre: nombre2,
            primer_apellido: apellido1,
            segundo_apellido: apellido2,
            direccion: direccion,
            fono: fono,
            comuna: comuna
                      
          }),
          success: function(respuesta) {
            console.log(respuesta);
           
           }
        })
    }
});

//Registrar un nuevo usuario al hacer click en el boton
$(document).on('click', '#btnRegistrarUsuario', function(){
    //obtener los datos del usuario
    
    var correo = $('#inputCorreo').val();
    var password = $('#inputPassword').val();
    var estado = 1;  //1 = activo, 0 = inactivo
    var nombre1 = $('#inputNombre1').val();
    var nombre2 = $('#inputNombre2').val();
    var apellido1 = $('#inputApellido1').val();
    var apellido2 = $('#inputApellido2').val();
    var direccion = $('#inputDireccion').val();
    var fono = $('#inputFono').val();
    var comuna = $('#comunas').val();
    if (correo == '' || password == '' || nombre1 == '' || apellido1 == '' || direccion == '' || fono == '' || comuna == ''){
      //alert('Debe llenar todos los campos correo, password, nombre, apellido, direccion, fono y comuna!');
      
    }
    else{
    //console.log(comuna)
      //alert('Gracias por registrarse!, será redirigido a la página de inicio de sesión');

    // para comprobar que se capturan los datos del form
    //console.log(correo, password, estado, nombre1, nombre2, apellido1, apellido2, direccion, fono, comuna);

    //cargar los datos mediante ajax
    $.ajax({
      url: API_URL+'usuario_car', 
      type: 'POST',  
      contentType: 'application/json',
      data: JSON.stringify({
        
        correo: correo,
        password: password,
        estado: estado,
        primer_nombre: nombre1,
        segundo_nombre: nombre2,
        primer_apellido: apellido1,
        segundo_apellido: apellido2,
        direccion: direccion,
        fono: fono,
        comuna: comuna
                  
      }),
      success: function(respuesta) {
        console.log(respuesta);
        //volver_inicio();
       }
    })
  }
});

// función para volver al inicio de sesión
function volver_inicio(){
  window.location.href = 'index.html';
}
//volver_inicio();

function limpiarFormulario(){
    $('#inputCorreo').val('');
    $('#inputPassword').val('');
    $('#inputNombre1').val('');
    $('#inputNombre2').val('');
    $('#inputApellido1').val('');
    $('#inputApellido2').val('');
    $('#inputDireccion').val('');
    $('#inputFono').val('');
    $('#comunas').val('');

    
    /*

    $('#btnAgregarUsuario').show();
    $('#btnEditarUsuarioTabla').hide();
    $('#btnCancelarEdicion').hide();
    */
}