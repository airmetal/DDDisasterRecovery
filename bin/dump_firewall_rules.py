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

network_domains = client.ex_list_network_domains()

all_data = {}
for network_domain in network_domains:
    firewall_rules = client.ex_list_firewall_rules(network_domain)
    all_rules = []
    for firewall_rule in firewall_rules:
        temp_dict = {}
        temp_dict['id'] = firewall_rule.id
        temp_dict['name'] = firewall_rule.name
        temp_dict['action'] = firewall_rule.action
        temp_dict['ip_version'] = firewall_rule.ip_version
        temp_dict['protocol'] = firewall_rule.protocol
        temp_dict['enabled'] = firewall_rule.enabled
        temp_dict['source'] =  {'any_ip': firewall_rule.source.any_ip,
                                'ip_address': firewall_rule.source.ip_address,
                                'ip_prefix_size': firewall_rule.source.ip_prefix_size,
                                'port_begin': firewall_rule.source.port_begin,
                                'port_end': firewall_rule.source.port_end,
                               }
        temp_dict['destination'] =  {'any_ip': firewall_rule.destination.any_ip,
                                'ip_address': firewall_rule.destination.ip_address,
                                'ip_prefix_size': firewall_rule.destination.ip_prefix_size,
                                'port_begin': firewall_rule.destination.port_begin,
                                'port_end': firewall_rule.destination.port_end,
                               }
        temp_dict['location'] = firewall_rule.location.id
        temp_dict['status'] = firewall_rule.status
        all_rules.append(temp_dict)
    all_data[network_domain.id] = all_rules

print(json.dumps(all_data, indent=4, separators=(',', ': ')))
