from flask import render_template, jsonify
from flask import current_app as app
from flask import redirect


@app.route('/')
def index():
    return render_template(
        'index.html',
        title="Index",
        description="Index of App"
    )

@app.route('/test/')
def test():
    return redirect("../data/")