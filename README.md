# Password Manager App #

An app to save websites and their passwords locally and if needed generate a password to use for that site

## Usage ##

From the terminal in the project dir
    Run pip install -r requirements.txt

    then run  python  main.py

The data is saved to a data.txt file in the project dir

### Class ###

    1)SaveData
        In save_data.py
        Functions:
            i)get_data - Processes data from the Tkinter Entry filed in main and formats it into a dictionary of website, email and password keys
            ii)save_data_file - Save the processed data to a text file
            iii)clear_data - Clear password and website fields after saving it
            iv) is_website_or_password_empty - Checks whether both password and websites fields have been filled and returns a boolean. True for missing field and False for all fields filled
            v) is_ready_to_save - Confirms a user is ready to save data using dialog
            vi)save_data_to_json - Create a json file if it does not exist and save the data to it else read the contents of the json file , update then save it.
    2)Password
        In password.py
        Functions:
            i)generate_password - Create a password that includes letters , numbers and symbols, fill it in the password_field and copy it to clipboard
