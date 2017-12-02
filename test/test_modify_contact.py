from model.contact import Contact

def test_modify_first_contact_firstname(app):
    if app.new_cont.count() == 0:
        app.new_cont.create(Contact(firstname="test"))
    app.new_cont.modify_first_contact(Contact(firstname="New firstname"))

def test_modify_first_contact_lastname(app):
    if app.new_cont.count() == 0:
        app.new_cont.create(Contact(firstname="test"))
    app.new_cont.modify_first_contact(Contact(lastname="New lastname"))
