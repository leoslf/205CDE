from flask import *
from jinja2 import TemplateNotFound
from app.utils import *
from collections import OrderedDict

admin = Blueprint("admin", __name__,
                  template_folder=rootpath("templates/admin"),
                  static_folder="static",
                  url_prefix="/admin")

@admin.route("/", defaults={"page": "index.html"})
@admin.route("/<page>")
def display(page):
    try:
        if logged_in() == False:
            return errmsg("Please login first")
        if authentication():
            return render_template(admin.url_prefix + "/" + page)

    except TemplateNotFound:
        return admin.send_static_file(page)

    abort(404)

@admin.route("/update_table", methods=["POST", "GET"])
def update_table():
    if request.method == "POST":
        msg = ""
        updated_rows = 0
        inserted_rows = 0
        print ("referrer: " + request.referrer)
        try:
            # for key in request.form:
            #     print ((key, request.form[key]))
            # msg = request.form["table_name"] + "<br />" +  "<br />".join(map(str, ["%s: %s" % (key, request.form[key]) for key in request.form]))
            table_name = request.form["table_name"]
            for key, value in request.form.items():
                print ((key, value))
            update_items = [request.form[key] for key in request.form if request.form[key].startswith("id")]
            update_items = [item.split("__sep__") for item in update_items]
            update_dict_by_id = {}
            
            if len(update_items) > 0:
                for item in update_items:
                    attr = dict(map(lambda s: s.split("__fieldsep__"), item))
                    # msg += ", ".join(map(str, ["%s: %s" % (key, attr[key]) for key in attr])) + "<br />"
                    if attr["id"] not in update_dict_by_id:
                        update_dict_by_id[attr["id"]] = OrderedDict()
                    update_dict_by_id[attr["id"]][attr["column"]] = attr["value"]
                    # msg += "%r %r %r" % (row_id, update_dict_by_id[row_id], item) + "<br />"
                for row_id in update_dict_by_id:
                    err_msg = []
                    col_and_val = ", ".join(["%s = '%s'" % (column, update_dict_by_id[row_id][column]) for column in update_dict_by_id[row_id]])
                    rc = update(table_name, col_and_val, "id = " + row_id, err_msg)
                    if rc == -1: # error occured
                        msg += err_msg[0] + "<br />"
                    else:
                        updated_rows += rc

        except Exception as e:
            # application.logger.error("Exception in login: " + str(e))
            exception_msg = str(e)
            msg += exception_msg

        return errmsg(msg, request.referrer, redirect)
    return redirect(request.referrer)
