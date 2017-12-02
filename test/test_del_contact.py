from model.contact import Contact

def test_delete_first_contact(app):
    if app.new_cont.count() == 0:
        app.new_cont.create(Contact(firstname="test"))
    app.new_cont.delete_first_contact()
