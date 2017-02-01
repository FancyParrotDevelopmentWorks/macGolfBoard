from app import db
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime

class Users(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    create_date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    last_update_date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    user_name = db.Column(db.String())
    avatar = db.Column(db.String(200))
    active = db.Column(db.Boolean, default=False)
    tokens = db.Column(db.Text)
    phone_number = db.Column(db.String())
    can_text = db.Column(db.Boolean)
    
    def __init__(self, email, user_name, avatar, active, tokens, phone_number, can_text):
        self.email = email
        self.user_name = user_name
        self.avatar = avatar
        self.active = active
        self.tokens = tokens
        self.phone_number = phone_number
        self.can_text = can_text
        
    def __repr__(self):
        return '<id {}>'.format(self.id)
    
class Clubs(db.Model):
    __tablename__ = 'clubs'
    
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    last_update_date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    name = db.Column(db.String())
    home_course_id = db.Column(db.Integer)
    num_members = db.Column(db.Integer)
    
    def __init__(self, name, home_course_id, num_members):
        self.name = name,
        self.home_course_id = home_course_id
        self.num_members = num_members
        
    def __repr__(self):
        return '<id {}>'.format(self.id)

class Club_Members(db.Model):
    __tablename__ = 'club_members'
    
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    last_update_date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    club_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    
    def __init__(self, club_id, user_id):
        self.club_id = club_id
        self.user_id = user_id
    
    
class Rounds(db.Model):
    __tablename__ = 'rounds'
    
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    last_update_date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    course_id = db.Column(db.Integer)
    tee_id = db.Column(db.Integer)
    time = db.Column(db.DateTime(timezone=True))
    group_id = db.Column(db.Integer)
    score = db.Column(db.Integer)
    
    def __init__(self, course_id, tee_id, time, group_id, score):
        self.course_id = course_id
        self.tee_id = tee_id
        self.time = time
        self.group_id = group_id
        self.score = score
        
    def __repr__(self):
        return '<id {}>'.format(self.id)
    
class Groups(db.Model):
    __tablename__ = 'groups'
    
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    last_update_date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    group_type = db.Column(db.String())
    course_id = db.Column(db.Integer)
    tee_id = db.Column(db.Integer)
    time = db.Column(db.DateTime(timezone=True))
    parent_group_id = db.Column(db.Integer)
    max_players = db.Column(db.Integer)
    num_players = db.Column(db.Integer)
    
    def __init__(self, group_type, course_id, tee_id, time, parent_group_id, max_players, num_players):
        self.group_type = group_type
        self.course_id = course_id
        self.tee_id = tee_id
        self.time = time
        self.parent_group_id = parent_group_id
        self.max_players = max_players
        self.num_players = num_players
    
    def __repr__(self):
        return '<id {}>'.format(self.id)
    
class Courses(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    last_update_date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    name = db.Column(db.String())
    phone = db.Column(db.String())
    address1 = db.Column(db.String())
    address2 = db.Column(db.String())
    city = db.Column(db.String())
    province = db.Column(db.String())
    state = db.Column(db.String())
    country = db.Column(db.String())
    postal_code = db.Column(db.String())
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    #info = db.Column(JSON)
    
    def __init__(self, name, phone, address1, address2, city, province, state, country, postal_code, lat, lng):
        self.name = name
        self.phone = phone
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.province = province
        self.state = state
        self.country = country
        self.postal_code = postal_code
        self.lat = lat
        self.lng = lng
        #self.info = info
        
    def __repr__(self):
        return '<id {}>'.format(self.id)

class Tees(db.Model):
    __tablename__ = 'tees'
    
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    last_update_date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    course_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String())
    par = db.Column(db.Integer)
    index = db.Column(db.Float)
    slope = db.Column(db.Float)
    
    def __init__(self, course_id, name, par, index, slope):
        self.course_id = course_id,
        self.name = name,
        self.par = par
        self.index = index
        self.slope = slope
    
    def __repr__(self):
        return '<id {}>'.format(self.id)

class Holes(db.Model):
    __tablename__='holes'
    
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    last_update_date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    course_id = db.Column(db.Integer)
    tee_id = db.Column(db.Integer)
    par = db.Column(db.Integer)
    distance = db.Column(db.Float)
    
    def __init__(self, course_id, tee_id, par, distance):
        self.course_id = course_id
        self.tee_id = tee_id
        self.par = par
        self.distance = distance
        
    def __repr__(self):
        return '<id {}>'.format(self.id)
    