import json

from flask import Flask, jsonify, request, Response
from flask_swagger_ui import get_swaggerui_blueprint

from pdm_wrap import PdM_wrap

# Init pdm class
pdm = PdM_wrap()
# Init flask app
app = Flask(__name__)
# Init swagger
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Navarchos PdM API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


# Get data route
@app.route("/data", methods=["POST"])
def data():
    in_data = request.get_json()
    if "timestamp" not in in_data or "features" not in in_data or "source" not in in_data:
        return Response(json.dumps({"error": "Missing 1 or more keys 'timestamp', 'features', 'source'"}), 500)
    try:
        res = pdm.collect_data(in_data)
    except Exception as e:
        return Response(json.dumps({"error": repr(e)}), 500)
    return jsonify(res)


@app.route("/event", methods=["POST"])
def event():
    in_data = request.get_json()
    if "timestamp" not in in_data or "description" not in in_data or "source" not in in_data:
        return Response(json.dumps({"error": "Missing 1 or more keys 'timestamp', 'description', 'source'"}), 500)
    try:
        pdm.collect_event(in_data)
    except Exception as e:
        return Response(json.dumps({"error": repr(e)}), 500)
    return jsonify({"Message": "OK"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
