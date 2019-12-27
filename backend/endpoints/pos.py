from flask import request
from flask_restplus import Resource
from .. import apimodel
from .. import serializers
from backend.database import models
from sqlalchemy.orm.exc import NoResultFound

posns = apimodel.api.namespace('pos', description='operations related to pos')

@posns.route('/<int:clientid>')
@apimodel.api.response(404, 'pos not found')
class PosCollection(Resource):

    @apimodel.api.marshal_with(serializers.pos)
    def get(self, clientid):
        """
        Returns all pos records for a client
        """
        try:
            return models.Pos.query.order_by(models.Pos.name.asc()).filter(models.Pos.clientid == clientid).all()

        except NoResultFound:
            return {'message': 'A database result was required but none was found.'}, 404

@posns.route('/detail/<int:posid>/')
class PosRecord(Resource):
    @apimodel.api.response(404, 'pos not found')
    @apimodel.api.marshal_list_with(serializers.pos)
    def get(self, posid):
        """
        Returns list a single pos record
        """
        pos_record = models.Pos.query.filter(models.Pos.posid == posid).one()
        return pos_record

@posns.route('/detail/<int:posid>/cdmjobs')
class CdmJobsCollection(Resource):
    @apimodel.api.response(404, 'cdmjobs not found')
    @apimodel.api.marshal_list_with(serializers.cdmjob)
    def get(self, posid):
        """
        Returns list of pos config params
        """
        cdm_jobs = models.Cdmjob.query.filter(models.Cdmjob.posid == posid).all()
        return cdm_jobs