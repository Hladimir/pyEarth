import sys
import web_server.pyearth_web_server


def main():
    port = 325

    if len(sys.argv) == 2:
        try:
            port = int(sys.argv[1])
            print("The port is %d" % port)
        except Exception as ret:
            print("Error:You must use 'python3 main.py' or 'python3 main.py PORT'")
            return
    # else:
    #     print("Error:You must use 'python3 main.py PORT' or 'python3 main.py'")
    #     return

    wsgi_server = web_server.pyearth_web_server.WSGIServer(port)
    wsgi_server.run_server()


if __name__ == '__main__':
    main()
