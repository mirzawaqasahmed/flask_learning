from puppy_project import db
# Setup db inside the __init__.py file under the puppy_project folder

class Puppy(db.Model):

    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        # return f"Puppy name: { self.name }, Puppy ID: { self.id }"
        if self.owner:
            return f"Puppy name is { self.name }-ID:{ self.id } and owner is { self.owner.name }"
        else:
            return f"Puppy name is { self.name }-ID:{ self.id } and has no owner yet!"

class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, index=True)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"Owner name: { self.name }, Puppy ID: { self.puppy_id }"
