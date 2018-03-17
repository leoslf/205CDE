function dump_errmsg() {
    var errmsg = get_cookie("errmsg");
    set_cookie("errmsg", "", 0);
    if (errmsg.length > 0) 
        $("#errmsg").removeClass("hidden").append("<span class=\"glyphicon glyphicon-remove-sign\"></span> " + errmsg);
    
    console.log(errmsg);
}

window.addEventListener("load", dump_errmsg, false);
