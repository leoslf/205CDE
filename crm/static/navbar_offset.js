function navbar_offset() {
    $("body").css("margin-top", $("#shared_navbar").outerHeight(true) + "px");
}

window.addEventListener("load", navbar_offset, false);
