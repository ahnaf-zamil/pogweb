"""
Copyright 2021 K.M Ahnaf Zamil

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

from pogweb import WebApp, Request

# Instantiate web app
app = WebApp()

# Flask-styled routes


@app.endpoint("/")
def main(request: Request):
    # Rendering HTML with data
    return app.render_html("index.html", name="Ahnaf")


@app.endpoint("/api")
def api(request: Request):
    # Returning JSON
    return {"status": 200, "msg": "Welcome to Pogweb API"}


@app.endpoint("/search")
def query(request: Request):
    # Accessing query arguments
    return f"<h1>You searched for {request.query_args['q']}</h1>"


# Django styled routes


def another_route(request: Request):
    return "This is a django styled route"


app.add_endpoint("/another-route", another_route)


# Running the server (Waitress)
app.run(port=80)