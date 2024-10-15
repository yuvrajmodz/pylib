from flask import Flask, request, jsonify
import requests
import json
import os

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_player_info():
    uid = request.args.get('getinfo')
    if not uid:
        return jsonify({'error': "Error: 'player' parameter is missing."}), 400

    # Make the request to the RapidAPI endpoint
    url = f"https://id-game-checker.p.rapidapi.com/ff-player-info/{uid}/IN"
    headers = {
        "x-rapidapi-host": "id-game-checker.p.rapidapi.com",
        "x-rapidapi-key": "031b64261dmsh1a1110a15ceba45p1dec0ejsn85ca47509f9c"
    }

    response = requests.get(url, headers=headers)

    # Check if the API response contains an error
    if response.status_code != 200:
        return jsonify({'error': 'API request failed'}), response.status_code

    # Format the JSON response with newlines after each field
    formatted_json = json.dumps(response.json(), indent=2)  # Format the JSON with indentation

    # Replace commas with commas followed by a newline for readability
    formatted_json = formatted_json.replace(',', ',\n')

    # Return the formatted JSON response
    return formatted_json, 200, {'Content-Type': 'application/json'}

# Run the Flask app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
