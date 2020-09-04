from flask import Flask, render_template, request, jsonify
from ml_model import classify
import json

app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
# whenever this route gets called, it will execute a function
def felipython_function():
    if request.method == 'POST':		# reading the inputs from the incoming post request
        text = request.get_json()		# we are going into to json request and getting the key called "text"
        data = text['text']		# call a function to get my prediction
        result = classify(data)		# returning the result to the html
        return jsonify(result.tolist())	# any type of cool logic in python can be exectured
	# read inputs from a html	# run a machine learning model (pre trained)	# return the result back to our html
    else:
        return jsonify({"result" : "Hello World this came from an api"})



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')