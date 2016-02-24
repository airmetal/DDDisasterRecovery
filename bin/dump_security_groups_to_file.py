#!/usr/bin/env python
import click
from nsx.client import NSXClient
import json
import logging
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

logging.basicConfig()

@click.command()
@click.option('--datacenter', required=True, prompt='Datacenter to Dump: ', help='This is the datacenter to dump NSX security groups for')
@click.option('--configFile', type=click.File('rb'), default='./nsx_config', help='The config file to use for credentials/endpoints')
@click.argument('output', type=click.File('wb'))
def nsx(datacenter, configfile, output):
    config = configparser.ConfigParser()
    config.readfp(configfile)
    user = config.get(datacenter, 'user')
    password = config.get(datacenter, 'password')
    endpoint = config.get(datacenter, 'endpoint')
    client = NSXClient(user, password, endpoint=endpoint)
    security_groups = client.list_security_groups()
    output.write(json.dumps(security_groups, sort_keys=True, indent=4, separators=(',', ': ')))

if __name__ == '__main__':
    nsx()
