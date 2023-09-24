from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Simulation of licence key database
licence_db = {
    'key1': {'valid': True, 'max_users': 5, 'expiry_date': "22/02/2024"},
    'key2': {'valid': True, 'max_users': 1, 'expiry_date': "20/12/2023"}
}


@app.route('/licences/<licence_key>', methods=['GET'])
def get_licence(licence_key):
    if licence_key in licence_db:
        licence_info = licence_db[licence_key]
        expiry_date = datetime.strptime(licence_info['expiry_date'], "%d/%m/%Y")
        if licence_info['valid']:
                if expiry_date >= datetime.now():
                    return jsonify({'licence_key': licence_key, 'valid': True, 'max_users': licence_info['max_users']}), 200
                else:
                    return jsonify({'licence_key': licence_key, 'valid': True, 'expiry_date': licence_info['expiry_date']}), 403
        else:
            return jsonify({'licence_key': licence_key, 'valid': False}), 403
    else:
        return jsonify({'error': 'Licence key not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)