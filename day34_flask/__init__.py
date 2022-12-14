from flask import Flask, request, session, redirect


def auth():
    if request.path.startswith("/login"):
        return

    if request.path.startswith("/static"):
        return

    name = session.get("user_info")
    if not name:
        return redirect("/login")


def get_mobile():
    return session["user_info"]["mobile"]


def create_app():
    app = Flask(__name__)
    app.secret_key = "0923i;ajksdf;apj230480239sxnvlkjv"

    app.before_request(auth)

    app.template_global()(get_mobile)

    from .views import account
    from .views import order

    app.register_blueprint(account.ac)
    app.register_blueprint(order.od)

    return app
