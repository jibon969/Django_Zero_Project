
// For DataTable jQuery Code 
$(document).ready(function () {
	var table = $('#datatables_jibon').DataTable({
		responsive: true,
		searching: true,
		pagingType: "full_numbers",
		ordering: false,
		lengthChange: false,
		buttons: ['copy', 'excel', 'csv',],
		lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]],
		"scrollY": 400,
		"scrollX": true,
	});

	table.buttons().container()
		.appendTo('#example_wrapper .col-md-6:eq(0)');
});
