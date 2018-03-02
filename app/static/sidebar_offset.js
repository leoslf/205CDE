function sidebar_offset() {
    navbar_offset();
    $("#main").css("margin-left", $("#cms_navbar").outerWidth(true) + "px");
    $("#main").css("width", ((1 - $("#cms_navbar").outerWidth(true) / $("html").outerWidth(true)) * 100) + "%");
}

$(window).resize(sidebar_offset);
$(document).ready(sidebar_offset);
