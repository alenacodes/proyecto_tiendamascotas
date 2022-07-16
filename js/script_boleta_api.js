const API_URL = 'http://127.0.0.1:5000/';
        
$(document).ready(function(){
  $('#boleta tbody , #datos tbody , #total tbody').empty();
  actualizarTabla()
  actualizarTotal()
  actualizarCliente()
  
})

// Tabla productos
function actualizarTabla(){
    $('boleta tbody').empty();

    $.ajax({
      url: API_URL+'producto_car',
      type: 'GET',
      //dataType: 'json',
      contentype: 'application/json',
      success: function(respuesta){
      //console.log(respuesta);
        
        for (var i = 0; i < respuesta.length; i++){
           
           var fila = '<tr>' +
              '<th scope="col"><small>'  + (i+1) + '</small></th>' +
              '<td ><small>'+ respuesta[i].codigo + '</small></td>' +
              '<td><small>' + respuesta[i].nombre + '</small></td>' +
              '<td><small>' + respuesta[i].descripcion + '</small></td>' +
              '<td><small>' + respuesta[i].valor_venta + '</small></td>' +
              '<td><small>' + respuesta[i].stock + '</small></td>' +
              '</tr>';                 
            

           $('#boleta').append(fila);
        }
        
      }
    })

  }

    // Tabla totales
  document.querySelector('#total tbody').addEventListener('blur', actualizarTotal);
        function actualizarTotal(){
          const xhttp = new XMLHttpRequest();
          xhttp.open('GET', API_URL+'producto_car', true);
          xhttp.send();
          xhttp.onreadystatechange = function(){
            if (this.readyState == 4 && this.status == 200){
               let datos = JSON.parse(this.responseText);
               //console.log(datos);
			   let res = document.querySelector('#total tbody');
               res.innerHTML = '';
			   var largo = datos.length;
			   var total_neto = 0;
               var total_iva = 0;
               var total_a_pagar = 0;
			   var total_productos = 0;
			   total_productos = largo;
			   for (let i = 0; i < largo; i++){
					total_neto += datos[i].valor_venta * datos[i].stock;
					total_iva += total_neto * 0.19;
					total_a_pagar = total_neto + total_iva;
				}
				console.log(total_a_pagar);
				res.innerHTML += `
				<tr>
                    
                    <td scope="col">${total_productos}</td>
                    <td scope="col">$ ${total_neto}</td>
                    <td scope="col">$ ${total_iva}</td>
                    <td scope="col">$ ${total_a_pagar}</td>
                   
                  </tr>
				`;
			               
              
          }
        }
	}

// Función patra buscafr la comuna y mostrarla, pero no resulta :/
document.querySelector('#datos tbody').addEventListener('blur', buscarComuna);
function buscarComuna(comu){
    const xhttp = new XMLHttpRequest();
    xhttp.open('GET', API_URL+'comuna/'+comu, true);
    xhttp.responseType = 'text';
    xhttp.send();
    xhttp.onreadystatechange = function() {
          
    if (this.readyState == 4 && this.status == 200) {
        let comuna = JSON.parse(this.responseText);
        console.log(comuna);
        //comuna = JSON.stringify(comuna);
              
        return `${comuna['Nombre']}`;
           
            
                      
                          
        }
      
    }  
                  
}


// Función para buscar el cliente y mostrarlo

document.querySelector('#datos tbody').addEventListener('blur', actualizarCliente);
function actualizarCliente(){
   //$('datos tbody').empty();
   const xhttp = new XMLHttpRequest();
   xhttp.open('GET', API_URL+'usuario_car', true);
   xhttp.send();
   xhttp.onreadystatechange = function(){

    //console.log(respuesta);
    if (this.readyState == 4 && this.status == 200){
     //console.log(this.responseText);
        let datos = JSON.parse(this.responseText);
         //console.log(datos);
         let res = document.querySelector('#datos tbody');
         res.innerHTML = '';
         for (let item of datos){
           res.innerHTML += `
           <tr>
             <td scope="col"><small>${item.primer_nombre}</small></td>
             <td scope="col"><small>${item.apellido_paterno}</small></td>
             <td scope="col"><small>${item.apellido_materno}</small></td>
             <td scope="col"><small>${item.direccion}</small></td>
             <td scope="col"><small>${item.comuna}</small></td>
             <td scope="col"><small>${item.correo}</small></td>
                                 
           </tr>`
         }
       }
       
       
    }
   }