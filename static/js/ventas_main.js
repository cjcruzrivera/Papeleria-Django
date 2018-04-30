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

    
    

});

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