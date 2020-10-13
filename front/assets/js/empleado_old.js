var employee = class {
    constructor() {
        this.get_employee();
    }

    clear(){
        $("#nombre").val('');
        $("#apellido").val('');
        $("#tipo_doc").val('');
        $("#doc").val('');
        $("#direccion").val('');
        $("#mail").val('');
        document.getElementById("put_client").innerHTML = `<button class="btn btn-block btn-primary mb-2" type="button" onclick="post_employee()">Registrar</button>`;
    }
    
    post_employee(data) {
        $.ajax({
            type: "POST",
            url: `http://localhost:8000/empleado/viewset/empleado/`,
            dataType: 'json',
            data: data,
            success: function (formulario) {
                //
                employees.get_employee();
                alert("Se registro con exito");
                employees.clear();
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert("Status: " + XMLHttpRequest.responseJSON.detail);
            }
        });
    }

    get_employee(){
        $.ajax({
            type: "GET",
            url: `http://localhost:8000/empleado/viewset/empleado/`,
            dataType: 'json',
            success: function (formulario) {
               let html = ""
               formulario.forEach(element => {

                html = html+`<tr>
                                <td>${element.nombres}</td>
                                <td>${element.apellidos}</td>
                                <td>${element.tipodocumento}</td>
                                <td>${element.numdocumento}</td>
                                <td>${element.direccion}</td>
                                <td>${element.email}</td>
                                <td><button class="btn btn-block btn-primary" type="button" onclick="detail_employee(${element.id})">Editar</button></td>
                                <td><button class="btn btn-block btn-danger" type="button" onclick="delete_employee(${element.id})">Eliminar</button></td>
                            </tr>`
               });

               document.getElementById('list_employee').innerHTML = html;
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert("Status: " + XMLHttpRequest.responseJSON.detail);
            }
        });
        
        
    }

    detail_employee(id){
        $.ajax({
            type: "GET",
            url: `http://localhost:8000/empleado/viewset/empleado/${id}/`,
            dataType: 'json',
            success: function (formulario) {
               
                $("#nombre").val(formulario.nombres);
                $("#apellido").val(formulario.apellidos);
                $("#tipo_doc").val(formulario.tipodocumento);
                $("#doc").val(formulario.numdocumento);
                $("#direccion").val(formulario.direccion);
                $("#mail").val(formulario.email);   
                
                document.getElementById("put_employee").innerHTML = `<button class="btn btn-block btn-warning" type="button" onclick="put_employee(${formulario.id})">Modificar</button>`;
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert("Status: " + XMLHttpRequest.responseJSON.detail);
            }
        });
    
    }


    put_employee(id,data) {
        $.ajax({
            type: "PUT",
            url: `http://localhost:8000/empleado/viewset/empleado/${id}/`,
            dataType: 'json',
            data: data,
            success: function (formulario) {
                //
                employees.get_employee();
                alert("Se Actualizo con exito");
                employees.clear();
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert("Status: " + XMLHttpRequest.responseJSON.detail);
            }
        });
    }

    delete_employee(id) {
        $.ajax({
            type: "DELETE",
            url: `http://localhost:8000/empleado/viewset/empleado/${id}/`,
            dataType: 'json',
            success: function (formulario) {
                //
                employee.get_employee();
                alert("Se Elimino con exito");

            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert("Status: " + XMLHttpRequest.responseJSON.detail);
            }
        });
    }

}

var employees = new employee();


function post_employee(){
    debugger;
    let data = {
        nombres: $('#first_name').val(),
        apellidos: $('#last_name').val(),
        tipodocumento: $('#document_type').val(),
        numdocumento: $('#document').val(),
        horario: $('#hour').val(),
    }
    obj.post_employee(data);
}

function detail_employee(id){
        employee.detail_employee(id);
}
function put_employee(id){
    let data = {
        nombres: $('#first_name').val(),
        apellidos: $('#last_name').val(),
        tipodocumento: $('#document_type').val(),
        numdocumento: $('#document').val(),
        horario: $('#hour').val(),
    }
    obj.put_employee(id, data);
}

function delete_employee(id){
    
    employee.delete_employee(id);
}




