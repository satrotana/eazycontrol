
$(document).ready(function(){
  $("#example1").DataTable({
    "responsive": true,
    "autoWidth": false,
    "ordering": false,
    "paging": false,
    "lengthChange": false,
    "info": false,

  });
  $("#example2").DataTable({
    "responsive": true,
    "autoWidth": false,
    "ordering": true,

  });
  //  $('#example2').DataTable({
  //    "paging": true,
  //    "lengthChange": false,
  //    "searching": false,
  //    "ordering": true,
  //    "info": true,
  //    "autoWidth": false,
  //    "responsive": true,
  //  });

  //Initialize Select2 Elements
  $('.select2').select2()
  //Initialize Select2 Elements
  $('.select2bs4').select2({
    theme: 'bootstrap4'
  })
});


function clearinput(id){
  $('#'+id).val('')
}
function clearLabel(id,text){
  $('#'+id).text(text)
}