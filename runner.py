import yaml
from yaml.loader import SafeLoader
from robot import run

# Open the file and load the file
with open('configuration.yaml') as f:
    configuration_data = yaml.load(f, Loader=SafeLoader)

run('Tests/LaunchBrowser.robot', **configuration_data.get('cli_settings', {}))
