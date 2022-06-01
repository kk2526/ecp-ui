var action = [
	"Delete","In-Review","Keep"

];

$(document).ready(function() {
    $('#example').DataTable( {
        dom: 'lBfrtip',
        "pageLength": 25,
        responsive: true,
        stateSave: true,
        buttons: [
            'excelHtml5',
            'pdfHtml5',
            {
                text: 'Alert',
                action: function ( e, dt, node, config ) {
                    alert( 'Activated!' );
                    this.disable(); // disable button
                }
            }
        ],
        columns:[
        	null,
        	null,
        	null,
        	{
            	"render": function(d,t,r){
                	var $select = $("<select></select>", {
                    	"id": r[0]+"start",
                        "value": d
                    });
                	$.each(action, function(k,v){
                    	var $option = $("<option></option>", {
                        	"text": v,
                            "value": v
                        });
                        if(d === v){
                        	$option.attr("selected", "selected")
                        }
                    	$select.append($option);
                    });
                    return $select.prop("outerHTML");
                }
            }
        ]
    } );
} );
