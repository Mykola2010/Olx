from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length, URL

class ProductForm(FlaskForm):
    name = StringField("Назва предмету", [DataRequired(), Length(max=80)])
    description = StringField("Опис",[DataRequired(), Length(max=240)])
    price = FloatField("Ціна", [DataRequired()])
    image = StringField("Зображення", [DataRequired(), URL()])
    submit = SubmitField("Додати товар")