from flask import *
import os

FOLDER = "zvířátka"
CONTEXT_SIZE = 50

app = Flask(__name__)

def get_file_content(file):
  with open(file, "r", encoding='utf-8') as content:
    return content.read()

@app.route("/home")  
def home():
    return render_template("search.html")

@app.route("/results", methods=["GET", "POST"])
def search(): 
    user_query = request.form.get("query")

    file_names = [file for file in os.listdir(FOLDER) if os.path.isfile(os.path.join(FOLDER, file))]
    results = []

    for file_name in file_names:
        absolute_path_to_file = os.path.abspath(FOLDER) + "\\" + file_name
        file_content = get_file_content(absolute_path_to_file)
        if user_query in file_content:
            text_before_query = file_content.split(user_query)[0]
            text_after_query = file_content.split(user_query)[1]
            result_dict = {
                "file_name" : file_name,
                "absolute_path" : absolute_path_to_file,
                "result" : user_query,
                "context_before" : "..." + text_before_query[-CONTEXT_SIZE:],
                "context_after" : text_after_query[:CONTEXT_SIZE] + "..."
            }
            results.append(result_dict)
    return render_template("results.html", list_of_results=results)

if __name__ == "__main__":
    app.run(debug=True)