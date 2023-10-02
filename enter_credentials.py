'''This file will automatically enter your credentials into wow for you
        - Be sure to edit the confif.yml with the correct details!!
'''
import yaml, os



def load_config(config_file='config.yml')->tuple:
    '''
        This function loads the given config file and returns the username and password in a tuple

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



print(load_config())



  


