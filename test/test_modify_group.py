from model.group import Group

def test_modify_fist_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="11111", header="22222", footer="2222"))
    app.session.logout()