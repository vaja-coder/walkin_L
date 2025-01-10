from configurs import app
app = app

if __name__ == '__main__':
    from routs import *
    app.run(debug=True)