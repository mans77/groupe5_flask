$("document").ready(function(){
    $(".loaduser").on("click",function(){ 
      window.location.href = "http://127.0.0.1:5000/load";  
    });
  });

  $("document").ready(function(){
    $(".pav").on("click",function(){ 
      window.location.href = "http://127.0.0.1:5000/login";  
    });
  });
  $("document").ready(function(){
    $(".adduser").on("click",function(){ 
      window.location.href = "http://127.0.0.1:5000/newuser";  
    });
  });

