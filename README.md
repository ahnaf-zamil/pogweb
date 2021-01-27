# PogWeb

A simple web framework for all of you POG people out there!

# Usage

```python
from pogweb import WebApp, Request


# Instantiate web app
app = WebApp()


# Flask-styled endpoints
@app.endpoint("/")
def main(request: Request) -> str:
    return "<h1>Hello world!</h1>"

# Django-styled endpoints
def another_route(request: Request) -> str:
    return "<h1>This is another route</h1>"

app.add_endpoint("/another-route", another_route)


# Running the app on 127.0.0.1:69
app.run(port=69)
```

# Deploying/Using production servers

By default, PogWeb runs a Waitress production server (because I was too lazy to write a development server or use Wekrzeug's one) but you can use your own servers by using

```python
if __name__ == "__name__":
    app.run()
```

before `app.run()`. This will only run the server when you run the module itself. But if you import it from some other module that you might use as a wrapper for some other production server, that is possible too.

For example, with gunicorn, you can run the web application like this:

```sh
$ gunicorn -w 4 main:app
```

Here, `main` (on the left side if the colon) is the name of the file (main.py) and `app` on the right side is the instance of the PogWeb application.

# License

Copyright 2021 K.M Ahnaf Zamil

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
