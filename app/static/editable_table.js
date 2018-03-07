"use strict";

/* jQuery Plugin */
(function ($) {
    /* Attaching new method to jQuery */
    $.fn.extend({
        /* Plugin's name */
        editabletbl: function (options) {

            /* Iterate through the set of matched elements */
            return this.each(function () {

                var default_options = function () {
                        var options = $.extend({}, {
                            /* CSS Properties for in-place editor */
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

                /* Constants */
                const table = $(this);
                const current_options = $.extend(default_options(), options);
                const key = { left: 0x25, up: 0x26, right: 0x27, down: 0x28, enter: 0xd, esc: 0x1b, tab: 0x9, };

                var active_cell,
                    editor = current_options.editor
                                   .css("position", "absolute")
                                   .hide()
                                   .appendTo(table.parent()),
                    showEditor = function (select) {
                        active_cell = table.find("td:focus");
                        if (active_cell.length) {
                            editor.val(active_cell.text())
                                .removeClass("error")
                                .show()
                                .offset(active_cell.offset())
                                .css(active_cell.css(current_options.css_properties))
                                .width(active_cell.width())
                                .height(active_cell.height())
                                .focus();

                            if (select)
                                editor.select();
                        }
                    },
                    setActiveText = function () {
                        var text = editor.val(),
                            event = $.Event("change"),
                            content_backup;

                        if (active_cell.text() === text || editor.hasClass("error"))
                            return true;

                        content_backup = active_cell.html();
                        active_cell.text(text).trigger(event, text);


                        if (event.result === false)
                            active_cell.html(content_backup);
                        else {
                            active_cell.addClass("changed");
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
                            active_cell.focus();
                            editor.hide();
                            event.preventDefault();
                            event.stopPropagation();
                            break;
                        case key.esc:
                            editor.val(active_cell.text());
                            active_cell.focus();
                            editor.hide();
                            event.preventDefault();
                            event.stopPropagation();
                            break;
                        case key.tab:
                            active_cell.focus();
                            break;
                        default:
                            if (this.selectionEnd - this.selectionStart === this.value.length) {
                                var move = movement(active_cell, event.which);
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
                    active_cell.trigger(event, editor.val());
                    if (event.result === false)
                        editor.addClass("error");
                    else 
                        editor.removeClass("error");
                });

                table.on("click keypress dblclick", showEditor)
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
                
                table.find("td").prop("tabindex", 1);

                $(window).on("resize", function () {
                    if (editor.is(":visible")) 
                        editor.offset(active_cell.offset())
                            .width(active_cell.width())
                            .height(active_cell.height());
                });
            });
        }
    });
})(jQuery);


$("#addrow_btn").on("click", function () {

    var tr = $("<tr>").addClass("new-row");

    for (var i = 0; i < $("#table > thead > tr > th").length; ++i) {
        var td = $("<td>");
        td.attr("tabindex", 1);
        tr.append(td);
    }
    $("#table > tbody").append(tr);
});



$("#table").closest("form").submit(function (e) {

    /* Helper Function */
    function colname(table, col) {
        return table.find("th").eq($(col).index()).text();
    }

    // console.log("submitting");
    
    /* loop through rows */
    var table = $("#table"),
        new_row_count = 0;
    $("#table > tbody > tr").each(function (i, row) {
        var delta_dict = {};
        $(row).find("td").each(function (j, col) {
            // console.log("col " + j + " class: " + $(col).attr("class"));
            if ($(col).hasClass("changed")) {
                var column_name = colname(table, col),
                    column_value = $(col).text();
                delta_dict[column_name] = column_value;
            }
        });

        if (Object.keys(delta_dict).length > 0) {
            var row_id = $(row).find("td:first").text(),
                input_name = $(row).hasClass("new-row") 
                                ? "newrow-" + new_row_count++ 
                                : "id-" + row_id; // Primary Key
            console.log(input_name);
            /* new row */
            $("<input>").attr({
                name: input_name,
                type: "text",
                class: "hidden",
                value: JSON.stringify(delta_dict)
            }).appendTo(table.parent());
        }
    });

    
    // prevent default
    //return false; // superfluous, but placed here for fallback
    
    // continue to submit form with update_table
    return true; 
});
    
