#!/usr/bin/env python
# _*_coding:utf8_*_
# __auth:ChenFan


def Foo(name):
    print('%s去砍材' % name)


# Foo('liyang')
# Foo('laogou')

def login(username):
    if username == 'mumu':
        return 'success'
    else:
        return 'error'


def detail(user):
    print('xxxxxx')


if __name__ == '__main__':
    user = raw_input('请输入用户名：')
    res = login(user)
    if res == 'success':
        detail(user)
    else:
        print('error')
