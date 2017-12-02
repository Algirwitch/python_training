# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_new_contact(app):
    app.new_cont.create(Contact(firstname="asdfaasdf", lastname="asdfeee", address="dfsf", mobile="asfsdg", email="dfs"))

def test_add_empty_new_contact(app):
    app.new_cont.create(Contact(firstname="", lastname="", address="", mobile="", email=""))
