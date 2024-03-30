from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import select

from app.forms.review import ReviewForm
from app.database import Session
from app.models import Post


bp = Blueprint("default", __name__)


@bp.route("/index")
@bp.route("/")
def index():
    with Session() as session:
        query = select(Post)
        posts = session.scalars(query).all()
    return render_template("main.html", posts=posts)

# https://openweathermap.org/


@bp.route("/reviews", methods=["GET", "POST"])
def reviews():
    form = ReviewForm()
    if form.validate_on_submit():
        name = form.name.data
        rating = form.rating.data
        comment = form.comment.data

        flash("Thank you for your review!", "success")
        return redirect(url_for("default.reviews"))

    return render_template("reviews.html", form=form)


@bp.route("/reviews_list")
def reviews_list():
    reviews = [
        {"name": "John", "rating": "5", "comment": "Great pizza!"},
        {"name": "Jane", "rating": "3", "comment": "Average pizza."},
    ]
    return render_template("reviews_list.html", reviews=reviews)
