function navbar_active() {
    $("#shared_navbar ul li a").each(function(index, element) {
        var href = $(element).attr("href");
        console.log("href: " + href + " vs " + window.location.href);
        if (href == window.location.href)
            $(element).addClass("active");
    });
}

window.addEventListener("load", navbar_active, false);

