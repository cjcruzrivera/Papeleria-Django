$(document).ready(function () {



});

$(document).on('click', '#delete', function () {
    var cliente = "";
    cliente = $(this).attr('data-nombre');
    id_cliente = $(this).attr('data-id');
    swal({
        title: "Advertencia",
        text: "¿Seguro que desea eliminar al cliente " + cliente + "?",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    })
        .then((willDelete) => {
            if (willDelete) {
                borrado = deleteCliente(id_cliente);
                console.log(borrado); 
                if (borrado) {
                    swal({
                        title: "Borrado con éxito",
                        text: "El cliente " + cliente + " ha sido borrado con éxito",
                        icon: "success",
                        buttons: false,
                        timer: 1500,
                    });
                    
                    setTimeout(function(){ location.reload(true); }, 1500);
                }
            }
        });
});

function deleteCliente(id) {

    $.ajax({
        type: "POST",
        data: {
            id_cliente: id
        },
        url: "/clientes/eliminar/",
        success: function (msg) {
            borrado = "SI";
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
            borrado = "NO";
        },
    });
    return borrado;
}