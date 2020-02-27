from models import People


# Insert data into table People
def insert_person():
    person = People(name='Craig', age=20)
    print(person)
    person.save()


# Select data in the table People
def select_person():
    person = People.query.all()
    print(person)
    # for i in person:
    #     print(i.name)
    person = People.query.filter_by(name='Diana').first()
    print(person.age)


# Update data in the table People
def update_person():
    person = People.query.filter_by(name='Craig').first()
    person.age = 21
    person.save()
    person.name = 'Diana'
    person.save()


# Delete data in the table People
def delete_person():
    person = People.query.filter_by(name='Diana').first()
    person.delete()


if __name__ == '__main__':
    insert_person()
    update_person()
    select_person()
    delete_person()
