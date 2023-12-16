import openai

import os

from flask import Flask, render_template_string, request


openai.api_key = os.environ['OPENAI_API_KEY']


def generate_tutorial(disease):

 response = openai.ChatCompletion.create(

  model="gpt-3.5-turbo",

  messages=[{

   "role": "system",

   "content": "You are a helpful assistant"

  }, {

   "role":

   "user",

   "content":

   f"Provide overview, symptoms, causes, treatment and suggest home remedies for disease - {disease} Give a caution too "

  }])

 return response['choices'][0]['message']['content']

# Create a Flask web application object named app and define a route for the root URL that responds to GET and POST requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

# This code defines a function that generates the response based on user input obtained through a POST request.

def hello():

 output = ""

 if request.method == 'POST':

  disease = request.form['disease']

  output = generate_tutorial(disease)


 return render_template_string('''

 <!DOCTYPE html>

 <html>

 <head>

  <title>Personal Health Assistant</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"rel="stylesheet">
    <style>
        body {
            background-color: #f8f9fa;
            font-family: 'Arial', sans-serif;
        }

        .container {
            background-color: #ffffff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            border-radius: 10px;
        }

        h1 {
            color: #007bff;
        }

        .card {
            margin-top: 20px;
            border: 1px solid rgba(0, 0, 0, 0.125);
            border-radius: 8px;
        }

        .card-header {
            background-color: #007bff;
            color: #ffffff;
        }

        .btn-primary {
            background-color: #007bff;
            border-color: #007bff;
        }

        .btn-primary:hover {
            background-color: #0056b3;
            border-color: #0056b3;
        }

        .btn-secondary {
            background-color: #6c757d;
            border-color: #6c757d;
        }

        .btn-secondary:hover {
            background-color: #545b62;
            border-color: #545b62;
        }

        .container-fluid {
            background-color: #343a40;
            color: #ffffff;
            padding: 5px 0;
            text-align: center;
        }
    </style>

  <script>

  async function generateTutorial() {

   const disease = document.querySelector('#disease').value;

   const output = document.querySelector('#output');

   output.textContent = 'Health is Wealth... wait for few seconds';

   const response = await fetch('/generate', {

    method: 'POST',

    body: new FormData(document.querySelector('#tutorial-form'))

   });

   const newOutput = await response.text();

   output.textContent = newOutput;

  }

  function copyToClipboard() {

   const output = document.querySelector('#output');

   const textarea = document.createElement('textarea');

   textarea.value = output.textContent;

   document.body.appendChild(textarea);

   textarea.select();

   document.execCommand('copy');

   document.body.removeChild(textarea);

   alert('Copied to clipboard');

  }

  </script>

 </head>

 <body>

  <div class="container mt-3 mb-3" style="min-height:629px;">

   <h1 class="my-4">Healthoepaedia</h1>

   <form id="tutorial-form" onsubmit="event.preventDefault(); generateTutorial();" class="mb-3">

    <div class="mb-3">

     <label for="disease" class="form-label">Disease Name:</label>

     <input type="text" class="form-control" id="disease" name="disease" placeholder="Enter the name of Disease"required>

    </div>

    <button type="submit" class="btn btn-primary">Generate details</button>

   </form>

   <div class="card">

    <div class="card-header mb-2 d-flex justify-content-between align-items-center">

     Disease Details:

     <button class="btn btn-secondary btn-sm" onclick="copyToClipboard()">Copy</button>

    </div>

    <div class="card-body">

     <pre id="output" class="mb-0" style="white-space: pre-wrap;">{{ output }}</pre>

    </div>

   </div>

  </div>
  <div class="container-fluid bg-dark text-light mb-0">
      <p class="text-center mb-0">
          copyright &copy; 2023 Healthoepaedia | All rights reserved
      </p>
  </div>


 </body>

 </html>

 ''',

                output=output)

# This code defines a route for the URL "/generate" that only accepts POST requests.

@app.route('/generate', methods=['POST'])

# This code defines a function 'generate' that takes a POST request containing a 'disease' field and returns the result of calling the 'generate_tutorial' function with the provided disease as input.

def generate():

 disease = request.form['disease']

 return generate_tutorial(disease)

# This code snippet starts the Flask application if the script is being run directly as the main program, running on the IP address '0.0.0.0' and port number 8080.

if __name__ == '__main__':

 app.run(host='0.0.0.0', port=8080)