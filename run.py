#!/usr/bin/env python
from simple_app import app

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=65440, debug=True, use_reloader=True)