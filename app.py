from flask import Flask, request, render_template
import yaml

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        yaml_input = request.form.get("yaml_input", "")

        try:
            parsed_data = yaml.load(yaml_input)  
            return f"<h3>Parsed Data:</h3><pre>{parsed_data}</pre>"
        except TypeError as e:
            error_message = "App failed to load YAML due to PyYAML 6.0.2 upgrade: 'Loader' argument missing in yaml.load()."
            return f"<h3>App Error:</h3><pre>{error_message}</pre><h4>Details:</h4><pre>{str(e)}</pre>"

    return render_template("index.html")

@app.route("/health", methods=["GET"])
def health_check():
    try:
        test_yaml = """app_name: TestApp
debug_mode: true"""
        parsed_data = yaml.load(test_yaml)
        return "<h3>Health Check Passed: App is functioning correctly.</h3><pre>Test YAML parsed successfully.</pre>"
    except Exception as e:
        return f"<h3>Health Check Failed:</h3><pre>{str(e)}</pre>"

if __name__ == "__main__":
    app.run(debug=True)
