from . import b  # relative import

print('you imported package code - module a')


def A():
    print('A')


b.B()  # function from b.py
