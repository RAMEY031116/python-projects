#this is a simple sub_domain enumaration script
import requests
import sys
subdomain_lists = open('subdomain_lists.txt').read()
list_subdomain = subdomain_lists.splitlines()

for file in list_subdomain:
    url = f"http://{file}.{sys.argv[1]}"
    try:
        requests.get(url)
    
    except requests.ConnectionError: 
        pass
    
    else:
        print("Valid domain: ",url)  