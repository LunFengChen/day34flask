from flask import Blueprint, render_template, request, session, redirect

from day34_flask.utils import db

ac = Blueprint("account", __name__)


@ac.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    # 1. 获取到用户输入到的数据
    mobile = request.form.get("mobile")
    passwd = request.form.get("password")

    # 2. 连接mysql进行校验
    row_dict = db.fetch_one("select id, mobile from userinfo where mobile=%s and password=%s", [mobile, passwd])
    if not row_dict:
        return render_template("login.html", error="用户名或密码错误")

    # 3. 登陆成功
    session["user_info"] = row_dict
    return redirect("/order/list")


@ac.route("/register")
def register():
    return "注册"


@ac.route("/logout")
def logout():
    # 删除当前用户会话信息
    session.clear()

    return redirect("/order/list")
