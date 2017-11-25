from model.contact import Contact

def test_modify_fist_contact(app):
    app.session.login(username="admin", password="secret")
    app.new_cont.modify_first_contact(Contact(firstname="11111", lastname="22222", address="3333", mobile="4444", email="5555"))
    app.session.logout()