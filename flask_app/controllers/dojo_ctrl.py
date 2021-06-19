from flask import Flask, render_template, request, redirect, session
from flask_app import app
from ..models.dojo_model import Dojo
from ..models.new_ninja_model import Ninja


@app.route('/')
def index():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("dojos.html", all_dojos = dojos)


@app.route('/create/dojo', methods = ['POST'])
def creates_dojo():
    dojos_id = Dojo.create(request.form)
    return redirect('/')


@app.route('/show/dojo/<int:dojo_id>')
def dojo_show(dojo_id):
    this_dojo = Dojo.get_one( {'id':dojo_id})
    return render_template('dojo_members.html', this_dojo = this_dojo)
