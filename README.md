# GD
Step 1 : Prerequisites
******************
Make sure all prerequisites are installed and configured. Please refer to https://code.visualstudio.com/docs/python/tutorial-django#_prerequisites

Step 2 : Clone repository on your machine
***********************************
Run the following command inside your folder to clone the repository on your computer
>git clone "https://github.com/pallavitilloo/GD.git"
This will create a folder "GD" in your computer at the location where you ran the command.

Step 3 : Create project environment
******************************
Open the GD project folder in Visual Studio Code
On your file system, create a project folder GD.
Now in VS Code, open Terminal and use the following command (as appropriate to your computer) to create a virtual environment named env based on your current interpreter:
>sudo apt-get install python3-venv   (if required for macOS)
>python3 -m venv env (for macOS/Linux)
>python -m venv env (for Windows)
This should create 'env' folder in your project folder.

Step 4 : Select interpreter
**********************
In VS Code, go to settings -> Command Palette. Select the option 'Python: Select interpreter'.
In the list, select the interpreter under ".env\Scripts\Python.exe"
The selected environment appears at the bottom left side of the VS Code status bar, and notice the "(env)" indicator that tells you that you're using a virtual environment

Step 5 : Install Django
******************
Install Django in the virtual environment by running one of the following commands in the VS Code Terminal:
>python -m pip install django
It might show message "Requirement already satisfied...".

Step 6 : Start the server
********************
Start the Django's development server using the command 
>python manage.py runserver

For details, please refer to the URL https://code.visualstudio.com/docs/python/tutorial-django
