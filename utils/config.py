import configparser

def read_config():
    """
    Reads the configuration file and returns a dictionary containing the key-value pairs.
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    return dict(config['DEFAULT'])

def write_config(data):
    """
    Writes the given key-value pairs to the configuration file.
    """
    config = configparser.ConfigParser()
    config['DEFAULT'] = data
    with open('config.ini', 'w') as config_file:
        config.write(config_file)

def update_config(key, value):
    """
    Updates the value of the given key in the configuration file.
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    config.set('DEFAULT', key, value)
    with open('config.ini', 'w') as config_file:
        config.write(config_file)

def delete_config(key):
    """
    Deletes the given key from the configuration file.
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    config.remove_option('DEFAULT', key)
    with open('config.ini', 'w') as config_file:
        config.write(config_file)
