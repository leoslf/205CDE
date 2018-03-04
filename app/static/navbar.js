function navbar_active() {
    $("#shared_navbar > div > div > ul > li > a").each(function(index, element) {
        var href = $(element).attr("href");
        console.log("href: " + href + " vs " + window.location.pathname);
        if (href == window.location.pathname)
            $(element).addClass("active");
    });
}

window.addEventListener("load", navbar_active, false);

