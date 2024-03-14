# Ensemble Installation Instructions

Note: These instructions are not complete yet.

[Windows](#windows-installation)

[MacOS](#macos-installation)

[Linux/Unix](#linuxunix-installation)


___
### Windows Installation:
1. Download Python: https://www.python.org/downloads/windows/
2. Add Python to your PATH environment variables: https://realpython.com/add-python-to-path/#how-to-add-python-to-path-on-windows
3. Ensure `pip` is installed on your computer by running `pip -V` in the CLI. If not, follow the download instructions for pip here: https://pip.pypa.io/en/stable/installation/
4. Clone this repo onto your machine.
6. You can now create a Ensemble file with the .ens extension and run `ensemble <filename>.ens`5. Run `pip install .` while in "\ensemble" director
y.


___
### MacOS Installation:
1. Download Python: https://www.python.org/downloads/macos/
2. Add Python to your PATH environment variables: https://realpython.com/add-python-to-path/#how-to-add-python-to-path-on-linux-and-macos
3. Ensure `pip` is installed on your computer by running `pip -V` in the CLI. If not, follow the download instructions for pip here: https://pip.pypa.io/en/stable/installation/
4. Clone this repo onto your machine.
6. You can now create a Ensemble file with the .ens extension and run `ensemble <filename>.ens`5. Run `pip install .` while in "/ensemble" director
y.


___
### Linux/UNIX Installation:
___
1. According to the Python documentation, "Python comes preinstalled on most Linux distributions, and is available as a package on all others" (see https://docs.python.org/3/using/unix.html). Confirm Python is installed by running `python3 --version` in your terminal. If not installed, follow these directions: https://www.python.org/downloads/source/
2. Confirm Python is added to your PATH by running `echo $PATH | grep Python`. If not added to the path, follow the instructions here: https://realpython.com/add-python-to-path/#how-to-add-python-to-path-on-linux-and-macos
3. Ensure `pip` is installed on your computer by running `pip -V` in the CLI. If not, run `sudo apt update; sudo apt install python3-pip`.
4. Ensure `git` is installed on your computer by running `git version` in the terminal. If not, follow these instructions: https://github.com/git-guides/install-git#install-git-on-linux
5. Clone this repo onto your machine by running `git clone https://github.com/dhodgdon/ensemble.git`.
6. Run `cd ensemble` to change directories to the top-level directory of Ensemble.
7. Run `pip install .`.
8. You may receive some warnings about scripts being installed in a folder names something like `/home/<username>/.local/bin`. If you do, run `export PATH=/home/<username>/.local/bin:$PATH` with your username substituted.

You can now create a Ensemble file with the .ens extension and run `ensemble <your_file_name>.ens` from the console!