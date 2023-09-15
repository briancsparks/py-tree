#!/usr/bin/env python3
import configparser

config = configparser.ConfigParser()
config.read('setup.cfg')

# Read metadata section
metadata_name = config.get('metadata', 'name', fallback=None)
metadata_version = config.get('metadata', 'version', fallback=None)

# Read options section
options_install_requires = config.get('options', 'install_requires', fallback=None)

print(f'Metadata Name: {metadata_name}')
print(f'Metadata Version: {metadata_version}')
print(f'Install Requires: {options_install_requires}')

