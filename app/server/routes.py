from dash.dependencies import Output
from dash_core_components import Input
from flask import render_template, jsonify, request
from flask import current_app as app
from flask import redirect
from flask_login import login_required, current_user, login_manager, logout_user

@app.route('/home')
def index():
    return render_template(
        'index.html',
        title="Index",
        description="Index of App"
    )

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route('/test/')
def test():
    return redirect("../data/")

@app.before_request
def dash():
    print(request.path)

    if "dash" in request.path:

        if current_user.is_authenticated:
            print("authenticated")
            return
        else:
            print("not authenticated")
            return redirect("/")

