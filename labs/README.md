# Running thelabs


[Python >=3.7](https://www.python.org/downloads/)
[VS Code](https://code.visualstudio.com/)
[Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
[Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
[Git](https://git-scm.com/downloads)



## Installing

```windows
git clone https://github.com/bathcat/python_foundations
cd python_foundations/labs
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

For *nix:
```
git clone https://github.com/bathcat/python_foundations
cd python_foundations/labs
python3 -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
```

Test it out:
```
python .\src\A.1.HelloBlinky\startingpoint\mood.py
```


## Hooking up to the PI


### With Visual Studio Code




# Notes

## On visual studio code:
  * https://code.visualstudio.com/docs/python/python-tutorial
  * https://binx.io/blog/2020/03/05/setting-python-source-folders-vscode/
  * https://code.visualstudio.com/docs/python/environments


## Installing




# https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

Install venv like this:

sudo apt-get install python3-pip python3-venv idle3
git clone https://github.com/bathcat/python_foundations
cd python_foundations/labs
python3 -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt  // It's safe to ignore the warnings.

# Activation
https://stackoverflow.com/questions/9554087/setting-an-environment-variable-in-virtualenv

## Emulation

https://www.makeuseof.com/tag/emulate-raspberry-pi-pc/
