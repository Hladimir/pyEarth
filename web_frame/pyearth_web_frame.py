# -*- coding: utf-8 -*-

URL_FUNC_DICT = dict()


def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)

        return call_func

    return set_func


@route("/index.html")
def index():
    with open("./web_server/static_resource/index.html") as f:
        content = f.read()

    return content


@route("/help.html")
def center():
    with open("./web_server/static_resource/help.html") as f:
        content = f.read()

    return content


def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html;charset=utf-8")])
    file_name = environ['PATH_INFO']

    # if environ['PATH_INFO'] == "/index.py":
    #     return index()
    # elif environ['PATH_INFO'] == "/login.py":
    #     return login()
    # else:
    #     return "NOT FOUND"

    try:
        func = URL_FUNC_DICT[file_name]
        return func()
    except Exception as ret:
        return "404 NOT FOUND %s" % str(ret)
