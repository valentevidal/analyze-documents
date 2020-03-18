$(function () {
    /* 1. OPEN THE FILE EXPLORER WINDOW */
    $(".js-upload-photos").click(function () {
      $("#fileupload").click();
    });
  
    /* 2. INITIALIZE THE FILE UPLOAD COMPONENT */
    $("#fileupload").fileupload({
      dataType: 'json',
      done: function (e, data) {  /* 3. PROCESS THE RESPONSE FROM THE SERVER */
        if (data.result.is_valid) {
          
          var form_idx1 = document.getElementById("id_form-TOTAL_FORMS").value - 1;
          console.log(form_idx1);
          // document.getElementById("id_form-0-name").value = data.result.name;
          var form_id_X_name = ('id_form-'.concat(form_idx1, '-name'));
          console.log(form_id_X_name);
          document.getElementById(form_id_X_name).value = data.result.name;
          var form_idx = $('#id_form-TOTAL_FORMS').val();
          document.getElementById("id_form-TOTAL_FORMS").value = parseInt(form_idx) + 1;
          
          //console.log(form_id_X_name);
          $('#form_set').append($('#empty_form').html().replace(/__prefix__/g, form_idx));

          // $("#gallery tbody").prepend(
          //   "<tr><td><a href='" + data.result.url + "'>" + data.result.name + "</a></td></tr>"
          //)
        }
      }
    });
  
  });