from flask import Flask, render_template
import json
import os

app = Flask(__name__)

FOLDER = "zvířátka"
CONTEXT_SIZE = 50

def get_file_content(file):
  with open(file, "r", encoding='utf-8') as content:
    return content.read()

@app.route('/moje_api')
def index():
    lidi = [ 
        {"jmeno" : "Honza", "prijmeni" : "Veverka"}, 
        {"jmeno" : "Jitka", "prijmeni" : "Kloboukova"}
    ]

    return json.dumps(lidi)


if __name__ == '__main__':
    app.run(debug=True)
