from flask import Flask

from database_11_11_22 import app
from developer_data_3_11_22 import Dev_api

app.add_url_rule('/data', 'Dev_api.add', view_func=Dev_api.add, methods=['POST'])

app.add_url_rule('/fetch_all', 'Dev_api.view_all', view_func=Dev_api.view_all, methods=['GET'])

app.add_url_rule('/fetch/<dept_no>', 'Dev_api.view', view_func=Dev_api.view, methods=['GET'])

app.add_url_rule('/update/<dept_no>', 'Dev_api.update', view_func=Dev_api.update, methods=['PUT'])

app.add_url_rule('/delete/<dept_no>', 'Dev_api.delete', view_func=Dev_api.delete, methods=['DELETE'])

if __name__ == '__main__':
    app.run(debug=True)
