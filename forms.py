from flask_wtf import FlaskForm
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, length
from wtforms import StringField, SubmitField, FileField


class AddItemForm(FlaskForm):
    img =  FileField("img",validators=[DataRequired()])
    item_name = StringField("name",validators=[DataRequired("Pleas enter the item")])
    size = StringField("size",validators=[DataRequired("pleas enter the size")])
    price = StringField("price", validators=[DataRequired("pleas enter the price")])
    description = StringField("description")
    submit =SubmitField("add")

class RegisterForm(FlaskForm):
    username = StringField(label="Enter name here ", validators=[DataRequired(), length(min=5, max=55)])
    password = PasswordField(label="password", validators=[DataRequired()])
    address = StringField(label="Enter you house address here ", validators=[DataRequired()])
    submit = SubmitField("register")

class LoginForm(FlaskForm):
        username = StringField(label="Enter name here ", validators=[DataRequired(), length(min=5, max=55)])
        password = PasswordField(label="password", validators=[DataRequired()])
        submit = SubmitField("Login")

class BuyingForm(FlaskForm):
    credit_card_number = PasswordField(label="enter your credit card number", validators=[DataRequired()])
    password = PasswordField(label="enter your password", validators=[DataRequired()])
    submit = SubmitField("BUY")