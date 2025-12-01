from flask import Flask, request, render_template, jsonify
import cohere

app = Flask(__name__)

def create_app():
   return app

@app.route('/')
def index():
    return render_template('index.html')  # Fixed: Added quotes around template name

@app.route('/AI', methods=['POST'])  # Fixed: 'methods' not 'method'

def AI():
    data = request.get_json()
    
    #return jsonify(data) check to see if the right data was sent and returned back to fetch
    
    
    # Check if data is None 
    if not data:
        return jsonify({"error": "No JSON data received"}), 400
    
    query = data.get('query', '')
   
    # Check if query is empty
    if not query:
        return jsonify({"error": "Query is required"}), 400


    # Fixed: Moved Cohere client inside the function and fixed indentation
    co = cohere.ClientV2("p1N0vhx8yfUzcK4ZIcGVyL9yQAG8wJ6THJX0q8a1")

    
    response = co.chat(
        model="command-a-03-2025", 
        messages=[{"role": "user", "content": query}],
        )
    
    # Extract the response content
    return jsonify(response.message.content[0].text)
        
    
if __name__ == '__main__':
 app.run(debug=False)