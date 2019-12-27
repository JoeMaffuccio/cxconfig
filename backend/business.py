from app import db
from backend.models import Client, ClientConfigParam

def create_client(data):
    client_id = data.get('clientid')
    client_guid = data.get('clientguid')
    name = data.get('name')
    enabled_flag = data.get('enabledflag')
    date_added = data.get('dateadded')
    date_updated = data.get('dataupdated')
    added_by = data.get('addedby')
    updated_by = data.get('updatedby')

    client = Client(client_id, client_guid, name, enabled_flag, date_added, date_updated, added_by, updated_by)
    db.session.add(client)
    db.session.commit()

def create_client_config_param(data):
    client_id = data.get('clientid')
    name = data.get('name')
    value = data.get('value')
    date_added = data.get('dateadded')
    date_updated = data.get('dataupdated')
    added_by = data.get('addedby')
    updated_by = data.get('updatedby')

    clientconfigparam = ClientConfigParam(client_id, name, value, date_added, date_updated, added_by, updated_by)
    db.session.add(clientconfigparam)
    db.session.commit()