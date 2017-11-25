# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="asdfaasdf", lastname="asdfeee", address="dfsf", mobile="asfsdg", email="dfs"))
    app.logout()

def test_add_empty_new_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="", lastname="", address="", mobile="", email=""))
    app.logout()
