Exercice about creation of a python package

etap 1 create new file "__init.py__" -> python consider it's a package

etap 2 create a setup.py 

gg package is create now you can install it by doing this commands in the following order:

python setup.py sdist bdist_wheel

pip install ./dist/ft_package-0.0.1.tar.gz

pip install ./dist/ft_package-0.0.1-py3-none-any.whl

Now you can try the tester with "python tester.py"

if you want to uninstall --> pip uninstall ft_package

easy