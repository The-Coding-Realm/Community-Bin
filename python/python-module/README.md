# Author info
I'm Big Brain Mossy#9139 or often called mossy, I like coding in python.

# Description
This is an example package I made, you may use it as you want. I also write this on my own or by copy pasting my own existing code.

# Dependencies
- [`setuptools`](https://pypi.org/project/setuptools/)
- [`wheel`](https://pypi.org/project/wheel/)
- [`twine`](https://pypi.org/project/twine/)

# How to use
First, go to `setup.py`. I have leave some note there to help you, next go to mymodule folder (if you havent change the name, if yu does then go to the folder you have renamed) and open `__init__.py`. I also have leave some note there for you.

After you done run this command in the setup.py folder:
`python setup.py bdist_wheel`
This command will build your package file.
It should be generating a file named dist, inside it will be a .whl file or so. That is your package. you can install it using `pip install /path/to/wheelfile.whl` or publish it using twine with [`this`](https://twine.readthedocs.io/en/latest/#twine-upload) command.

# References
- [`How to make python package by Kia Eisinga`](https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f)
- [`discord.py setup file`](https://github.com/Rapptz/discord.py/blob/master/setup.py), the code owned by Rapptz but I just use it as reference.