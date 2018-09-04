from db_ex01_basic import db,Puppy

# Creates all the table. Essentially from Model creating a DB Table.
db.create_all()

sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 4)

#This will print none...because nothing is added right now in db.
print(sam.id)
print(frank.id)


db.session.add_all([sam, frank])

# The above can be done using.
# db.session.add(sam)
# db.session.add(frank)

db.session.commit()
# will save the changes to db.

print(sam.id)
print(frank.id)
