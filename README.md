# pyEarth

> 请在Python3下运行

pyEarth is a mini TCP Web server, for research and learning.

pyEarth 是一款支持 WSGI 协议的小型 TCP Web 服务器，可以用来研究 Web 服务器原理.

## 环境安装

```bash
$ git clone https://github.com/Hladimir/pyEarth.git
```

## 配置运行

进入项目目录,

```bash
$ python3 main.py
```

默认端口为 `325` ，您可以通过

```bash
$ python3 main.py 7788
```

指定端口运行

浏览器访问 http://127.0.0.1:325/ 查看运行效果

## 目录解释
`web_server` 目录下为 pyEarth Web服务器 核心文件

`web_frame` 目录下为 pyEarth Web框架 核心文件

pyEarth Web服务器 支持 `WSGI` 协议，理论上只要满足 `WSGI` 协议的 Web框架 就可配合 pyEarth 运行。

`static_resource` 目录下为静态资源

## 最后
您觉得项目**太烂**，可以通过
```bash
$ cd ../
$ rm -rf pyEarth-master
```
进行删除

**感谢品尝！**