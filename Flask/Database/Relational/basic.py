# if you want to run this file again and again then you have first
# delte the data.sqlite db and then run models.py and then this basic.py
# # this is the file where entries for table will be created.
from models import db,Puppy,Owner,Toy

# creating 2 puppies
rufus = Puppy('Rufus')
fido = Puppy('Fido')

# Add puppies to db.
db.session.add_all([rufus,fido])
db.session.commit()

# Check!
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first() # will give the first
# rufus = Puppy.query.filter_by(name='Rufus').all() # will give all puppies with name Rufus.
print(rufus)

# Create owner object
jose = Owner('Jose', rufus.id)

# Give Rufus some toys.

toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([jose,toy1,toy2])
db.session.commit()

# Grab Rufus after those additions

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

rufus.report_toys()
