from flask import Flask, render_template, jsonify
from database import engine 
from sqlalchemy import text


app = Flask(__name__) 

JOBS = [
    {
        "id": '1',
        'title': 'Data Analyst', 
        'location': 'Benguluru, India', 
        'salary': 'Rs. 10,000,000'
    },
    {
        "id": '2',
        'title': 'Data Scientist', 
        'location': 'Delhi, India', 
        'salary': 'Rs. 15,000,000'
    },
    {
        "id": '3',
        'title': 'Frontend Engineer',
        'location': 'Remote', 
        'salary': 'Rs. 1,000,000'
    },
    {
        "id": '4',
        'title': 'Backend Emgineer', 
        'location': 'Hybrid', 
    }
    
]

def load_jobs_from_db(): 
    with engine.connect() as conn : 
        result = conn.execute(text("SELECT * FROM jobs")) 
        jobs = [] 
        for row in result.all() : 
            jobs.append(dict(row)) 
    return jobs

@app.route("/") 
def hello(): 
    return render_template("home.html", jobs=JOBS)

@app.route("/api/jobs")
def list_jobs(): 
    return jsonify(JOBS)

if __name__ == "__main__" : 
    app.run(debug=True)

