var alertPlaceholder = document.getElementById('liveAlertPlaceholder');
var alertTrigger = document.getElementById('btnConectar');

function alert(message, type) {
    document.getElementById("alert").innerHTML = '<div class="alert alert-' + type + ' alert-dismissible" role="alert">' + message + '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'
}

$(document).ready(function () {
    $("#btnConectar").click(function () {
        var email = $("#Email").val();
        if (email.includes("@gmail") || email.includes("@hotmail") || email.includes("@outlook")) {
            var contraseña = $("#Password").val();
            if(contraseña.length > 8){
                alertTrigger.addEventListener('click', function () {
                    alert('Has ingresado correctamente los valores de tu cuenta!', 'success');
                })    
            }else {
                if (alertTrigger) {
                    alertTrigger.addEventListener('click', function () {
                        alert('Campo Contraseña no puede estar vacio', 'danger');
                    })
                }
            }
        }else {
            if (alertTrigger) {
                alertTrigger.addEventListener('click', function () {
                    alert('Formato de Correo Incorrecto', 'danger');
                })
            }
        }  
    });
});