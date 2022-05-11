from lib.httpclient import HttpClient

http_client = HttpClient(headers={})
print('running program')

print(http_client.get('https://api.github.com/repos/MichaelMIL/pico_git_basic_ota/releases/latest').json())

print('Version 2 installed using USB') 