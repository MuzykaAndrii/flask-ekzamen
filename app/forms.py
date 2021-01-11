from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError, Regexp
from app.models import Article


class ArticleForm(FlaskForm):
    name = StringField('Article name', validators=[Length(min=4, max=90, message='too long/short'), DataRequired(message='This area is required')])
    year_posted = IntegerField('Year posted', validators=[DataRequired(message='This area is required')])
    count_of_pages = IntegerField('Number of pages',validators=[DataRequired(message='This area is required')])
    author = StringField('Author name', validators=[Length(min=4, max=50, message='too long/short'), DataRequired(message='This area is required')])
    note = TextAreaField('Article note', validators=[Length(min=4, max=300, message='too long/short'), DataRequired(message='This area is required')])
    type_of_art = SelectField('Type of article', choices=['book', 'article', 'tags', 'matherial', 'other'], validate_choice=True)

    submit = SubmitField('Enter')

    def validate_username(self, name):
        if Article.query.filter_by(name=name.data).first():
            raise ValidationError('This article already exists')
