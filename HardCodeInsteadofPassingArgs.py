import requests
import urllib3
urllib3.disable_warnings()

def proxmox_connect(proxmoxhost: str, api_token: str, token_id: str, node: str, vmid: str, newid: str, name: str, full: bool, pool: str, storage: str, target: str):
# API Token Authentication URI
    uri = f"https://{proxmoxhost}:8006/api2/json/nodes/{node}/qemu/{vmid}/clone"

    # Headers for authentication
    headers = {
        'Authorization': f'PVEAPIToken={token_id}={api_token}'
    }

    #Data for clone
    data = {
        'newid': newid,
        'name': name,
        'full': full,
        'pool': pool,
        'storage': storage,
        'target': target
    }

    try:
        # Send the POST request to the Proxmox API
        response = requests.post(uri, headers=headers, data=data, verify=False)

        # Check if the request was successful
        if response.status_code == 200:
        # Print the response in JSON format
            print("Response JSON:", response.json())
        else:
        # Print error if request failed
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
  
    #Change all these values to your own
  
    # Variables
    node = "node" # Proxmox node (Required) 
    vmid = "vm id"  # VM ID (Required) 
    newid = "vm id" #new VM ID (Required)

    #Authentication (Required)
    proxmoxhost = "yourhost" # Proxmox host address
    api_token = "your api key" # API token
    token_id = "your token ID" # Proxmox token ID

    #Optional Configurations
    name = "name" #New VM name (Optional)
    full = "full" #Full clone copy (Optional)
    storage= "storage" #Target Storage
    pool = "pool" #Resource Pool
    #snapname = "current" #Snapshot backup/current (broken rn)
    target = "target" #destination pve node

    proxmox_connect(proxmoxhost=proxmoxhost, api_token=api_token, token_id=token_id, node=node, vmid=vmid, newid=newid, name=name, full=full, pool=pool, storage=storage, target=target)

if __name__ == "__main__":
        main()
