from db_ex01_basic import db,Puppy

### Create a new Entry ###
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

[Puppy Sammy is 3 year/s old,
 Puppy Frankie is 4 year/s old,
 Puppy Rufus is 5 year/s old,
 Puppy Rufus is 5 year/s old]


### Read the entries ###
all_puppies = Puppy.query.all() # list of all puppies objects in the table.
print(all_puppies)
# Select by ID
puppy_one = Puppy.query.get(1)
print(puppy_one.name)
# Filter by name
# This will produce SQL code. Then you need to call .all object to get it printed.
puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())
# This will print based on the structure of that we defined in __repr__ method.
# It will return a list of all record.
# ["Frankie is 3 years old"]



##### update records #####
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()



####### Deleting record #########
second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()


# Print all records back.
all_puppies = Puppy.query.all()
print(all_puppies)
