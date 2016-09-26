# Balance
##Life Goal tracking app
Create an app which tracks life goals created by user. The app should be able to create goals by taking inputs such as end date, title, and additional notes to the task from user. Show the name of the task with progress made till the end date, sorted by end date on the landing page while showing details including the additional notes on the details page. There should be an option to rename the title, text and to change the end date also mark the task complete after the end date. User should be able to delete the task.

##Backend

Create a REST API
design a SQL schema with
```
id: integer autoincrement
title: string field
text: string field
status: boolean field
datetime: datetime field
```
###endpoints:
```
/goals
/goals/<str:goal_id>
```
##requirements:
```
virtual environment
flask
flask-restful
flask_sqlalchemy
```
##setup:
-Clone the repository
-Create a database table using db_create.py
-Run the development server using run.py
-Hit the endpoints using a browser at http://127.0.0.1:5000/goals or use curl/python requests(accepts json only)

##POST request example using python requests
```
url = 'https://127.0.0.1:5000/goals'
payload = {'title': 'hello', 'text': 'world', 'status': False, 'end_date': str(datetime.datetime.utcnow())}
headers = {'content-type': 'application/json'}

response = requests.post(url, data=json.dumps(payload), headers=headers)
```
