from flask import *
from jinja2 import TemplateNotFound
from crm.utils import *
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

        msg = []
        if authentication(msg):
            return render_template(admin.url_prefix + "/" + page)
        else:
            assert (len(msg) > 0)
            return errmsg(msg[0]) 
            

    except TemplateNotFound:
        return admin.send_static_file(page)

    abort(404)

@admin.route("/update_table", methods=["POST", "GET"])
def update_table():
    if request.method == "POST":
        msg = dict(success="", info="", warn="", err="")
        updated_rows = 0
        inserted_rows = 0
        print ("referrer: " + request.referrer)
        try:
            # for key in request.form:
            #     print ((key, request.form[key]))
            # msg = request.form["table_name"] + "<br />" +  "<br />".join(map(str, ["%s: %s" % (key, request.form[key]) for key in request.form]))
            table_name = request.form["table_name"]
            print ("UPDATE: " + table_name)
            print (str(request.form))

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
                        msg["err"] += "update failed, id: %s, delta_dict: %r" % (row_id, delta_dict) + "<br />" \
                                        + err_msg[0] + "<br />"
                    else:
                        updated_rows += rc

                elif name.startswith("newrow-"):
                    msg["info"] += "insert: %s, %r" % (name, request.form[name]) + "<br />"
                    delta_dict = json.loads(request.form[name])
                    rc = insert(table_name,
                                values = delta_dict,
                                errmsg = err_msg)
                    if rc < 0:
                        msg["err"] += "update failed, delta_dict: %r" % delta_dict + "<br />" \
                                        + err_msg[0] + "<br />"
                    else:
                        msg["info"] += "inserted row's id: %d" % rc
                        inserted_rows += 1

            if updated_rows > 0:
                msg["success"] += "updated_rows: %d" % updated_rows + "<br />"
            if inserted_rows > 0:
                msg["success"] += "inserted_rows: %d" % inserted_rows + "<br />"

        except Exception as e:
            # application.logger.error("Exception in login: " + str(e))
            exception_msg = str(e)
            msg["err"] += exception_msg
            error(exception_msg)

        return set_msg(msg, request.referrer, redirect)
    return redirect(request.referrer)
