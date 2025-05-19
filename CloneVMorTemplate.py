#////////////////////////////////////////////////////////////////////////////
#// ____        _   _                   ____            _       _          //
#//|  _ \ _   _| |_| |__   ___  _ __   / ___|  ___ _ __(_)_ __ | |_        //
#//| |_) | | | | __| '_ \ / _ \| '_ \  \___ \ / __| '__| | '_ \| __|       //
#//|  __/| |_| | |_| | | | (_) | | | |  ___) | (__| |  | | |_) | |_        //
#//|_|    \__, |\__|_| |_|\___/|_| |_| |____/ \___|_|  |_| .__/ \__|       //
#//       |___/         / ___| | ___  _ __   ___         |_|               //
#//                    | |   | |/ _ \| '_ \ / _ \                          //
#//                    | |___| | (_) | | | |  __/                          //
#//__     ____  __      \____|_|\___/|_| |_|\___|          _       _       //
#//\ \   / /  \/  |   ___  _ __  |_   _|__ _ __ ___  _ __ | | __ _| |_ ___ //
#// \ \ / /| |\/| |  / _ \| '__|   | |/ _ \ '_ ` _ \| '_ \| |/ _` | __/ _ \//
#//  \ V / | |  | | | (_) | |      | |  __/ | | | | | |_) | | (_| | ||  __///
#//   \_/  |_|  |_|  \___/|_|      |_|\___|_| |_| |_| .__/|_|\__,_|\__\___|//
#//                                                 |_|       -by Vinny    //
#////////////////////////////////////////////////////////////////////////////

#If this errors out with 403 permission check failed it is not because of that it is because it is missing a required parameter
#Use escape character \ for ! in token id or itll error out ex: vinny@pve\!vinny-windmill

import requests
import urllib3
import argparse

def proxmox_connect(proxmoxhost: str, api_token: str, token_id: str, node: str, vmid: str, newid: str, name: str, pool: str, target: str, storage: str, description: str):
# API Token Authentication URI
    uri = f"https://{proxmoxhost}:8006/api2/json/nodes/{node}/qemu/{vmid}/clone"

    # Headers for authentication
    headers = {
        'Authorization': f'PVEAPIToken={token_id}={api_token}'
    }

    #Data for clone
    data = {
        'newid': newid,
        'node': node,
        'vmid': vmid,
        'name': name,
        'pool': pool,
        'target': target,
        'storage': storage,
        'description': description   
    }

    try:
        # Send the POST request to the Proxmox API
        response = requests.post(uri, headers=headers, data=data, verify=False)

        # Check if the request was successful
        if response.status_code == 200:
        # Print the response in JSON format
            print("Status Code:200(Successful) Response JSON:", response.json())
        else:
        # Print error if request failed
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main(proxmoxhost, api_token, token_id, node, vmid, newid, name, pool, target, storage, description):
    # Function to call proxmox_connect with the parsed arguments
    proxmox_connect(proxmoxhost=proxmoxhost, api_token=api_token, token_id=token_id, node=node, vmid=vmid, newid=newid, name=name, pool=pool, target=target, storage=storage, description=description)

if __name__ == "__main__":
    # Setup argument parser
    parser = argparse.ArgumentParser(description="Windmill Script.")

    # Authentication
    parser.add_argument('--proxmoxhost', type=str, required=True, help='Proxmox hostname')
    parser.add_argument('--token_id', type=str, required=True, help='Proxmox token_id example user@pve!tokenName')
    parser.add_argument('--api_token', type=str, required=True, help='Proxmox API token.')

    # Clone Arguments
    parser.add_argument('--vmid', type=str, required=True, help='Proxmox virtual machine ID number of template you\'re copying.')  # required
    parser.add_argument('--newid', type=str, required=True, help='New proxmox virtual machine ID number.')  # required
    parser.add_argument('--node', type=str, required=True, help='The cluster node name.')  # required
    parser.add_argument('--pool', type=str, required=True, help='Pool for the proxmox virtual machine.')  # optional
    parser.add_argument('--name', type=str, required=False, help='New proxmox virtual machine ID name.')  # optional
    parser.add_argument('--target', type=str, required=False, help='Target pve #.')  # optional
    parser.add_argument('--storage', type=str, required=False, help='Storage to use.')  # optional
    parser.add_argument('--description', type=str, required=False, help='Description.')  # optional

    # Parse the arguments
    args = parser.parse_args()

    # Call the main function with parsed arguments
    main(proxmoxhost=args.proxmoxhost, api_token=args.api_token, token_id=args.token_id, node=args.node, vmid=args.vmid, newid=args.newid, name=args.name, pool=args.pool, target=args.target, storage=args.storage, description=args.description)
