var pos, $details;

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    $details.text("Geolocation is not supported by this browser.");
  }
}

function showPosition(position) {
  pos = position.coords;
  $details.html(
    `
    <div class="row mb-2">
      <div class="col-sm-2">Latitude:</div>
      <div class="col-sm-10">${pos.latitude}</div>
    </div>
    <div class="row mb-2">
      <div class="col-sm-2">Longitude:</div>
      <div class="col-sm-10">${pos.longitude}</div>
    </div>
    <div class="row mb-2">
      <div class="col-sm-2">Accuracy:</div>
      <div class="col-sm-10">${pos.accuracy}</div>
    </div>
    `
  );
  $('#btn_submit').attr("disabled", null);
}

$(document).ready(function() {
  $details = $("#details");
  $('#btn_submit').on('click', function() {
    if ($('#uname').val() == "") {
      alert("Input username");
      $('#uname').focus();
      return;
    }

    var data = pos;
    data.username = $('#uname').val();
    
    $.post("/api/savelocation", data, function(r) {
      if (r.success) {
        alert("Success");
      }
      else {
        if (r.error)
          alert(r.error);
        else
          alert("Invalid request");
      }
    });
  });

  function change_status(data) {
    $.post("/api/changestatus", data, function(r) {
      if (r.success) {
        alert("Success");
        location.reload();
      }
      else {
        if (r.error)
          alert(r.error);
        else
          alert("Invalid request");
      }
    });
  }

  $('.btn-approval').on('click', function() {
    const id = $(this).parent().parent().get(0).id;
    change_status({'id': id, 'status': 'approved'});
  });

  $('.btn-denial').on('click', function() {
    const id = $(this).parent().parent().get(0).id;
    change_status({'id': id, 'status': 'denied'});
  });
});