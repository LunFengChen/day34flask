from datetime import datetime
import random

from flask import Blueprint, render_template, session, request, redirect

from day34_flask.utils import db

od = Blueprint("od", __name__)


@od.route("/order/list")
def order_list():
    # 1. 获取用户信息
    user_id = session["user_info"]["id"]

    # 2. 数据库获取数据
    # [{}, {}]
    data_list = db.fetch_all("select * from task where user_id=%s order by id desc", [user_id, ])

    status_dict = {
        1: "待执行",
        2: "执行中",
        3: "已完成"
    }

    # 3. 渲染页面

    return render_template("order_list.html", data_list=data_list, status_dict=status_dict)


@od.route("/order/add", methods=["GET", "POST"])
def order_add():
    if request.method == "GET":
        return render_template("order_add.html")

    # 1. 获取数据
    url = request.form.get("url")
    count = request.form.get("count")

    # 2. 在数据库中插入数据
    oid = "{}{}".format(datetime.now().strftime("%Y%m%d%H%M%S"), random.randint(1000, 9999))  # 18 位订单号
    user_id = session["user_info"]["id"]
    sql = "insert into task(oid, url, count, status, user_id) values (%s, %s, %s, %s, %s)"

    db.commit(sql, [oid, url, count, 1, user_id])

    # 3. 跳转回订单页面
    return redirect("/order/list")


@od.route("/order/delete")
def order_delete():
    # 1. 获取数据
    nid = request.args.get("nid")

    # 2. 在数据库中删除数据
    sql = "delete from task where id=%s"

    db.commit(sql, [nid, ])

    # 3. 跳转回订单页面
    return redirect("/order/list")


@od.route("/set/pwd")
def set_pwd():
    return "设置密码"
