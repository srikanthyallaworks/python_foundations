<h1 style='font-size:250%;'>Python Foundations: Setup Guide</h1>



## Development Tools: Minimal
At a minimum you just need: 
1. A recent(ish) version of Python 3 
2. Your favorite text editor


However, the tools below are very nice to have:
* [Python >=3.7](https://www.python.org/downloads/)
* [VS Code](https://code.visualstudio.com/)
* [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* [Git](https://git-scm.com/downloads)


&nbsp;

## Development Tools: Minimal

You don't need this stuff, but it's nice to have for running tests, linting, and etc. There's a detailed discussion [here](https://code.visualstudio.com/docs/remote/containers).

Install this stuff--
* [Git](https://git-scm.com/downloads)
* [Docker Desktop](https://www.docker.com/products/docker-desktop)
* [VSCode](https://code.visualstudio.com/)
  -[Remote Development Extensions](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

(I had to feff around with WSL (Windows Subsystem for Linux) and reboot a couple times, but the install pages had reliable instructions.)

&nbsp;

# Download and open the project.

Fire up a terminal and do something like this:
```
cd c:\
mkdir workspace
cd workspace
git clone https://github.com/bathcat/python_foundations
cd python_foundations
code .
```

If everything goes right, VSCode will read its configuration files and offer to open your project in a container.

Choose to reopen and you're all set up! Dig around if you want.
