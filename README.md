# Flask Series
For a bit of a recap on Flask I decided to do a [Flask Tutprial](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH) by [Corey Schafer](https://www.youtube.com/@coreyms).

## Prerequisites
Python >= 3.12

## Setup

### Virtual Environment
Create & activate virtual environment with following commands in project root directory:
``` console
# For Linux & Mac
python3 -m venv .venv
source .venv/bin/activate

# For Windows
py -m venv .venv
.venv/Scripts/activate
```

### Install Requirements
Run following command to install all python requirements:
``` console
pip install -r requirements.txt
``` 

### Setup & Configure ENV Constants
Create `.env` file using following command in project root directory:
``` console
# For Linux & Mac
touch .env

# For Windows
copy nul .env > nul
```

In newly created file add following constants:

```
### Flask settings ######### 
FLASK_HOST=[host_or_hostname] ; Host to run APP
FLASK_PORT=[port_number] ; Port number to listen
FLASK_DEBUG_MODE=[number] ; 0 = Disable, 1 = Enable, debug mode
```

Replace `[values]` with corresponding values.

For quick local setup you can use the following:
```
### Flask settings ######### 
FLASK_HOST=127.0.0.1 ; localhost
FLASK_PORT=9000
FLASK_DEBUG_MODE=1 ; Debug mode enabled
``` 
Once you run the application you should be able to access the app via a browser with following link: [http://localhost:9000](http://localhost:9000)

### Run app
Use following command to run the app:
``` console
# For Linux & Mac
python3 flask_server.py

# For Windows
py flask_server.py
```