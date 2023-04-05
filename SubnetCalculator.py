def validate_ip(ip_add):
    # check number of periods
    if ip_add.count(".") != 3:
      return False

    # check range of each number between periods
    for num in ip_add.split("."):
        if int(num) < 0 or int(num) > 255:
          return False

    return True

def brodcast_address(ip_address, subnet_mask):
    ip_list = ip_address.split(".")
    subnet_list = subnet_mask.split(".")
    broadcast_list = [int(ip_list[i]) | (255 - int(subnet_list[i])) for i in range(4)]
    broadcast = ".".join(map(str, broadcast_list))

    return broadcast

def cidr_to_netmask(cidr):
  mask = (0xffffffff >> (32 - cidr)) << (32 - cidr)
  return (str( (0xff000000 & mask) >> 24)   + '.' +
          str( (0x00ff0000 & mask) >> 16)   + '.' +
          str( (0x0000ff00 & mask) >> 8)    + '.' +
          str( (0x000000ff & mask)))

def netmask_to_cidr(netmask):
    negative_offset = 0

    for octet in netmask.split("."):
        binary = format(int(octet), '08b')
        for char in reversed(binary):
            if char == '1':
                break
            negative_offset += 1

    return '{0}'.format(32-negative_offset)

def network_address(ip_address, subnet_mask):
    ip_octets = ip_address.split('.')
    subnet_octets = subnet_mask.split('.')
    network_octets = []

    for i in range(4):
        network_octets.append(str(int(ip_octets[i]) & int(subnet_octets[i])))

    return '.'.join(network_octets)

def number_of_hosts(cidr):
    return (1 << (32 - int(cidr))) - 2

def number_of_subnets(cidr):
   if int(cidr) >= 24:
       return 0x100 >> (int(cidr) - 24)
   else:
       return 0x100 >> (24 - int(cidr))

def first_host(ip_add,netmask):
  num = [0,0,0,0]
  i = 0
  while i < len(ip_add.split(".")):
    num[i] = int(ip_add.split(".")[i]) & int(netmask.split(".")[i])
    i += 1
  num[len(num)-1] += 1
  return '.'.join(map(str, num))

def main():
  ip_address = input("Please enter an ip address with cidr or subnet mask: ")
  if validate_ip(ip_address.split("/")[0]) == False:
    print("Invalid address.")
  elif ip_address.split("/")[1].count(".") > 0 and validate_ip(ip_address.split("/")[1]) == False:
    print("Invalid address.")
  elif ip_address.split("/")[1].count(".") > 0:
    netmask=ip_address.split("/")[1]
    cidr=netmask_to_cidr(ip_address.split("/")[1])
  else:
    cidr=int(ip_address.split("/")[1])
    netmask=cidr_to_netmask(int(ip_address.split("/")[1]))

  if cidr != 0:
      brodcast = brodcast_address(ip_address.split("/")[0], netmask)
      last = brodcast.split(".")
      last[-1] = str(int(last[-1]) - 1)
      last = ".".join(last)
      print("Subnet mask: " + netmask)
      print("CIDR: " + str(cidr))
      print("Number of hosts: " + str(number_of_hosts(cidr)))
      print("Number of subnets: " + str(number_of_subnets(cidr)))
      print("First IP: " + str(first_host(ip_address.split("/")[0], netmask)))
      print("Last IP: " + str(last))
      print("Network address: " + str(network_address(ip_address.split("/")[0], netmask)))
      print("Broadcast: " + str(brodcast_address(ip_address.split("/")[0], netmask)))

if __name__ == '__main__':
  main()
