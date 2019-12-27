from . import db
import datetime

class Postype(db.Model):
    postypeid = db.Column(db.Integer, primary_key=True)
    manufacturername = db.Column(db.String(100))
    name = db.Column(db.String(100))
    description = db.Column(db.String(510))

    def __init__(self, postypeid, manufacturername, name, description):
        self.postypeid = postypeid
        self.manufacturername = manufacturername
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Postype %r>' % self.postypeid

class Timezone(db.Model):
    timezoneid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    mysql_tz = db.Column(db.String(20))
    timezoneoffset = db.Column(db.Float)

    def __init__(self, timezoneid, name, mysql_tz, timezoneoffset):
        self.timezoneid = timezoneid
        self.name = name
        self.mysql_tz = mysql_tz
        self.timezoneoffset = timezoneoffset

    def __repr__(self):
        return '<Timezone %r>' % self.timezoneid

class Person(db.Model):
    personid = db.Column(db.Integer, primary_key=True, nullable=False)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    emailaddress = db.Column(db.String(256))

    def __init__(self, personid, firstname, lastname, emailaddress):
        self.personid = personid
        self.firstname = firstname
        self.lastname = lastname
        self.emailaddress = emailaddress

    def __repr__(self):
        return '<Person %r>' % self.personid

class Client(db.Model):
    clientid = db.Column(db.Integer, primary_key=True)
    clientguid = db.Column(db.String(64))
    name = db.Column(db.String(256))
    enabledflag = db.Column(db.Integer)
    dateadded = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    dateupdated = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    addedby = db.Column(db.Integer, db.ForeignKey('person.personid'))
    addedbyuser = db.relationship('Person', foreign_keys=[addedby], uselist=False)
    updatedby = db.Column(db.Integer, db.ForeignKey('person.personid'))
    updatedbyuser = db.relationship('Person', foreign_keys=[updatedby], uselist=False)

    def __init__(self, clientid, clientguid, name, enabledflag, dateadded, dateupdated, addedby, updatedby):
        self.clientid = clientid
        self.clientguid = clientguid
        self.name = name
        self.enabledflag = enabledflag
        if dateadded is None:
            dateadded = datetime.datetime.utcnow()
        self.dateadded = dateadded
        if dateupdated is None:
            dateupdated = datetime.datetime.utcnow()
        self.dateupdated = dateupdated
        self.addedby = addedby
        self.updatedby = updatedby

    def __repr__(self):
        return '<Client %r>' % self.clientid

class ClientConfigParam(db.Model):
    clientid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), primary_key=True)
    value = db.Column(db.String(5000))
    dateadded = db.Column(db.DateTime)
    dateupdated = db.Column(db.DateTime)
    addedby = db.Column(db.Integer, db.ForeignKey('person.personid'))
    addedbyuser = db.relationship('Person', foreign_keys=[addedby], uselist=False)
    updatedby = db.Column(db.Integer, db.ForeignKey('person.personid'))
    updatedbyuser = db.relationship('Person', foreign_keys=[updatedby], uselist=False)

    def __init__(self, clientid, name, value, dateadded, dateupdated, addedby, updatedby):
        self.clientid = clientid
        self.name = name
        self.value = value
        if dateadded is None:
            dateadded = datetime.datetime.utcnow()
        self.dateadded = dateadded
        if dateupdated is None:
            dateupdated = datetime.datetime.utcnow()
        self.dateupdated = dateupdated
        self.addedby = addedby
        self.updatedby = updatedby

    def __repr__(self):
        return '<Client_Config_Param %r>' % self.name

class Pos(db.Model):
    posid = db.Column(db.Integer, primary_key=True)
    posguid = db.Column(db.String(64))
    postypeid = db.Column(db.Integer, db.ForeignKey('postype.postypeid'))
    postype = db.relationship('Postype', foreign_keys=[postypeid], uselist=False)
    clientid = db.Column(db.Integer, db.ForeignKey('client.clientid'), nullable=False)
    name = db.Column(db.String(256))
    timezoneid = db.Column(db.Integer, db.ForeignKey('timezone.timezoneid'))
    timezone = db.relationship('Timezone', foreign_keys=[timezoneid], uselist=False)
    allowactivationflag = db.Column(db.Integer)
    activationcode = db.Column(db.String(100))
    enabledflag = db.Column(db.Integer)
    dateadded = db.Column(db.DateTime)
    dateupdated = db.Column(db.DateTime)
    addedby = db.Column(db.Integer, db.ForeignKey('person.personid'))
    addedbyuser = db.relationship('Person', foreign_keys=[addedby], uselist=False)
    updatedby = db.Column(db.Integer, db.ForeignKey('person.personid'))
    updatedbyuser = db.relationship('Person', foreign_keys=[updatedby], uselist=False)

    def __init__(self, posid, posguid, postypeid, name, timezoneid, allowactivationflag, activationcode, enabledflag, dateadded, dateupdated, addedby, updatedby):
        self.posid = posid
        self.posguid = posguid
        self.postypeid = postypeid
        self.name = name
        self.timezoneid = timezoneid
        self.allowactivationflag = allowactivationflag
        self.activationcode = activationcode
        self.enabledflag = enabledflag
        if dateadded is None:
            dateadded = datetime.datetime.utcnow()
        self.dateadded = dateadded
        if dateupdated is None:
            dateupdated = datetime.datetime.utcnow()
        self.dateupdated = dateupdated
        self.addedby = addedby
        self.updatedby = updatedby

    def __repr__(self):
        return '<Pos %r>' % self.posid

class PosConfigParam(db.Model):
    posid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), primary_key=True)
    value = db.Column(db.String(5000))
    dateadded = db.Column(db.DateTime)
    dateupdated = db.Column(db.DateTime)
    addedby = db.Column(db.Integer, db.ForeignKey('person.personid'))
    addedbyuser = db.relationship('Person', foreign_keys=[addedby], uselist=False)
    updatedby = db.Column(db.Integer, db.ForeignKey('person.personid'))
    updatedbyuser = db.relationship('Person', foreign_keys=[updatedby], uselist=False)

    def __init__(self, posid, name, value, dateadded, dateupdated, addedby, updatedby):
        self.posid = posid
        self.name = name
        self.value = value
        if dateadded is None:
            dateadded = datetime.datetime.utcnow()
        self.dateadded = dateadded
        if dateupdated is None:
            dateupdated = datetime.datetime.utcnow()
        self.dateupdated = dateupdated
        self.addedby = addedby
        self.updatedby = updatedby

    def __repr__(self):
        return '<Pos_Config_Param %r>' % self.name

class Cdmjob(db.Model):
    jobid = db.Column(db.Integer, primary_key=True)
    posid = db.Column(db.Integer)
    taskid = db.Column(db.String(45))
    workingdirectory = db.Column(db.String(150))
    script = db.Column(db.String(45))
    enabled = db.Column(db.Integer)
    comments = db.Column(db.String(150))

    def __init__(self, jobid, posid, taskid, workingdirectory, script, enabled, comments):
        self.jobid = jobid
        self.posid = posid
        self.taskid = taskid
        self.workingdirectory = workingdirectory
        self.script = script
        self.enabled = enabled
        self.comments = comments

    def __repr__(self):
        return '<Cdmjob %r>' % self.jobid