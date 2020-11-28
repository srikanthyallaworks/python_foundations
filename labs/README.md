# Running thelabs



[Python >=3.7](https://www.python.org/downloads/)
[VS Code](https://code.visualstudio.com/)
[Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
[Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)


[Git](https://git-scm.com/downloads)




## Installing

```shell
git clone https://github.com/bathcat/python_foundations
cd python_foundations/labs
python3 -m venv .venv
```

For *nix:
```
source ./.venv/bin/activate
```

For Windows:
```
.\env\Scripts\activate
```

Finally:
```
pip install -r requirements.txt
```


## Using Visual Studio Code



## Using Other Stuff


On Linux/MacOS
```shell
cd python_foundations\labs
export PYTHONPATH="./fakes/"
python ./src/E1.FizzBuzzBlinky/complete/main.py 
```

On Windows 10:
```pwsh
$Env:PYTHONPATH = '.\fakes\'
python .\src\E1.FizzBuzzBlinky\startingpoint\main.py
```


## Hooking up to the PI


### With Visual Studio Code




