import flask
import pandas as pd

data_csv_file = 'task_data.csv'
sample_count = 400


def get_data():
    """
    :return: JSON Object of the csv input data file
    """
    return transform_data(pd.read_csv(data_csv_file).to_dict(orient='list'))


def transform_data(raw_data):
    """

    :param (list) all samples from the input csv file
    :return: list of rearranged samples adequate for filtering
    """
    all_sample_data = []
    for i in range(0, sample_count):
        sample_data = {
            'id': int(raw_data['sample index'][i].replace('sample', '')),
            'sample_class': raw_data['class_label'][i],
            #'sensors': get_sensors(raw_data, i),
            'sensors': [raw_data['sensor%s' % j][i] for j in range(0, 10)],

        }
        all_sample_data.append(sample_data)
    return all_sample_data


def create_app():
    app = flask.Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        """
        Index page view handler.
        :return: rendered index.html template
        """
        return flask.render_template('index.html')

    @app.route('/data', methods=['GET', 'POST'])
    def data():
        """
        Data view handler
        :return: JSON object of the data
        """
        return flask.jsonify(get_data())

    return app


if __name__ == "__main__":
    app = create_app()
    # serve the application on port 7410
    app.run(host='0.0.0.0', port=7410)
