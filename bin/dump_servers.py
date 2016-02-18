#!/usr/bin/env python

from libcloud.compute.drivers.dimensiondata import DimensionDataNodeDriver
from libcloud.common.dimensiondata import DEFAULT_REGION
import argparse
import json

parser = argparse.ArgumentParser(description='Dumppppp')
parser.add_argument('--user')
parser.add_argument('--password')
parser.add_argument('--region', default=DEFAULT_REGION)
args = parser.parse_args()

client = DimensionDataNodeDriver(args.user, args.password, args.region)

nodes = client.list_nodes()


node_list = []
#We need to convert a List of Nodes to a list of dictionarys.  Silly I know,
#The other option is to add .to_json methods or write a json parser for node objects
for node in nodes:
    temp_dict = {}
    temp_dict['id'] = node.id
    temp_dict['name'] = node.name
    temp_dict['public_ips'] = node.public_ips
    temp_dict['private_ips'] = node.private_ips
    temp_dict['memoryMb'] = node.extra['memoryMb']
    temp_dict['cpu'] = {'cpuCount': node.extra['cpu'].cpu_count,
                        'cores_per_socket': node.extra['cpu'].cores_per_socket,
                        'performace': node.extra['cpu'].performance
                       }
    temp_dict['OS'] = node.extra['OS_displayName']
    node_list.append(temp_dict)

print(json.dumps(node_list, indent=4, separators=(',', ': ')))
