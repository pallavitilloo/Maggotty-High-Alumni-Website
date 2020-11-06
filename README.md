# Maggotty High Alumni Website setup
Steps to set up the project on your computer

## Prerequisites

Make sure all [prerequisites](https://code.visualstudio.com/docs/python/tutorial-django#_prerequisites) are installed and configured.

## Clone the repository
Run the following command inside your folder to clone the repository on your computer
```
git clone "https://github.com/pallavitilloo/GD.git"
```
This will create a folder "GD" in your computer at the location where you ran the command. Open the folder in Visual Studio Code.

## Create virtual environment
In VS Code, open 'Terminal' and use the following command (as appropriate to your computer) to create a virtual environment named env based on your current interpreter:
```
# macOS
sudo apt-get install python3-venv    # if required
python3 -m venv env

# Windows
python -m venv env
```
This will create ENV folder in your project folder.

## Select Interpreter
In VS Code, go to Settings -> Command Palette. Select the option 'Python: Select interpreter'. Select the interpreter under ".env\Scripts\Python.exe".
```
Note that the selected environment appears at the bottom left side of the VS Code status bar. Notice the "(env)" indicator that tells you that you're using a virtual environment
```

## Check Django, if installed
Install Django in the virtual environment by running one of the following commands in the VS Code Terminal. It should show a message "Requirement already satisfied...".
```
python -m pip install django
```


## Start the server
Start the Django's development server using the command 
```
python manage.py runserver
```


