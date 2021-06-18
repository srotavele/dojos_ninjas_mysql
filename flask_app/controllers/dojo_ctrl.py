from flask import Flask, render_template, request, redirect, session
from flask_app import app
from ..models.dojo_model import Dojo


@app.route('/')
def index():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("dojos.html", all_dojos = dojos)
