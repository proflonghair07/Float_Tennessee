

  $( "#test" ).click(function() {
    $.ajax({

        type:"GET",//or POST
        url:'http://localhost:8000/float/users/',
                           //  (or whatever your url is)
        data:{},
        //can send multipledata like {data1:var1,data2:var2,data3:var3
        //can use dataType:'text/html' or 'json' if response type expected 
        success:function(responsedata){
               // process on data
               console.log("got response as "+"'"+responsedata+"'");

        }
     }) 
  });