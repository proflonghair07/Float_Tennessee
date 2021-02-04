$.get( "localhost:8000/user", function( data ) {
    $( "#users" ).html( data );
    alert( "found data" );
  });

  $.get("test.php", function(data){
    alert("Data: " + data);
  });  