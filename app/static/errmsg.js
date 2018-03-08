function dump_errmsg() {
    var errmsg = get_cookie("errmsg");
    set_cookie("errmsg", "", 0);
    // console.log("errmsg: " + errmsg);
    if (errmsg.length > 0)
        $("#errmsg").append("<span class=\"glyphicon glyphicon-remove-sign\"></span> " + errmsg)
}

window.addEventListener("load", dump_errmsg, false);
