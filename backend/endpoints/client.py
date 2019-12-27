from flask import request
from flask_restplus import Resource
from flask_jwt_extended import jwt_required
from .. import apimodel
from .. import serializers
from .. import business
from backend.database import models
from sqlalchemy.orm.exc import NoResultFound

clientns = apimodel.api.namespace('client', description='operations related to client')

parser = apimodel.api.parser()
parser.add_argument('Authorization', location='headers')

@clientns.route('/')
class ClientCollection(Resource):

    @apimodel.api.marshal_list_with(serializers.client)
    @apimodel.api.header('Authorization:', 'JWT TOKEN', required=True)
    @apimodel.api.expect(parser)
    @jwt_required
    def get(self):
        """
        Returns list of clients
        """
        clients = models.Client.query.order_by(models.Client.name.asc()).all()
        return clients

    @apimodel.api.response(201, 'client successfully created')
    @apimodel.api.expect(serializers.client)
    def post(self):
        """
        Creates a new client
        """
        data = request.json
        business.create_client(data)
        return None, 201

@clientns.route('/<int:clientid>')
@apimodel.api.response(404, 'client not found')
class ClientRecord(Resource):

    @apimodel.api.marshal_with(serializers.client)
    @apimodel.api.header('Authorization:', 'JWT TOKEN', required=True)
    @apimodel.api.expect(parser)
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
    @apimodel.api.header('Authorization:', 'JWT TOKEN', required=True)
    @apimodel.api.expect(parser)
    def get(self, clientid):
        """
        Returns list of clientconfigparams for a client
        """
        client_parameters = models.ClientConfigParam.query.filter(models.ClientConfigParam.clientid == clientid).all()
        return client_parameters