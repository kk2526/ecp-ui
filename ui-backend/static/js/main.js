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
            'pdfHtml5'
        ],
    } );
} );