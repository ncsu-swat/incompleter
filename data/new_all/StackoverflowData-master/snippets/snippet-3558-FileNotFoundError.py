#Source: https://stackoverflow.com/questions/72245924/re-search-typeerror-cannot-use-a-string-pattern-on-a-bytes-like-object
import subprocess
import re

interface = input(" interface : ")
new_mac = input("new MAC : ")

print("Changing " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
subprocess.call(["ifconfig"])

ifconfig_result = subprocess.check_output(["ifconfig", "eth0",])
print(ifconfig_result)

mac_addr_searchresult = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
print(mac_addr_searchresult.group(0))