# -*- coding: utf-8 -*-


def index():
    with open("./web_server/static_resource/demo.html") as f:
        content = f.read()

    return content


def login():
    return "这是登录页"


def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html;charset=utf-8")])
    if environ['PATH_INFO'] == "/index.py":
        return index()
    elif environ['PATH_INFO'] == "/login.py":
        return login()
    else:
        return "NOT FOUND"
