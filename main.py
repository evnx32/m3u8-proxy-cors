from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/proxy/<path:url>')
def proxy(url):
    # Set Mozilla user-agent header
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'  # Mozilla user-agent
    }

    # Fetch the M3U8 file from the URL with custom headers
    response = requests.get(url, stream=True, headers=headers)

    # Set the appropriate response headers
    headers = response.headers
    headers['Access-Control-Allow-Origin'] = '*'  # Allow cross-origin requests
    headers['Content-Type'] = 'application/vnd.apple.mpegurl'  # Set content type to M3U8

    # Stream the M3U8 file as a response
    return Response(response.iter_content(chunk_size=1024), headers=headers)

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode