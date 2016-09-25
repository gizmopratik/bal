from app import app, models, db
from flask_restful import Resource, Api, reqparse, fields, marshal_with
import datetime

api = Api(app)

goal_fields = {
    'title':fields.String,
    'text':fields.String,
    'status':fields.Boolean,
    'end_date':fields.DateTime(dt_format='rfc822'),
}

class LifeGoalList(Resource):
    @marshal_with(goal_fields)
    def get(self):
        return models.LifeGoals.query.order_by(models.LifeGoals.end_date).all()

    @marshal_with(goal_fields)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, help='No Title given', location='json')
        parser.add_argument('text', type=str, location='json')
        parser.add_argument('status', type=bool, location='json')
        parser.add_argument('end_date', type=str, help="end_date required", location='json')
        args = parser.parse_args()
        goal_time = datetime.datetime.strptime(args['end_date'], "%Y-%m-%d %H:%M:%S.%f")
        new = models.LifeGoals(args['title'], args['text'], args['status'], goal_time)
        db.session.add(new)
        db.session.commit()
        return models.LifeGoals.query.filter_by(title=args['title']).first(), 201

class LifeGoal(Resource):
    @marshal_with(goal_fields)
    def get(self, goal_id):
        return models.LifeGoals.query.filter_by(title=goal_id).first()

    @marshal_with(goal_fields)
    def put(self, goal_id):
        entry = models.LifeGoals.query.filter_by(title=goal_id).first()
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, help='No Title given', location='json')
        parser.add_argument('text', type=str, location='json')
        parser.add_argument('status', type=bool, location='json')
        parser.add_argument('end_date', type=str, help="end_date required", location='json')
        args = parser.parse_args()
        goal_time = datetime.datetime.strptime(args['end_date'], "%Y-%m-%d %H:%M:%S.%f")
        entry.title = args['title']
        entry.text = args['text']
        entry.status = args['status']
        entry.end_date = goal_time
        db.session.commit()
        return models.LifeGoals.query.filter_by(title=args['title']).first(), 202

    def delete(self, goal_id):
        trash = models.LifeGoals.query.filter_by(title=goal_id).first()
        db.session.delete(trash)
        db.session.commit()
        return '', 204

api.add_resource(LifeGoal, '/goals/<string:goal_id>', endpoint='goal')
api.add_resource(LifeGoalList, '/goals', endpoint='goals')
