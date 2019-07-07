import sys
import configparser


def get_config():
    configparser.ConfigParser(allow_no_value=True)
    config_path = sys.argv[1] if len(sys.argv) > 1 else '../config.ini'
    config_parser = configparser.ConfigParser()
    config_parser.read(config_path)
    return config_parser


CONFIG = get_config()
