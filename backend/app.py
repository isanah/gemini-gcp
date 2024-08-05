from flask import Flask, request, jsonify
import os
from google.cloud import aiplatform

app = Flask(__name__)

def generate_text(prompt):
    # Set the API key as an environment variable
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "AIzaSyDFQlOm0NEBLruNRqJYqzg9-82Rhkkpf60"

    # Initialize the AI Platform client
    client_options = {"api_endpoint": "us-central1-aiplatform.googleapis.com"}
    aiplatform.init(client_options=client_options)

    # Load the model
    model = aiplatform.Model(
        model_name="projects/chromatic-idea-422815-v2/locations/us-central1/models/gemini-1.5-flash-latest"
    )

    # Generate text using the model
    response = model.predict(instances=[{"prompt": prompt}])
    return response.predictions[0]

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt')
    generated_text = generate_text(prompt)
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(debug=True)



from flask import Flask, request, jsonify
import os
import google.cloud.aiplatform as aiplatform

app = Flask(__name__)

def generate_text(prompt):
    # Set the API key as an environment variable
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "AIzaSyDFQlOm0NEBLruNRqJYqzg9-82Rhkkpf60"

    # Initialize the Gemini model
    model = aiplatform.gapitlm.Model(
        endpoint='projects/chromatic-idea-422815-v2/locations/us-central1/models/gemini-1.5-flash-latest'
    )

    # Generate text using the model
    response = model.predict(prompt)
    return response.text

@app.route('/generate', methods=['POST'])
def generate():
        data = request.get_json()
        prompt = data.get('prompt')
        generated_text = generate_text(prompt)
        return jsonify({'generated_text': generated_text})

# Add a root endpoint for GET requests
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Gemini Text Generation API!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')