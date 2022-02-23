from flask import Flask, render_template
import oyaml as yaml 

application = Flask(__name__)
application.config['JSON_SORT_KEYS'] = False

@application.route('/')
def index():
    website_data = yaml.safe_load(open('_config.yaml'))

    return render_template('index.html', data=website_data)

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=80, debug=True)