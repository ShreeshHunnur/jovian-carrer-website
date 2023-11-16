from flask import Flask, jsonify, render_template



app = Flask(__name__)


JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'San Francisco',
    'salary': '$100,000'
  },
  
  {
    'id': 2,
    'title': 'Software Engineer',
    'location': 'Pune,India',
    'salary': 'Rs 10,00,000'
  },

  {
    'id': 3,
    'title': 'Machine Learning Engineer',
    'location': 'Bengaluru,India',
    'salary': 'Rs 15,00,000'
  },

  {
    'id': 4,
    'title': 'Data Scientist',
    'location': 'Remote',
    'salary': 'Rs 13,00,000'
  }
  
]

@app.route('/')
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name='Jovian')

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

  
if (__name__) == '__main__':
  app.run(host = '0.0.0.0',debug=True)