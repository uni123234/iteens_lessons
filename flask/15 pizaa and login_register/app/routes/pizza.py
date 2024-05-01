from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import select
from app.database import Session
from app.models import Pizza

bp = Blueprint("pizza", __name__)


@bp.route("/pizzas")
def list_pizzas():
    with Session() as session:
        pizzas = session.scalars(select(Pizza)).all()
    return render_template("pizzas.html", pizzas=pizzas)


@bp.route("/pizza/add", methods=["GET", "POST"])
def add_pizza():
    if request.method == "POST":
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        with Session() as session:
            new_pizza = Pizza(name=name, description=description, price=price)
            session.add(new_pizza)
            session.commit()
        return redirect(url_for('pizza.list_pizzas'))
    return render_template('add_pizza.html')
