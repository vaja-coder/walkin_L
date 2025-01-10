from configurs import db, app, login_manager
from flask_login import  UserMixin

class Item(db.Model):
    name = db.Column(db.String(), nullable=False)
    img = db.Column(db.String(), nullable=False)
    pin = db.Column(db.Integer, primary_key = True)
    size = db.Column(db.String(), nullable=False)
    price = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.String(), nullable=False)
    def __repr__(self):
        return f"{self.id},{self.name}"
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == '__main__':
    items = [{"name": "satvale", "img": "satvale.jfif", "pin": 0, "size": "100cm,by20cm", "price": "5gel",
              "description": ""},
             {"name": "mtversruti", "img": "mtversasruti.jfif", "pin": 1, "size": "1m,by1m", "price": "300$",
              "description": ""}]
    with app.app_context():
        db.create_all()
        admin = User(username = "admin", password = "admin123", address = "32324")
        user = User(username = "userA", password = "123", address = "132324")
        db.session.add(admin)
        db.session.add(user)
        db.session.commit()
        for item in items:
            added_item = Item(name=item["name"], img=item["img"], size=item["size"], price=item["price"], description=item["description"] ,user_id=2)
            db.session.add(added_item)
            db.session.commit()