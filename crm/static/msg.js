function dump_msg() {
    var cookies = cookie_dict();
    const msgType = ["successmsg", "infomsg", "warnmsg", "errmsg"];
    for (var i = 0; i < msgType.length; ++i)
        if (msgType[i] in cookies && cookies[msgType[i]].length > 0) {
            $("#" + msgType[i]).removeClass("hidden")
                      .append(cookies[msgType[i]]);
            set_cookie(msgType[i], "", 0);
        }
}

window.addEventListener("load", dump_msg, false);
                      

        
