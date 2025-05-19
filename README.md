**Some python scripts for Proxmox API calls**

First two scripts are for passing arguments required arguments are coded with required: true or false

Usage example:
run with python3 ./CloneVMorTemplate.py --proxmox host --api_token api token --token_id token id --vmid # --newid # --node name --target name --name name --pool name etc 

the last one is for entering in hard coded values (not recommended)
Usage example:
python3 ./HardCodeInsteadofPassingArgs.py

note: Im by no means a coder results may vary (it works on my stuff)
