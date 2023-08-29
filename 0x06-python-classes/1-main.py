#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    pass
root@de42b6af4b03:/0x06-python-classes# emacs 1-main.py
root@de42b6af4b03:/0x06-python-classes# cat 1-main.py
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
