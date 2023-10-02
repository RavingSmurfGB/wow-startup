# wow-statrup
 The following repo is how to start wow client and maybe server

This project does store credentials in plain text for now - use this if security is not your priority

This project was written for windows and for 2.5.3 hermes proxy.

## Install
0. First ensure that "Remember Account Name" is disabled in the game logon screen
1. Ensure python is downloaded and installed.
2. Navigate to your Wow directory
3. Download the code above and ensure the files are placed inside your Wow directory.
4. Open a terminal in this location and then install the requirements with:
```
pip install -r requirements.txt
```
5. Ammend the config.yml file with your credentials.
6. Edit the file "Start WoW TBC.bat" and add the following to the top! - Ensure it is before everything!
```bat
start enter_credentials.pyw
```
7. Open the game how you would normally



