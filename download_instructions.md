# Ensemble Installation Instructions

[Windows](#windows-installation)

[MacOS](#macos-installation)

[Debian/Ubuntu Linux](#linuxunix-installation)


___
### Windows Installation:
1. Download Python 3+: https://www.python.org/downloads/windows/
2. Add Python to your PATH environment variables: https://realpython.com/add-python-to-path/#how-to-add-python-to-path-on-windows
3. Ensure `pip` is installed on your computer by running `pip -V` in the CLI. If not, follow the download instructions for pip here: https://pip.pypa.io/en/stable/installation/
4. Ensure `git` is installed on your computer by running `git version` in the terminal. If not, follow these instructions: https://github.com/git-guides/install-git#install-git-on-windows
5. Change folders to the folder where you would like to download Ensemble; then, clone this repo onto your machine by running `git clone https://github.com/dhodgdon/ensemble.git`.
6. Run `cd ensemble` to change directories to the top-level directory of Ensemble.
7. Run `pip install .`.
8. [Run Ensemble!](#time-to-run-ensemble)

___
### MacOS Installation:

1. Download Python 3+ (if given the option, include pip3 in the download): https://www.python.org/downloads/macos/
2. Python should be added to your PATH variables. Run `python3 --version` to confirm your system can find the correct version of Python. If not, add Python to your PATH environment variables: https://realpython.com/add-python-to-path/#how-to-add-python-to-path-on-linux-and-macos
3. Ensure `pip3` is installed on your computer by running `pip3 -V` in the CLI. If not, follow the download instructions for pip here: https://pip.pypa.io/en/stable/installation/
4. Ensure `git` is installed on your computer by running `git version` in the terminal. If not, follow these instructions: https://github.com/git-guides/install-git#install-git-on-mac
5. Change folders to the folder where you would like to download Ensemble; then, clone this repo onto your machine by running `git clone https://github.com/dhodgdon/ensemble.git`.
6. Run `cd ensemble` to change directories to the top-level directory of Ensemble.
7. Run `pip3 install .`.
8. [Run Ensemble!](#time-to-run-ensemble)

___
### Debian/Ubuntu Linux Installation:

1. According to the Python documentation, "Python comes preinstalled on most Linux distributions, and is available as a package on all others" (see https://docs.python.org/3/using/unix.html). Confirm Python 3+ is installed by running `python3 --version` in your terminal. If not installed, follow these directions: https://www.python.org/downloads/source/
2. Confirm Python is added to your PATH by running `echo $PATH | grep Python`. If not added to the path, follow the instructions here: https://realpython.com/add-python-to-path/#how-to-add-python-to-path-on-linux-and-macos
3. Ensure `pip` is installed on your computer by running `pip -V` in the CLI. If not, run `sudo apt update; sudo apt install python3-pip`.
4. Ensure `git` is installed on your computer by running `git version` in the terminal. If not, follow these instructions: https://github.com/git-guides/install-git#debianubuntu
5. Change folders to the folder where you would like to download Ensemble; then, clone this repo onto your machine by running `git clone https://github.com/dhodgdon/ensemble.git`.
6. Run `cd ensemble` to change directories to the top-level directory of Ensemble.
7. Run `pip install .`.
8. You may receive some warnings about scripts being installed in a folder names something like `/home/<username>/.local/bin`. If you do, run `export PATH=/home/<username>/.local/bin:$PATH` with your username substituted.
9. Run `sudo apt-get install timidity`. 
10. Copy the code below and run it in a Python script (any file with the file extension ".py") or in the Python REPL by typing `python3` in the command line.

    ```python
    import music21

    # Replace '/path/to/application' with the actual path to your MIDI application. Mine was located at '/usr/bin/timidity'. You can run 'which timidity' to find its path. 
    midi_application_path = '/path/to/application'
    music21.environment.set('midiPath', midi_application_path)
    ```

11. [Run Ensemble!](#time-to-run-ensemble)

___
### Time to Run Ensemble!
You can now create a Ensemble file with the .ens extension and run `ensemble <your_file_name>.ens` from the console! (Note: The `ensemble` command will use the app your system has set as its MIDI player to play your song.)

Change directories into "/ensemble/examples" by running `cd examples` when in the Ensemble top-level directory, and try running some of the example Ensemble programs there.