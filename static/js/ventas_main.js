$(document).on('click', '#guardar', function () {
    var cliente = $('#clientes').val();
    var producto = $('#productos').val();
    var total = $('#cantidad').val();

    
    if(cliente == 0){
        swal({
            title: "Seleccione un cliente",
            text: "Para registrar la venta debe haber seleccionado un cliente",
            type: "warning",
            icon: "warning",
            confirmButtonColor: "#d51b23"
        });
        return;
    }

    if(producto == 0){
        swal({
            title: "Seleccione un producto",
            text: "Para registrar la venta debe haber seleccionado un producto",
            type: "warning",
            icon: "warning",
            confirmButtonColor: "#d51b23"
        });
        return;
    }else{
        producto = producto.split("-")[0]
    }

    if (total == "") {
        swal({
            title: "Ingrese una cantidad de productos",
            text: "Para registrar la venta debe haber seleccionado cantidad de productos",
            type: "warning",
            icon: "warning",
            confirmButtonColor: "#d51b23"
        });
        return;
    }

    registrarVenta(cliente, producto, total);
    

});

$(document).on('keyup', '#cantidad', function () {
   validateCantidad(); 
});

$(document).on('blur', '#cantidad', function () {
    validateCantidad(); 
 });

function validateCantidad() {
    var total = $('#cantidad').val();
    var precio = $('#productos').val();
    console.log(precio)
    if(precio == "0"){
        swal({
            title: "Seleccione un producto",
            text: "Para registrar la venta debe haber seleccionado un producto",
            type: "warning",
            icon: "warning",
            confirmButtonColor: "#d51b23"
        });
        $('#cantidad').val("");
        return;
    }else{
        precio = precio.split('-')[1]
    }
    var total_venta = total*precio;
    $('#total_venta').val("$"+total_venta+" COP");
}

function registrarVenta(cliente, producto, total) {
    $.ajax({
        type: "POST",
        data: {
            id_cliente: cliente,
            id_producto: producto,
            total: total
        },
        url: "/ventas/nueva/",
        success: function (msg) {
            console.log(msg)
            swal({
                title: "Éxito",
                text: "Venta registra con éxito",
                icon: "success",
                buttons: false,
                timer: 1500,
            });
            location.reload(true);
        },
        async: false,
        dataType: "json",
        cache: "false",
        error: function (msg) {
            swal({
                title: "Error AJAX",
                text: msg.responseText,
                html: true,
                type: "warning",
                confirmButtonColor: "#d51b23"
            });
            console.log("AJAXerror");
            console.log(msg);
        },
    });
}

// limitar el ingreso de letras en el total de objetos en una venta
$(document).on('keypress', '#cantidad', function (e) {

    tecla = (document.all) ? e.keyCode : e.which;

    //backspace to delete always allows it
    if (tecla == 8 ) {
        return true;
    }
    // entry pattern, just accept numbers
    patron = /[0-9]/;
    tecla_final = String.fromCharCode(tecla);
    return patron.test(tecla_final);
});
