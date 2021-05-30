//jshint esversion: 6

const csrftoken = Cookies.get('csrftoken');

document.getElementById('rating').addEventListener('click', function(e) {
    var URL = "{% url 'rating' %}";
    e = e || window.event;
    var target = e.target || e.srcElement;
    target = String(target);
    var data = {'data': target.charAt(target.length - 1)};
    $.ajax({
        url:'/mobile/oneplus',
        type: "POST",
        data: data,
        headers: {'X-CSRFToken': csrftoken},
        success: function(response) {
            alert('Success');
        },
        error:function (xhr, textStatus, thrownError) {
            alert("Text status = " + textStatus);
            alert("Thrown Error = " + thrownError);
        }
    });
}, false);

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