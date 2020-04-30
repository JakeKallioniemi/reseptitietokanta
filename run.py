import sys

from application import app

if __name__ == '__main__':
    debug_on = len(sys.argv) == 2 and sys.argv[1] == '--debug'
    app.run(debug=debug_on)
