# -*- coding: utf-8 -*-

# import os
import os

from flask import Flask
from flask_restful import Api

from apps.live_url_api import live_api

# 注册flask
app = Flask(__name__)
# restful
api = Api(app)
# encode
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
app.config['JSON_AS_ASCII'] = False
# registered
app.register_blueprint(live_api, url_prefix='/dora')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    # app.run(host='0.0.0.0', port=port)
    app.run(host='0.0.0.0', port=port, threaded=True)