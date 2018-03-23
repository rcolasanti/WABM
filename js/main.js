$(document).ready(function(){
    $("button").click(function(){
        buttonAction()
    });
});

var buttonAction = function(number) {
    console.log("action load")
    $.ajax({
      url: "http://192.168.0.17:5000/getupdate",
      // The name of the callback parameter, as specified by the YQL service
      jsonp: "callback",
      // Tell jQuery we're expecting JSONP
      dataType: "jsonp",
      // Tell what type of call
      type:'GET',
      data: {
        company_number: 7
      },

      // Work with the response
      success: function(response) {
        console.log(response); // server response
      }
    }) ;
  }
