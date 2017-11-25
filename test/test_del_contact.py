

def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.new_cont.delete_first_contact()
    app.session.logout()