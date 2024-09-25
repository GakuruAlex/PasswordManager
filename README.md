# Password Manager App #

An app to save websites and their passwords locally and if needed generate a password to use for that site

## Usage ##

From the cli
    Run pip install -r requirements.txt
    Run python  main.py from the project dir

The data is saved to a data.txt file in the project dir

### Class ###

    1)SaveData
        In save_data.py
        Functions:
            i)get_data - Processes data from the Tkinter Entry filed in main and formats it into a dictionary of website, email and password keys
            ii)save_data_file - Save the processed data to a text file
            iii)clear_data - Clear password and website fields after saving it
