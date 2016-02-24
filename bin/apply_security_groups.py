#!/usr/bin/env python
import click
from nsx.client import NSXClient
import json
from requests import HTTPError
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

try:
    import configparser
except ImportError:
    import ConfigParser as configparser
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
@click.command()
@click.option('--datacenter', required=True, prompt='Datacenter to Dump: ', help='This is the datacenter to dump NSX security groups for')
@click.option('--configFile', type=click.File('rb'), default='./nsx_config', help='The config file to use for credentials/endpoints')
@click.option('--go', help='By default this is a dry run, these will actually do the puts', default=False, is_flag=True)
@click.argument('input', type=click.File('rb'))
def nsx(datacenter, configfile, go, input):
    config = configparser.ConfigParser()
    config.readfp(configfile)
    user = config.get(datacenter, 'user')
    password = config.get(datacenter, 'password')
    endpoint = config.get(datacenter, 'endpoint')
    client = NSXClient(user, password, endpoint=endpoint)

    security_groups = json.load(input)
    if not go:
        click.secho('This is a dryrun', fg='yellow')

    for security_group in security_groups:
        click.secho("Security group {}".format(security_group['objectId']))
        if not security_group.has_key('member'):
            click.secho("Security group has no members skipping...")
            continue
        if isinstance(security_group['member'], dict):
            add_member(client, security_group['objectId'], security_group['member']['objectId'], go)
        else:
            for member in security_group['member']:
                add_member(client, security_group['objectId'], member['objectId'], go)


def add_member(client, group, member, go):
    if not go:
        click.secho("Would have made call for {} and {}".format(group, member), fg='green')
    else:
        try:
            output = client.add_member_to_security_group(group, member)
            click.secho("SUCCESS: {} {}".format(group, member), fg='green')
        except HTTPError:
            pass
if __name__ == '__main__':
    nsx()
