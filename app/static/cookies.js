function get_cookie(name) {
    var lst = decodeURIComponent(document.cookie).split(";");
    for (var i = 0; i < lst.length; ++i) {
        var c = lst[i].trim();
        if (c.indexOf(name) == 0 && c !== "")
            return c.substring(c.indexOf("=") + 1, c.length).replace(/"([^"]+(?="))"/g, '$1');
    }
    return "";
}


function set_cookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}


