# wow-startup
 The following repo is how to automatically enter credentials into the classic 2.5.3 client 

This project does store credentials in plain text for now - use this if security is not your priority

This project was written for windows and for 2.5.3 hermes proxy.

## Install
0. Ensure python is downloaded and installed.
1. Then ensure that "Remember Account Name" is disabled in the game logon screen
2. Navigate to your Wow directory
3. To download the project, Click above from the Green Dropdown, then download Zip
4. Extract the files, not the folder into your Wow directory
5. Open a terminal in this location and then install the requirements with:
```
pip install -r requirements.txt
```
6. Ammend the config.yml file with your credentials.
7. Edit the file "Start WoW TBC.bat" and add the following to the top! - Ensure it is before everything!
```bat
start enter_credentials.pyw
```
8. Open the game how you would normally



