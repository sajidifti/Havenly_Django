// const page ="127.0.0.1"

$(document).ready(function () {
  $(window).scroll(function () {
    var scroll = $(window).scrollTop();
    if (scroll > 200) {
      $(".bg-scollme").css("background", "rgba(0, 0, 0, 0.4)");
    } else {
      $(".bg-scollme").css("background", "transparent");
    }
  });
});