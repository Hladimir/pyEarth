import socket
import re
import multiprocessing
import web_frame.pyearth_web_frame


class WSGIServer(object):
    """
    pyEarth 是一款满足 WSGI 规范的小型 Web 服务器，用于研究 Web 服务器的原理
    """

    def __init__(self):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.tcp_server_socket.bind(("", 7890))

        self.tcp_server_socket.listen(128)

    def service_client(self, new_socket):
        """
        处理请求，返回数据
        :param new_socket: 浏览器发出的 HTTP 请求
        :return:
        """

        request = new_socket.recv(1024).decode("utf-8")

        request_lines = request.splitlines()

        file_name = ""
        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        if ret:
            file_name = ret.group(1)
            if file_name == "/":
                file_name = "/demo.html"

        if not file_name.endswith(".py"):

            # 请求静态资源
            try:
                f = open("./static_resource" + file_name, "rb")
            except:
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                response += "file not found"
                new_socket.send(response.encode("utf-8"))
            else:
                html_content = f.read()
                f.close()
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"

                new_socket.send(response.encode("utf-8"))
                new_socket.send(html_content)
        else:
            env = dict()
            env['PATH_INFO'] = file_name

            body = web_frame.pyearth_web_frame.application(env, self.set_response_header)

            header = "HTTP/1.1 %s\r\n" % self.status
            for temp in self.headers:
                header += "%s:%s\r\n" % (temp[0], temp[1])
            header += "\r\n"

            response = header + body

            new_socket.send(response.encode("utf-8"))

        new_socket.close()

    def set_response_header(self, status, headers):
        """
        用来接收框架返回的 Headers
        :param status: 框架返回的状态码
        :param headers: 框架返回的 Headers
        :return:
        """

        self.status = status
        self.headers = [('server', 'pyearth v0.0.2')] + headers

    def run_server(self):

        while True:
            new_socket, client_addr = self.tcp_server_socket.accept()

            p = multiprocessing.Process(target=self.service_client,
                                        args=(new_socket,))
            p.start()

            new_socket.close()

        self.tcp_server_socket.close()


def main():
    wsgi_server = WSGIServer()
    wsgi_server.run_server()


if __name__ == '__main__':
    main()
