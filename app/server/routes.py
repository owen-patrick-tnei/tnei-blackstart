from flask import render_template, jsonify
from flask import current_app as app
from flask import redirect
from flask_login import login_required


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
