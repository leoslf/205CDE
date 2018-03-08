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
        debug_msg = ""
        updated_rows = 0
        inserted_rows = 0
        print ("referrer: " + request.referrer)
        try:
            # for key in request.form:
            #     print ((key, request.form[key]))
            # msg = request.form["table_name"] + "<br />" +  "<br />".join(map(str, ["%s: %s" % (key, request.form[key]) for key in request.form]))
            table_name = request.form["table_name"]

            for name in request.form:
                err_msg = []
                # update row
                if name.startswith("id-"):
                    row_id = name.split("-")[1]
                    delta_dict = json.loads(request.form[name])
                    # msg += "update: %s, %r" % (name, delta_dict) + "<br />"
                    rc = update(table_name,
                                delta_dict,
                                condition="id = %s" % row_id,
                                errmsg=err_msg)
                    if rc < 0:
                        msg += "update failed, id: %s, delta_dict: %r" % (row_id, delta_dict) + "<br />"
                        msg += err_msg[0] + "<br />"
                    else:
                        updated_rows += rc

                elif name.startswith("newrow-"):
                    debug_msg += "insert: %s, %r" % (name, request.form[name]) + "<br />"
                    delta_dict = json.loads(request.form[name])
                    rc = insert(table_name,
                                values = delta_dict,
                                errmsg = err_msg)
                    if rc < 0:
                        msg += "update failed, delta_dict: %r" % delta_dict + "<br />"
                        msg += err_msg[0] + "<br />"
                    else:
                        msg += "inserted row's id: %d" % rc
                        inserted_rows += 1

            msg += "updated_rows: %d" % updated_rows + "<br />"
            msg += "inserted_rows: %d" % inserted_rows + "<br />"

        except Exception as e:
            # application.logger.error("Exception in login: " + str(e))
            exception_msg = str(e)
            msg += exception_msg

        return errmsg(msg, request.referrer, redirect)
    return redirect(request.referrer)
