// const csrftoken = Cookies.get('csrftoken');sour

// document.getElementById('rating').addEventListener('click', function(e) {
//     var URL = "{% url 'rating' %}";
//     e = e || window.event;
//     var target = e.target || e.srcElement;
//     target = String(target);
//     var data = {'data': target.charAt(target.length - 1)};
//     $.ajax({
//         url:'/mobile/oneplus',
//         type: "POST",
//         data: data,
//         headers: {'X-CSRFToken': csrftoken},
//         success: function(response) {
//             alert('Success');
//         },
//         error:function (xhr, textStatus, thrownError) {
//             alert("Text status = " + textStatus);
//             alert("Thrown Error = " + thrownError);
//         }
//     });
// }, false);

// document.getElementsByClassName('stars-box')[0].addEventListener('click', function(e) {
//   alert(e.target.dataset.value);
//   var data = {'data': e.target.dataset.value};
//   $.ajax({
//     url:'/mobile/oneplus',
//     type: "POST",
//     data: data,
//     headers: {'X-CSRFToken': csrftoken},
//     success: function(response) {
//         alert('Success');
//     },
//     error:function (xhr, textStatus, thrownError) {
//         alert("Text status = " + textStatus);
//         alert("Thrown Error = " + thrownError);
//     }
//   });
// });

$(function () {
    $('[data-toggle="tooltip"]').tooltip();
});

var d = new Date();
d.setDate(d.getDate() + 3);
document.getElementById("free-delivery").innerHTML = "Free Delivery: " + d.toDateString();

d = new Date();
d.setDate(d.getDate() + 1);
document.getElementById("fastest-delivery").innerHTML = "Fastest Delivery: " + d.toDateString();

$(document).ready(function(){
    $('[data-toggle="popover"]').popover();
});




$(".rating-component .star").on("mouseover", function () {
  var onStar = parseInt($(this).data("value"), 10); //
  $(this).parent().children("i.star").each(function (e) {
    if (e < onStar) {
      $(this).addClass("hover");
    } else {
      $(this).removeClass("hover");
    }
  });
}).on("mouseout", function () {
  $(this).parent().children("i.star").each(function (e) {
    $(this).removeClass("hover");
  });
});

$(".rating-component .stars-box .star").on("click", function () {
  var onStar = parseInt($(this).data("value"), 10);
  var stars = $(this).parent().children("i.star");
  var ratingMessage = $(this).data("message");

  var msg = "";
  if (onStar > 1) {
    msg = onStar;
  } else {
    msg = onStar;
  }
  $('.rating-component .starrate .ratevalue').val(msg);
  

 
  $(".fa-smile-wink").show();
  
  $(".button-box .done").show();

  if (onStar === 5) {
    $(".button-box .done").removeAttr("disabled");
  } else {
    $(".button-box .done").attr("disabled", "true");
  }

  for (i = 0; i < stars.length; i++) {
    $(stars[i]).removeClass("selected");
  }

  for (i = 0; i < onStar; i++) {
    $(stars[i]).addClass("selected");
  }

  $(".status-msg .rating_msg").val(ratingMessage);
  $(".status-msg").html(ratingMessage);
  $("[data-tag-set]").hide();
  $("[data-tag-set=" + onStar + "]").show();
});

$(".feedback-tags  ").on("click", function () {
  var choosedTagsLength = $(this).parent("div.tags-box").find("input").length;
  choosedTagsLength = choosedTagsLength + 1;

  if ($(this).hasClass("choosed")) {
    $(this).removeClass("choosed");
    choosedTagsLength = choosedTagsLength - 2;
  } else {
    $(this).addClass("choosed");
    $(".button-box .done").removeAttr("disabled");
  }

  console.log(choosedTagsLength);

  if (choosedTagsLength <= 0) {
    $(".button-box .done").attr("enabled", "false");
  }
});



$(".compliment-container .fa-smile-wink").on("click", function () {
  $(this).fadeOut("slow", function () {
    $(".list-of-compliment").fadeIn();
  });
});



$(".done").on("click", function () {
  $(".rating-component").hide();
  $(".feedback-tags").hide();
  $(".button-box").hide();
  $(".submited-box").show();
  $(".submited-box .loader").show();

  setTimeout(function () {
    $(".submited-box .loader").hide();
    $(".submited-box .success-message").show();
  }, 1500);
});
