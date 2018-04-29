$(document).on('click', '#delete', function () {
    var producto = "";
    producto = $(this).attr('data-nombre');
    id_producto = $(this).attr('data-id');
    swal({
        title: "Advertencia",
        text: "¿Seguro que desea eliminar el producto " + producto + "?",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    })
        .then((willDelete) => {
            if (willDelete) {
                borrado = deleteProducto(id_producto);
                console.log(borrado); 
                if (borrado) {
                    swal({
                        title: "Borrado con éxito",
                        text: "El producto " + producto + " ha sido borrado con éxito",
                        icon: "success",
                        buttons: false,
                        timer: 1500,
                    });
                    
                    setTimeout(function(){ location.reload(true); }, 1500);
                }
            }
        });
});

function deleteProducto(id) {

    $.ajax({
        type: "POST",
        data: {
            id_producto: id
        },
        url: "/productos/eliminar/",
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