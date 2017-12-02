from model.contact import Contact

def test_modify_first_contact_firstname(app):
    app.new_cont.modify_first_contact(Contact(firstname="New firstname"))

def test_modify_first_contact_lastname(app):
    app.new_cont.modify_first_contact(Contact(lastname="New lastname"))
