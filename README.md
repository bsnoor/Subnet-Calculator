# SubnetCalculator.py
## IP Address Subnetting Tool
 This tool allows you to perform subnetting calculations on IP addresses. Given an IP address with a CIDR or subnet mask, the tool will output information such as the subnet mask, CIDR,  number of hosts, number of subnets, first and last IP addresses, network address, and broadcast address.
## Usage
To use this tool, simply run the main() function. You will be prompted to enter an IP address with a CIDR or subnet mask. The tool will then output the subnet mask, CIDR, number of hosts, number of subnets, first and last IP addresses, network address, and broadcast address.
## Example
#### Please enter an ip address with cidr or subnet mask: 192.168.1.0/24

##### Subnet mask: 255.255.255.0
##### CIDR: 24
##### Number of hosts: 254
##### Number of subnets: 1
##### First IP: 192.168.1.1
##### Last IP: 192.168.1.254
##### Network address: 192.168.1.0
##### Broadcast: 192.168.1.255
## Dependencies
This tool requires Python 3 to run.
