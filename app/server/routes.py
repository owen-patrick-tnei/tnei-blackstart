from dash.dependencies import Output
from dash_core_components import Input
from flask import render_template, jsonify, request
from flask import current_app as app
from flask import redirect
from flask_login import login_required, current_user

@app.route('/home')
def index():
    return render_template(
        'index.html',
        title="Index",
        description="Index of App"
    )

@app.route('/test/')
def test():
    return redirect("../data/")

@app.before_request
def dash():
    print(request.path)
    if("dash" in request.path):
        if(current_user is None):
            return redirect("/")
