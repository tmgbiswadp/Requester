import requests
import sys
url = "https://"
main_url = url+str(sys.argv[1])
print(main_url)


response = requests.get(main_url)
if response.status_code == 200:
    print("Success")
elif response.status_code == 404:
    print("Not found")
'''
if response:
    print('Success!')
else:
    print('An error has occurred.')
'''