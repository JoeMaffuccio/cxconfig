from flask import request
from flask_restplus import Resource
from .. import apimodel
from .. import serializers
from backend.database import models
from sqlalchemy.orm.exc import NoResultFound

clientns = apimodel.api.namespace('client', description='operations related to client')

@clientns.route('/')
class ClientCollection(Resource):

    @apimodel.api.marshal_list_with(serializers.client)
    def get(self):
        """
        Returns list of clients
        """
        clients = models.Client.query.order_by(models.Client.name.asc()).all()

        return clients

@clientns.route('/<int:clientid>')
@apimodel.api.response(404, 'client not found')
class ClientRecord(Resource):

    @apimodel.api.marshal_with(serializers.client)
    def get(self, clientid):
        """
        Returns a single client
        """
        try:
            return models.Client.query.filter(models.Client.clientid == clientid).one()

        except NoResultFound:
            return {'message': 'A database result was required but none was found.'}, 404

@clientns.route('/<int:clientid>/config/')
class ClientConfigParamCollection(Resource):
    @apimodel.api.response(404, 'clientconfigparam not found')
    @apimodel.api.marshal_list_with(serializers.client_config_param)
    def get(self, clientid):
        """
        Returns list of clientconfigparams for a client
        """
        client_parameters = models.ClientConfigParam.query.filter(models.ClientConfigParam.clientid == clientid).all()
        return client_parameters