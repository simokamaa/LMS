# ImageSync Installition guidelines to the server

### Here's required technology and languages to get started:

Python 3.10+
Django 5.0+
Git
### Assets compile require the build tools. These libraries are required as below:

Node.js (LTS)
Gulp
Yarn
Install Python#
Python is the programming language that Django is built with. Django is a Python web framework. See What Python version can I use with Django? for details.

### To check if Python is already installed on your system, open your terminal/command prompt and run:

Info: macOS & Linux usually comes with Python pre-installed.
Copy
python --version
If Python is not installed, follow these steps to install it:

### Mac & Windows:
Download Python for macOS from the official website: python.org/downloads
Run the installer and make sure to check the box that says "Add Python to PATH" before clicking "Install Now."
### Linux:
For Linux, you can use your package manager to install Python. For example, on Ubuntu, you can use:

### Use
sudo apt-get update
sudo apt-get install python3
Install PIP#
Info: PIP is automatically installed with Python 2.7.9+ and Python 3.4+
Linux, Mac & Windows:
To check if PIP is already installed on your system, open your terminal/command prompt and run:

### Use
pip --version
Installing Pip using get-pip.py

Download the script, from https://bootstrap.pypa.io/get-pip.py.
Open a terminal/command prompt, cd to the folder containing the get-pip.py file and run:
LINUX
MACOS
WINDOWS
Use
python get-pip.py
Build Assets#
Before running the application we need to build theme assets from full-version/src/ or starter-kit/src/ folder:

Open terminal/command prompt and change directory to src/
Use
cd src
Install dependencies with either one, yarn or npm:
Tip: It's recommended to use YARN over NPM. In a comparison of speed, Yarn is much quicker and faster than most of the npm versions.
Use
## For Yarn
yarn

## For npm
npm install --legacy-peer-deps
You can use below commands to bundle theme assets. The below command will compile all the assets(sass, js, media) to src/assets folder:
Tip: While Django application development, use a "watch" task to automatically compile asset file changes and instantly observe their effects.
Task (yarn or gulp) lists for development build.

### YARN TASK	GULP TASK	DESCRIPTION
yarn watch	gulp watch	Watch files for changes and automatically recompile them when it changed.
yarn build	gulp build	Compile sources and Use assets.
Task (yarn or gulp) lists for production build. It will generate minified assets for production deployment.

### YARN TASK	GULP TASK	DESCRIPTION
yarn build:prod	gulp build --env=production	Run build task in production environment.For more details refer Available Tasks
Run Django#
WARNING: Depending on your PIP and Python installation, you may need to choose between using either pip or pip3, and similarly, for Python, you may need to select between python or python3.
First, ensure you are in the correct directory. You should be in either the "full-version" or "starter-kit" folder. Once you are in the appropriate folder, proceed with the following instructions:

Create a virtualenv:
Use
python -m venv .venv
Activate the virtualenv you have just created:
LINUX
MACOS
WINDOWS
Use
source .venv/bin/activate
Install development requirements:
Use
pip install -r requirements.txt
Apply migrations:
Use
python manage.py migrate
Run application through django development server:
Use
python manage.py runserver
Keep your prompt running by default application is served on http://localhost:8000

To execute the application on a particular IP address(For ex: http://0.0.0.0:8000), include the desired IP address within the `ALLOWED_HOSTS` parameter in the settings.py file.

Copy
python manage.py runserver 0.0.0.0:8000
