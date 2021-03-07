#!/usr/bin/env python3
from calc_api import app

# checks to see if name of the package is main package.
if __name__ == '__main__':
    app.run(host="0.0.0.0") # host 0.0.0.0 - expose api to WAN.