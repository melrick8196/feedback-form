from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:1by14cs048@127.0.0.1/feedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db=SQLAlchemy(app)

class Database(db.Model):
	__tablename__='feedback_table'
	id=db.Column('id',db.Integer, primary_key=True)
	name=db.Column('name',db.String(50))
	feedback=db.Column('feedback',db.String(100))



@app.route('/feedback')
def feedback():
	fbInput=request.values.get("feedback")
	nameInput=request.values.get("name")
	if fbInput:
		res=db.engine.execute("INSERT into feedback_table (name,feedback) values (%s,%s)",(nameInput,fbInput))
		db.session.commit()	
		return "Thanks for the feedback"
	return render_template('index.html')

if __name__=='__main__':
	app.run(host='0.0.0.0')

