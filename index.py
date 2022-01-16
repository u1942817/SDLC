from flask import Flask
from flask import render_template

app = Flask(__name__)

posts = [   {"id": 5, "title": "Powerpoints .PPTs", "Creator": "Claudia Ellis", "date": "10 Jan 2022", "count": 2},
    {"id": 4, "title": "Words .DOXs", "Creator": "Claudia Ellis", "date": "10 Jan 2022", "count": 2},
    {"id": 3, "title": "Excels .XMLs", "Creator": "Claudia Ellis", "date": "10 Jan 2022", "count": 2},
    {"id": 2, "title": "Recordings .MP4s", "Creator": "Claudia Ellis", "date": "10 Jan 2022", "count": 2},
    {"id": 1, "title": "Images .PNGs", "Creator": "Claudia Ellis", "date": "10 Jan 2022", "count": 2}
]

@app.route('/')
def index():
    return render_template('dashboard.html', title='Board Title', posts=posts)

@app.route('/layout')
def layout():
    return render_template('dashboard.html')
    
if __name__ =='__main__':
    app.run(debug=True)  

    