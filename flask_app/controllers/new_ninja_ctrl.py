from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.new_ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

@app.route('/')
def index2():
    ninjas = Ninja.get_all()
    print(ninjas)
    return render_template("dojos.html", all_ninjas = ninjas)


@app.route('/create/homepage')
def create_ninja_home():
    dojos = Dojo.get_all()
    
    return render_template("new_ninja.html", all_dojos = dojos)


@app.route('/create/ninja', methods = ['POST'])
def create_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    Ninja.create(data)

    return redirect('/')

