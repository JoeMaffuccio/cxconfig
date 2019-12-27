from flask import Response, request, json
from flask_restplus import Resource
from flask_jwt_extended import create_access_token
from .. import apimodel
from .. import serializers
import requests
import base64
import datetime

authns = apimodel.api.namespace('auth', description='operations related to authorization')

@authns.route('/')
class LoginApi(Resource):

    @apimodel.api.expect(serializers.authuser)
    def post(self):
        body = request.json
        try:
            userinfo = body.get('email') + ":" + body.get('password')
            key = base64.b64encode(bytes(userinfo.encode('utf-8'))).decode('utf-8')
            header = {"Authorization": "Basic " + key, "Content-Type" : "application/json; charset=utf-8"} 
            response = requests.get('https://crunchtime.zendesk.com/api/v2/search?query=type:user%20email:' + body.get('email'), headers = header)
            if response.status_code == 200:
                result = json.loads(response.text)
                group_id = result['results'][0]['default_group_id']
                if group_id == 360001909054:
                    authorized = True
                elif group_id == 360001868433:
                    authorized = False
            elif response.status_code == 401:
                result = json.loads(response.text)
                return result
            else:
                return None
            if not authorized:
                return {'error': 'Email or password invalid'}, 401
                
            expires = datetime.timedelta(minutes=60)
            access_token = create_access_token(identity=str(body.get('email')), expires_delta=expires)
            return {'token': 'Bearer ' + access_token}, 200

        except Exception:
            return None