import requests             #import thư viện Requests
import json                 #import thư viện 
import meraki_info
#import meraki

def get_network_device_inventory_organizaton():
    url = meraki_info.base_url + '/organizations/1154033/inventoryDevices'
    header = {"X-Cisco-Meraki-API-Key": meraki_info.api_key}
    resp = requests.get(url,headers=header)
    data = resp.json()
    print (json.dumps(data, indent=4))
    return data
get_network_device_inventory_organizaton()

def get_network_device_not_used():
    device = get_network_device_inventory_organizaton()
    device_list = device
    for items in device_list:
        if items["networkId"] is None:
            print(json.dumps(items, indent=4))        
get_network_device_not_used()