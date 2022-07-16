const Clickbutton = document.querySelectorAll('.button')
const tbody = document.querySelector('.tbody')
let carrito = []


Clickbutton.forEach(btn => {
  btn.addEventListener('click', addToCarritoItem)
})


function addToCarritoItem(e){
  const button = e.target
  const item = button.closest('.card')
  const itemTitle = item.querySelector('.card-title').textContent;
  const itemPrice = item.querySelector('.precio').textContent;
  const itemImg = item.querySelector('.card-img-top').src;
  const itemCodigo = item.querySelector('.card-codigo').textContent;
  const itemId = item.querySelector('.card-id').textContent;
  const desCrip = item.querySelector('.card-text').textContent;
  //const estaDo = item.querySelector('.card-estado').textContent;
  const estaDo = "A";
  
  const newItem = {
    title: itemTitle,
    precio: itemPrice,
    img: itemImg,
    sku: itemCodigo,
    id: itemId,
    descripcion: desCrip,
    estado: estaDo,
    cantidad: 1
  }

  addItemCarrito(newItem)
}


function addItemCarrito(newItem){

  const alert = document.querySelector('.alert')

  setTimeout( function(){
    alert.classList.add('hide')
  }, 2000)
    alert.classList.remove('hide')

  const InputElemnto = tbody.getElementsByClassName('input__elemento')
  for(let i =0; i < carrito.length ; i++){
    if(carrito[i].title.trim() === newItem.title.trim()){
      carrito[i].cantidad ++;
      const inputValue = InputElemnto[i]
      inputValue.value++;
      CarritoTotal()+"000"
      return null;
    }
  }
  
  carrito.push(newItem)
  
  renderCarrito()
} 


function renderCarrito(){
  tbody.innerHTML = ''
  carrito.map(item => {
    const tr = document.createElement('tr')
    tr.classList.add('ItemCarrito')
    const Content = `
    
    <th scope="row">1</th>
            <td class="table__productos">
              <img src=${item.img}  alt="" id="imgItemProducto"> 
              <h6 class="title" id="nombreItemProducto">${item.title}</h6>
              <h6 class="skuItem" id="codigoItemProducto" hidden>Codigo: ${item.sku}</h6>
              <h6 class="itemID" id="idProducto" hidden>ID: ${item.id}</h6>
              <h6 class="itemEstado" id="estadoProducto" hidden>Estado: ${item.estado}</h6>            
            </td>
            <td><h6 class="itemDescripcion" id="descripcionProducto" hidden>${item.descripcion}</h6></td>

            <td class="table__price" id="precioItemProducto"><p>${item.precio}</p></td>
            <td class="table__cantidad">
              <input type="number" min="1" value=${item.cantidad} class="input__elemento" id="CantidadItemProducto">
              <button class="delete btn btn-danger">x</button>
            </td>
    
    `
    tr.innerHTML = Content;
    tbody.append(tr)

    tr.querySelector(".delete").addEventListener('click', removeItemCarrito)
    tr.querySelector(".input__elemento").addEventListener('change', sumaCantidad)
  })
  CarritoTotal()
  
}

function CarritoTotal(){
  let Total = 0;
  const itemCartTotal = document.querySelector('.itemCartTotal')
  carrito.forEach((item) => {
    const precio = Number(item.precio.replace("$", ''))
    Total = Total + precio*item.cantidad
  })

  itemCartTotal.innerHTML = `Total $${Total}`
  addLocalStorage()
}

function removeItemCarrito(e){
  const buttonDelete = e.target
  const tr = buttonDelete.closest(".ItemCarrito")
  const title = tr.querySelector('.title').textContent;
  for(let i=0; i<carrito.length ; i++){

    if(carrito[i].title.trim() === title.trim()){
      carrito.splice(i, 1)
    }
  }

  const alert = document.querySelector('.remove')

  setTimeout( function(){
    alert.classList.add('remove')
  }, 2000)
    alert.classList.remove('remove')

  tr.remove()
  CarritoTotal()
}

function sumaCantidad(e){
  const sumaInput  = e.target
  const tr = sumaInput.closest(".ItemCarrito")
  const title = tr.querySelector('.title').textContent;
  carrito.forEach(item => {
    if(item.title.trim() === title){
      sumaInput.value < 1 ?  (sumaInput.value = 1) : sumaInput.value;
      item.cantidad = sumaInput.value;
      CarritoTotal()
      
    }
  })
}

function addLocalStorage(){
  localStorage.setItem('carrito', JSON.stringify(carrito))
  console.log(carrito);
}

window.onload = function(){
  const storage = JSON.parse(localStorage.getItem('carrito'));
  if(storage){
    carrito = storage;
    renderCarrito()
    //enviarProductoCarrito()
  }
}

//login

let loginForm = document.querySelector('.header .login-form');

document.querySelector('#login-btn').onclick = () =>{
//  document.querySelector('#login-btn').onload = () =>{
    loginForm.classList.toggle('active');
    navbar.classList.remove('active');
}

let navbar = document.querySelector('.header .navbar');

document.querySelector('#menu-btn').onclick = () =>{
//  document.querySelector('#menu-btn').onload = () =>{
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

//document.querySelector('.ItemCarrito').addEventListener('change', enviarProductoCarrito);
// Función para enviar los productos a la tabla carrito de compras.
function enviarProductoCarrito(){
  //let Total = 0;
  let cantidad = 0;
  let monto = 0;
  let titulo = '';
  let foto = '';
  let codigo = '';
  let ID = 0;
  let est = '';
  let desc = '';
  //let precio = 0;
  
      carrito.forEach((item) => {
        const API_URL = 'http://127.0.0.1:5000';
        cantidad = Number(item.cantidad)
        monto = Number(item.precio)
        ID = Number(item.id)
        est = item.estado
        desc = String(item.descripcion)
        foto = item.img
        titulo = item.title
        codigo = item.sku
       
        //})
        //Total = Total + precio*item.cantidad
        //console.log(cantidad, monto, titulo, foto, codigo, ID, est, desc);
        $.ajax({
          url: API_URL+'/producto_car',
          type: 'POST',
          //contentype: 'application/json',
          datatype: 'json',
          data: {
            id_producto: ID,
            codigo: codigo,
            nombre: titulo,
            valor_venta: monto,
            stock: cantidad,
            descripcion: desc,
            imagen: foto,
            estado: est
            
          },
          success: function(response){
            console.log(response);
          }
        })
      })
      }


    
  
  

  


  
  


