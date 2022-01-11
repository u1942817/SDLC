from flask import Flask
from flask import render_template

app = Flask(__name__)

posts = [   {"id": 5, "title": "Resource Board", "Creator": "Claudia Ellis", "date": "10 Jan 2022", "count": 2},
    {"id": 4, "title": "Notice Board", "Creator": "Claudia Ellis", "date": "10 Jan 2022", "count": 2},
    {"id": 3, "title": "Q&A Board", "Creator": "Claudia Ellis", "date": "10 Jan 2022", "count": 2},
    {"id": 2, "title": "Lecture Board", "Creator": "Claudia Ellis", "date": "10 Jan 2022", "count": 2},
    {"id": 1, "title": "Quiz Board ", "Creator": "Claudia Ellis", "date": "10 Jan 2022", "count": 2}
]

@app.route('/')
def index():
    return render_template('list.html', posts=posts)
    
if __name__ =='__main__':
    app.run(debug=True)  

    