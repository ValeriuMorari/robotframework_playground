import yaml
import argparse
from yaml.loader import SafeLoader
from robot import run

arg_parser = argparse.ArgumentParser(description='Arg parser..')

arg_parser.add_argument('-test',
                        dest='test',
                        help="test that u wanna run",
                        required=True)

args = arg_parser.parse_args()
args = vars(args)

print("Detected args: %s", args)

# Open the file and load the file
with open('configuration.yaml') as f:
    configuration_data = yaml.load(f, Loader=SafeLoader)
# 'Tests/LaunchBrowser.robot'
run(args['test'], **configuration_data.get('cli_settings', {}))
