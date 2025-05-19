#//////////////////////////////////////////////////////////////////////
#// ____        _   _                   ____            _       _    //
#//|  _ \ _   _| |_| |__   ___  _ __   / ___|  ___ _ __(_)_ __ | |_  //
#//| |_) | | | | __| '_ \ / _ \| '_ \  \___ \ / __| '__| | '_ \| __| //
#//|  __/| |_| | |_| | | | (_) | | | |  ___) | (__| |  | | |_) | |_  //
#//|_|___ \__, |\__|_|_|_|\___/|_| |_| |____/ \___|_|_ |_| .__/ \__| //
#// / ___||___/_ __  / _(_) __ _ _   _ _ __ __ _| |_(_) _|_| _ __    //
#//| |   / _ \| '_ \| |_| |/ _` | | | | '__/ _` | __| |/ _ \| '_ \   //
#//| |__| (_) | | | |  _| | (_| | |_| | | | (_| | |_| | (_) | | | |  //
#// \____\___/|_| |_|_| |_|\__, |\__,_|_|  \__,_|\__|_|\___/|_| |_|  //
#//                        |___/                         By- Vinny   //
#//////////////////////////////////////////////////////////////////////

import random
import requests
import argparse
import urllib3
urllib3.disable_warnings()

#API Authentication and POST request
def proxmox_connect(proxmoxhost: str, api_token: str, token_id: str, node: str, vmid: int, name: str, description: str, ipconfig: str, autostart: bool, nameserver: str, onboot: bool, sockets: int, ciuser: str, cipassword: str):
# API Token Authentication URI
    uri = f"https://{proxmoxhost}:8006/api2/json/nodes/{node}/qemu/{vmid}/config"

    # Headers for authentication
    headers = {
        'Authorization': f'PVEAPIToken={token_id}={api_token}'
    }

    #Data for clone
    data = {
        #required
        'node': node,
        'vmid': vmid,
        #optional
        'cores': cores,
        'ipconfig': ipconfig,
        'name': name,
        'description': description,
        'autostart': autostart,
        'nameserver': nameserver,
        'onboot': onboot,
        'sockets': sockets,
        'ciuser': ciuser,
        'cipassword': cipassword
        'newid': newid
    }

    try:
        # Send the POST request to the Proxmox API
        response = requests.post(uri, headers=headers, data=data, verify=False)

        # Check if the request was successful
        if response.status_code == 200:
        # Print the response in JSON format
            print("API POST Request Status Code:200(Successful) Response JSON:", response.json())
        else:
        # Print error if request failed
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"API POST Status Code Failed An error occurred: {e}")

#Primary function for execution of all instructions
def main(proxmoxhost, api_token, token_id, node, vmid, name, description, ipconfig, autostart, nameserver, onboot, sockets, cores, ciuser, cipassword):
    
    #Function to call proxmox_connect with the parsed arguments
    proxmox_connect(proxmoxhost=proxmoxhost, api_token=api_token, token_id=token_id, node=node, vmid=vmid, node=node, name=name, description=description, ipconfig=ipconfig, autostart=autostart, nameserver=nameserver, onboot=onboot, sockets=sockets, cores=cores, ciuser=ciuser, cipassword=cipassword)

if __name__ == "__main__":

    # Setup argument parser
    parser = argparse.ArgumentParser(description="Windmill Script.")

    # Authentication
    parser.add_argument('--proxmoxhost', type=str, required=True, help='Proxmox hostname')
    parser.add_argument('--token_id', type=str, required=True, help='Proxmox token_id example user@pve!tokenName tip: use back slash prior to typing an escape character such as exclamation mark')
    parser.add_argument('--api_token', type=str, required=True, help='Proxmox API token.')

    # Required Config Arguments
    parser.add_argument('--vmid', type=int, required=True, help='Proxmox virtual machine ID number of template you\'re copying.')
    parser.add_argument('--node', type=str, required=True, help='The cluster node name.')
    
    # Optional Config Arguments
   
    parser.add_argument('--name', type=str, required=False, help='New proxmox virtual machine ID name.')
    parser.add_argument('--description', type=str, required=False, help='Description.')
    parser.add_argument('--ipconfig', type=str, required=False, help='cloud-init: Specify IP addresses and gateways for the corresponding interface.')
    parser.add_argument('--autostart', type=bool, required=False, help='Automatic restart after crash.')
    parser.add_argument('--nameserver', type=str, required=False, help='cloud-init: Sets DNS server IP address for a container. Create will automatically use the setting from the host if neither searchdomain nor nameserver are set.')
    parser.add_argument('--onboot', type=bool, required=False, help='Specifies whether a VM will be started during system bootup.')
    parser.add_argument('--sockets', type=str, required=False, help='Number of CPU sockets.')
    parser.add_argument('--cores', type=str, required=False, help='Number of CPU cores.')
    parser.add_argument('--ciuser', type=str, required=False, help='cloud-init: User name to change ssh keys and password for instead of the image\'s configured default user.')
    parser.add_argument('--cipassword', type=str, required=False, help='cloud-init: Password to assign the user. Using this is generally not recommended. Use ssh keys instead.')

    # Parse the arguments
    args = parser.parse_args()

    # Call the main function with parsed arguments
    main(proxmoxhost=args.proxmoxhost, token_id=args.token_id, api_token=args.api_token, vmid=args.vmid, node=args.node, name=args.name, description=args.description, ipconfig=args.ipconfig, autostart=args.autostart, nameserver=args.nameserver, onboot=args.onboot, sockets=args.sockets, cores=args.cores, ciuser=args.ciuser, cipassword=args.cipassword)