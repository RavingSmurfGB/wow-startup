'''This file will automatically enter your credentials into wow for you
        - Be sure to edit the confif.yml with the correct details!!
'''
import yaml, os, pyautogui, time, subprocess



def load_config(config_file='config.yml')->tuple:
    ''' This function loads the given config file and returns the username and password in a tuple

        To call this function:
            load_config()
            load_config(config_file = "example_config.yml")

        Returns:
            ('example_user', 'example_password')
    '''
    if os.path.isfile(config_file):
        with open(config_file, 'r') as config:
            config_dict = yaml.safe_load(config)
        username = config_dict["username"]
        password = config_dict["password"]

        return (username, password)
    else:
        raise FileNotFoundError


def detect_application(application_name:str)->bool:
    '''This function detects if the given application is running and will return bool
            This function was written for Windows and linux compatibility may vary
            If the name does not match, including capital letters it will fail
    
        To call this function: 
            detect_application(application_name="WowClassic.exe")

    '''
    processes = subprocess.Popen('tasklist', stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()[0].decode().splitlines()
    for process in processes:
        if application_name in process:
            return True
        

def enter_credentials():
    ''' This function enters your username and password into wow
            It will call detect_application() to ensure wow is running first
            
    '''
    credentials = load_config(config_file="config.yml")
    username = credentials[0]
    password = credentials[1]

    # Wait untill we detect wow:
    while not detect_application(application_name="WowClassic.exe"):
        time.sleep(0.5)

    # When wow is dected we wait 7 seconds
    time.sleep(7)

    # Then enter the credentials
    pyautogui.write(username)
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.write(password)
    pyautogui.press('enter')


if __name__ == "__main__":
    enter_credentials()
    
