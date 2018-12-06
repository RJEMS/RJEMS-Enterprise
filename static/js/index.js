$(document).ready(function() {

$('#div_text').hide();
$('#div_upload').hide();


var coll = document.getElementsByClassName("collapsible");

var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  }
  )
  };

  var modal = document.getElementById('myModal');
  // Get the image and insert it inside the modal - use its "alt" text as a caption
  var img = document.getElementById('1');
  var images = $("img.img-thumbnail")
  var modalImg = document.getElementById("img01");
  var captionText = document.getElementById("caption");
    var setImageCallback = function(elem) {
        elem.onclick = function() {
            modal.style.display = "block"
            modalImg.src = elem.src;
        }
  }
  _.forEach(images, setImageCallback)

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[0];

  //When the user clicks on <span> (x), close the modal
 span.onclick = function() {
     modal.style.display = "none";
 }

});


// on change function of upload type drop down in upload page
function on_change() {
      if($('#input_upload_type :selected').text() == 'Training Material/Photos')
      {
        $('#invalid_upload_type').hide();
        $('#div_text').hide();
        $('#div_upload').show();
      }

      else if($('#input_upload_type :selected').text() == 'News/Updates')
      {
        $('#invalid_upload_type').hide();
        $('#div_upload').hide();
        $('#div_text').show();
      }
      else
      {
        $('#invalid_upload_type').show();
        $('#div_text').hide();
        $('#div_upload').hide();
      }

};


// validate function of upload button in upload page
function validate_upload() {

      if($('#div_text').is(":visible")){

            if($('#input_upload_text').val() == ''){
                $('#invalid_upload_text').show();
                $('#invalid_upload_text').text('Text cannot be empty.');
                return false;
            }
            return true;

      }
      else{

              if($('#input_upload_type :selected').text() == '' || $('#input_upload_type :selected').text() == 'Select Upload Type..')
              {
                   $('#invalid_upload_type').show();
                   return false;
              }

              if($('#upload_file').val() == '')
              {
                   $('#invalid_upload_file').show();
                   $('#invalid_upload_file').text('Please select a file to upload.');
                   return false;
              }
              else
              {
                  var valid_extensions = ['pdf','jpg','jpeg','gif']; //array of valid extensions
                   var file_Ext = $('#upload_file').val().split('.').pop();
                   if(valid_extensions.indexOf(file_Ext) > -1)
                   {
                       $('#invalid_upload_file').hide();
                   }
                   else
                   {
                       $('#invalid_upload_file').show();
                       $('#invalid_upload_file').text('Allowed extensions: pdf, png, jpg, jpeg, gif');
                       return false;
                   }

              }
              return true;
      }
};


function assign_manager_role(x) {

  var email = $(x).closest('tr').find('.c4').text();
     $.ajax({
     type: "POST",
     url: "/assign_manager_role",
     data: email
  }).done(function( response ) {
      location.reload();
      // $('#input_update_message').show();

  });

};