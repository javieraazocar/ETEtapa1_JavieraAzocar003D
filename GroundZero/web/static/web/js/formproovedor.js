$(function(){
    $("#formproovedor").validate({
        rules :{
            id: "required",
            nombre : {
                required: true,
                nombre: true
            },
            password:"required",
            email: "required"
        },//rules

        mesagges: {
            id: {
                required: "No puedes dejar este campo en blanco",
                minlenght:'Caracteres insuficientes'
            },
            nombre: {
                required:"No puedes dejar este campo en blanco",
                minlenght: 'Caracteres insuficientes'
            },
            email:{
                required:'Ingresa tu correo electrónico',
                email: 'Formato de correo no válido'
            },
            password:{
                required: 'Ingresa una contraseña',
                minlength: 'Caracteres insuficientes'
            },
            fono:{
                required:'Ingrese número de celular',
                minlenght: 'Cantidad de digitos insuficietes'
            },
            direccion:{
                required:'Ingrese una dirección',
                minlenght: 'Cantidad de caracteres insuficientes'
            },
            moneda:{
                required:'Ingrese la moneda de pago',
                minlenght:'Caracteres insuficientes'
            },
            pais:{
                required:'Ingrese el País',
                minlenght:'Caracteres insuficientes'
            }
        }
    });
});

function CambiarMayusculas()
      {
         String.prototype.initCap = function () {
            return this.toLowerCase().replace(/(?:^|\s)[a-z]/g, function (m) {
               return m.toUpperCase();
            });
         };

         a = document.getElementById("nombre");
         a.value = a.value.initCap();
         console.log('funciono!');
      }