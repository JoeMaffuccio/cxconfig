import base64
import requests
import json
def zendesk_auth_check(email, password):
    userinfo = email + ":" + password
    key = base64.b64encode(bytes(userinfo.encode('utf-8'))).decode('utf-8')
    header = {"Authorization": "Basic " + key, "Content-Type" : "application/json; charset=utf-8"} 
    response = requests.get('https://crunchtime.zendesk.com/api/v2/search?query=type:user%20email:' + email, headers = header)
    if response.status_code == 200:
        result = json.loads(response.text)
        print(result)
        group_id = result['results'][0]['default_group_id']
        if group_id == 360001909054:
            return 'ConneX'
        elif group_id == 360001868433:
            return 'Support'
        return None
    elif response.status_code == 401:
        result = json.loads(response.text)
        return result
    else:
        return None

x = zendesk_auth_check('jmaffuccio@crunchtime.com','1990Pickle')

print(x)