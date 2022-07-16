const API_URL = 'http://127.0.0.1:5000/';

let loginForm = document.querySelector('.header .login-form');

document.querySelector('#login-btn').onclick = () =>{
    loginForm.classList.toggle('active');
    navbar.classList.remove('active');
}

let navbar = document.querySelector('.header .navbar');

document.querySelector('#menu-btn').onclick = () =>{
    navbar.classList.toggle('active');    
    loginForm.classList.remove('active');
}

window.onscroll = () =>{
    loginForm.classList.remove('active');
    navbar.classList.remove('active');

    if(window.scrollY > 0){
        document.querySelector('.header').classList.add('active');
    }else{
        document.querySelector('.header').classList.remove('active');
    }
}

window.onload = () =>{
    if(window.scrollY > 0){
        document.querySelector('.header').classList.add('active');
    }else{
        document.querySelector('.header').classList.remove('active');
    }
}

function contacto(){
      
    alert('¡Mensaje enviado!, estimado/a  pronto nos comunicaremos con usted');
      
  }

//var btnRegistro = document.getElementById('botonRegistro');
//para validar usuario
function validarUsuario(){
    
    let usuario = document.getElementById('correoUsuario').value;
    let clave = document.getElementById('contraseña').value;
    let xhttp = new XMLHttpRequest();
    xhttp.open('GET', API_URL+'usuario_car', true);
    xhttp.send();
    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            let respuesta = JSON.parse(this.responseText);
            var tipoUsuario = '';
            //console.log(respuesta);
            if (respuesta.length > 0){
                for(i of respuesta){
                    if (i.correo == usuario && i.password == clave){
                        alert('Bienvenido/a '+i.primer_nombre);
                        localStorage.setItem('usuario', i.primer_nombre);
                        tipoUsuario = '<h2 class="badge-info" id="usuario">¡ Hola '+i.primer_nombre+' !</h2>';
                        document.getElementById('usuario').innerHTML = tipoUsuario;
                        
                                                           
                        //volver_inicio();
                        //window.location.href = 'carrito.html';
                        break;
                    }
                    else{
                        alert('Usuario o contraseña incorrectos');
                    }
                }
           
            }
        }    
    }
}

function volver_inicio(){
    window.location.href = 'index.html';
}

window.onload = function(){
    const usuarionombre = localStorage.getItem('usuario');
    if(localStorage.getItem('usuario') != null){

        document.getElementById('usuario').innerHTML = '<h2 class="badge-info" id="usuario">¡ Hola '+usuarionombre+' !</h2>';
    }
}