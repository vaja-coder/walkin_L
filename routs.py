from flask import render_template, request, redirect
from flask_login import login_user, logout_user, current_user
from forms import AddItemForm ,RegisterForm, LoginForm, BuyingForm
import os
from configurs import app
from asd import Item, db, User


@app.route("/")
def index():
    user = current_user
    items = Item.query.all()
    return render_template("main.html", items=items, user=user)



@app.route("/see_info/<item_pin>")
def see_info(item_pin):
    items = Item.query.get(item_pin)
    selected_item = items
    return render_template("2slide.html" , item=selected_item)

@app.route("/add_item", methods=["GET", "POST"])
def add_items():
    form = AddItemForm()
    if request.method == "POST":
        file = request.files["img"]
        filename = file.filename
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        print(current_user.id)
        item = Item(name = form.item_name.data, img = filename, size=form.size.data, description = form.description.data, price = form.price.data ,user_id=current_user.id)
        db.session.add(item)
        db.session.commit()
        return redirect("/")
    return render_template("1slide.html",form=form)


@app.route("/edit_item/<int:pin>", methods=["GET", "POST"])
def edit_items(pin):

    select_item = Item.query.get(pin)
    form = AddItemForm( name=select_item.name, img=select_item.img, size=select_item.size, description=select_item.description, price=select_item.price)
    if request.method == "POST":
        file = request.files["img"]
        filename = file.filename
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        select_item.name = form.item_name.data
        select_item.img = filename
        select_item.size = form.size.data
        select_item.description = form.description.data
        select_item.price = form.price.data
        db.session.commit()
        return redirect("/")
    return render_template("1slide.html",form=form)

@app.route("/delete_item/<int:pin>")
def delete(pin):
    delete_item = Item.query.get(pin)
    db.session.delete(delete_item)
    db.session.commit()
    return redirect("/")

@app.route("/register",methods=["GET","POST"])
def register():
    form = RegisterForm()
    if request.method == "POST":
        user = User(username=form.username.data, password=form.password.data, address = form.username.data)
        login_user(user)
        db.session.add(user)
        db.session.commit()
        print("registered")
        return redirect("/")
    return render_template("register.html", form=form)

@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            print("logged in")
            login_user(user)
            db.session.add(user)
            db.session.commit()
            return redirect("/")
    return render_template("login.html", form=form)

@app.route("/logout", methods=["Post","GET"])
def logout():
    logout_user()
    print("logged out")
    return redirect("/")

@app.route("/buy/<pin>", methods=["POST","GET"])
def buy(pin):
    form = BuyingForm()
    print(form)
    if request.method == "POST":
        print(request.method)
        user = User.query.filter_by(password=form.password.data).first()
        if user.password == form.password.data:
            delete_item = Item.query.get(pin)
            db.session.delete(delete_item)
            db.session.commit()
            return redirect("/")
    return render_template("buy.html", form=form)

@app.route("/ban/<int:user_id>", methods=["POST"])
def ban_user(user_id):
    admin = User.query.get(1)  # Assuming admin has ID 1
    if current_user.id == 1 and admin.id == 1:
        selected_user = User.query.get(user_id)
        db.session.delete(selected_user)
        db.session.commit()
        return redirect("/")
    return redirect("/")


