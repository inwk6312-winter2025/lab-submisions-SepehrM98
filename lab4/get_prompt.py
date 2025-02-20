from netmiko import Netmiko
device = {
"device_type": "cisco_ios",
"ip": "192.168.1.101", # R1 Mgmt Interface
"username": "student",
"password": "Meilab123",
© Dalhousie University, Internetworking Program 5/16
"port": "22",
}
net_connect = Netmiko(**device)
print(net_connect.find_prompt())