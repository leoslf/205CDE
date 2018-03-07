/* jQuery Plugin */
(function ($) {
    /* Attaching new method to jQuery */
    $.fn.extend({
        /* Plugin's name */
        editabletbl: function (options) {
            "use strict";

            /* Iterate through the set of matched elements */
            return this.each(function () {

                var default_options = function () {
                        var options = $.extend({}, {
                                css_properties: ["padding", 
                                                 "padding-top", "padding-bottom", "padding-left", "padding-right",
                                                 "text-align", 
                                                 "font", "font-size", "font-family", "font-weight",
                                                 "border", 
                                                 "border-top", "border-bottom", "border-left", "border-right"],
                                editor: $("<input>")
                            });
                        options.editor = options.editor.clone();
                        return options;
                    };
                var current_options = $.extend(default_options(), options),
                    key = {
                        left: 0x25, up: 0x26, right: 0x27, down: 0x28, enter: 0xd, esc: 0x1b, tab: 0x9,
                    },
                    elem = $(this),
                    active_elem,
                    editor = current_options.editor
                                   .css("position", "absolute")
                                   .hide()
                                   .appendTo(elem.parent()),
                    showEditor = function (select) {
                        active_elem = elem.find("td:focus");
                        if (active_elem.length) {
                            editor.val(active_elem.text())
                                .removeClass("error")
                                .show()
                                .offset(active_elem.offset())
                                .css(active_elem.css(current_options.css_properties))
                                .width(active_elem.width())
                                .height(active_elem.height())
                                .focus();

                            if (select)
                                editor.select();
                        }
                    },
                    setActiveText = function () {
                        var text = editor.val(),
                            event = $.Event("change"),
                            content_backup;

                        if (active_elem.text() === text || editor.hasClass("error"))
                            return true;

                        content_backup = active_elem.html();
                        active_elem.text(text).trigger(event, text);


                        if (event.result === false)
                            active_elem.html(content_backup);
                        else {
                            active_elem.addClass("changed");
                            /* add <input type="hide" name="" value="" /> */
                            const sep = "__sep__";
                            const fieldsep = "__fieldsep__";
                            var id = "id" + fieldsep + active_elem.siblings(":first").text() + sep
                                    + "column" + fieldsep + elem.find("th").eq(active_elem.index()).text();
                            if ($("#" + id).length == 0) {
                                $("<input>").attr({
                                    name: id,
                                    type: "text",
                                    class: "hidden"
                                }).appendTo(elem.parent());
                            }
                            $("input[name=" + id + "]").attr("value", id + sep + "value" + fieldsep + active_elem.text());
                        }


                    },
                    movement = function (elem, keycode) {
                        switch (keycode) {
                            case key.right:
                                return elem.next("td");
                            case key.left:
                                return elem.prev("td");
                            case key.up:
                                return elem.parent().prev().children().eq(elem.index());
                            case key.down:
                                return elem.parent().next().children().eq(elem.index());
                        }
                        return [];
                    };

                editor.blur(function () {
                    setActiveText();
                    editor.hide();
                }).keydown(function (event) {
                    switch (event.which) {

                        case key.enter:
                            setActiveText();
                            active_elem.focus();
                            editor.hide();
                            event.preventDefault();
                            event.stopPropagation();
                            break;
                        case key.esc:
                            editor.val(active_elem.text());
                            active_elem.focus();
                            editor.hide();
                            event.preventDefault();
                            event.stopPropagation();
                            break;
                        case key.tab:
                            active_elem.focus();
                            break;
                        default:
                            if (this.selectionEnd - this.selectionStart === this.value.length) {
                                var move = movement(active_elem, event.which);
                                if (move.length > 0) {
                                    move.focus();
                                    event.preventDefault();
                                    event.stopPropagation();
                                }
                            }
                    }
                })
                .on("input paste", function () {
                    var event = $.Event("validate");
                    active_elem.trigger(event, editor.val());
                    if (event.result === false)
                        editor.addClass("error");
                    else 
                        editor.removeClass("error");
                });

                elem.on("click keypress dblclick", showEditor)
                    .css("cursor", "pointer")
                    .keydown(function (event) {
                        var prevent = true,
                            move = movement($(event.target), event.which);
                        if (move.length > 0)
                            move.focus();
                        else if (event.which === key.enter) 
                            showEditor(false);
                        else if (event.which === 17 || event.which === 91 || event.which === 93) {
                            showEditor(true);
                            prevent = false;
                        }
                        else
                            prevent = false;
                        
                        if (prevent) {
                            event.stopPropagation();
                            event.preventDefault();
                        }
                    });
                
                elem.find("td").prop("tabindex", 1);

                $(window).on("resize", function () {
                    if (editor.is(":visible")) 
                        editor.offset(active_elem.offset())
                            .width(active_elem.width())
                            .height(active_elem.height());
                });
            });
        }
    });
})(jQuery);


$("#addrow_btn").on("click", function () {
    "use strict";
    var tr = $("<tr>");
    for (var i = 0; i < $("#table > thead > tr > th").length; ++i) {
        var td = $("<td>");
        td.attr("tabindex", 1);
        tr.append(td);
    }
    $("#table > tbody").append(tr);
});
