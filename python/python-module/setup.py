from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()  # get readme and import it for long description of module, you may delete this if you want to manually write it

setup(
    name='MyModule',  # Your module name
    packages=find_packages(include=['Mymodule']),  # Your module file
    version='0.1.0',  # module version
    description='My module made with python!',  # module short description
    long_description=long_description,  # module long description
    # if you want to manually write it change the variable to string and type your long description
    long_description_content_type="text/markdown",  # long description file type (in case of this because its .md we use text/markdown)
    url="https://github.com/somone/a_repostory",  # link to your github, this is optional
    author='Me',  # the author of the module, can be more than one
    license='MIT',  # module lisence
    install_requires=[],  # required packages (if there is one)
)