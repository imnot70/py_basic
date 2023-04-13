#!/usr/bin/env python3
# coding=utf-8

def application(environ, start_response):
    # print(dir(environ))
    # print(environ['PATH_INFO'])
    # print(type(environ))
    for x in environ:
        print('[%s] = [%s]\n'%(x,environ[x]))
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']

