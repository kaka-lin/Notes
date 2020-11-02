from flask import Response, Flask, jsonify
import prometheus_client
from prometheus_client import Counter

app = Flask(__name__)

total_requests = Counter(
    'request_count',
    'Total webapp request count')

@app.route('/metrics')
def requests_count():
    #total_requests.inc()
    return Response(
        prometheus_client.generate_latest(total_requests),
        mimetype='text/plain')

@app.route('/')
def index():
    total_requests.inc()
    return jsonify({
        'status': 'ok'
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
