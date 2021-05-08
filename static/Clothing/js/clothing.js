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