from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, TextAreaField, DateField


class searchForm(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])

class AssessmentForm(FlaskForm):
    Title = StringField('Title', validators=[DataRequired()])
    Module = StringField('Module', validators=[DataRequired()])
    Deadline = DateField('Deadline', validators=[DataRequired()])
    Description = TextAreaField('Description', validators=[DataRequired()])
