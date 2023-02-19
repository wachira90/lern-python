# lern-python
lern-python

## upgrade pip 

````
python.exe -m pip install --upgrade pip
````

## use virtual env

````
virtualenv env
````

### WINDOWS

````
env\Scripts\activate
````

### LINUX

````
source env\bin\activate
````

## Install Pip With Get-Pip.Py

````
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python get-pip.py
````

## check version

````
pip --version

pip 22.0.4 from D:\python37\lib\site-packages\pip (python 3.7)
````

## check site package

```
python -m site

python -c "import site; print(site.getsitepackages())"
```

