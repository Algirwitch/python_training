from model.contact import Contact

def test_modify_fist_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.new_cont.modify_first_contact(Contact(firstname="New firstname"))
    app.session.logout()

def test_modify_fist_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    app.new_cont.modify_first_contact(Contact(lastname="New lastname"))
    app.session.logout()