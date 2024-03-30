from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, SubmitField


class ReviewForm(FlaskForm):
    name = StringField("Your Name", validators=[validators.DataRequired()])
    rating = StringField("Rating", validators=[validators.DataRequired()])
    comment = TextAreaField("Comment", validators=[validators.DataRequired()])
    submit = SubmitField("Submit Review")
