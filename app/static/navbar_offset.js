function navbar_offset() {
    $("body").css("margin-top", $("#shared_navbar").outerHeight(true) + "px");
}

$(window).resize(navbar_offset);
$(document).ready(navbar_offset);
