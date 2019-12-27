from flask_restplus import fields
from . import apimodel

person = apimodel.api.model('Person', {
    'personid': fields.Integer(readonly=True),
    'firstname': fields.String(required=True),
    'lastname': fields.String(),
    'emailaddress': fields.String()})

postype = apimodel.api.model('Postype', {
    'postypeid': fields.Integer,
    'manufacturername': fields.String(),
    'name': fields.String(),
    'description': fields.String()})

timezone = apimodel.api.model('Timezone', {
    'timezoneid': fields.Integer,
    'name': fields.String(),
    'mysql_tz': fields.String(),
    'timezoneoffset': fields.Float})

client = apimodel.api.model('Client', {
    'clientid': fields.Integer(readOnly=True, description='unique identifier of a client'),
    'clientguid': fields.String(required=True, description='client guid'),
    'name': fields.String(required=True, description='client name'),
    'enabledflag': fields.Integer(required=True, description='client enabled'),
    'dateadded': fields.DateTime,
    'dateupdated': fields.DateTime,
    'addedbyuser': fields.Nested(person),
    'updatedbyuser': fields.Nested(person)})

client_config_param = apimodel.api.model('ClientConfigParam', {
    'clientid': fields.Integer(readOnly=True, description='unique identifier of a client'),
    'name': fields.String(required=True, description='name of parameter'),
    'value': fields.String(required=True, description='client name'),
    'dateadded': fields.DateTime,
    'dateupdated': fields.DateTime,
    'addedbyuser': fields.Nested(person),
    'updatedbyuser': fields.Nested(person)})

pos = apimodel.api.model('Pos', {
    'posid': fields.Integer(readOnly=True, description='unique identifier of a pos'),
    'posguid': fields.String(required=True, description='pos guid'),
    'postype': fields.Nested(postype),
    'clientid': fields.Integer,
    'name': fields.String(required=True, description='pos name'),
    'timezone': fields.Nested(timezone),
    'allowactivationflag': fields.Integer,
    'activationcode': fields.String,
    'enabledflag': fields.Integer(required=True, description='client enabled'),
    'dateadded': fields.DateTime,
    'dateupdated': fields.DateTime,
    'addedbyuser': fields.Nested(person),
    'updatedbyuser': fields.Nested(person)})

pos_config_param = apimodel.api.model('PosConfigParam', {
    'posid': fields.Integer(readOnly=True),
    'name': fields.String(required=True),
    'value': fields.String(required=True),
    'dateadded': fields.DateTime,
    'dateupdated': fields.DateTime,
    'addedbyuser': fields.Nested(person),
    'updatedbyuser': fields.Nested(person)})

cdmjob = apimodel.api.model('Cdmjob', {
    'jobid': fields.Integer,
    'posid': fields.Integer,
    'taskid': fields.String,
    'workingdirectory': fields.String,
    'script': fields.String,
    'enabled': fields.Integer,
    'comments': fields.String})