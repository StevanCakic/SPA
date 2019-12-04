from urllib import request
import json

content = request.urlopen("https://api.github.com/users/StevanCakic").read()
print(json.loads(content.decode()))
