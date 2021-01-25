"""
Copyright 2021 K.M Ahnaf Zamil

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

from waitress import serve
from pogweb.models import Request
from pogweb.utils import Utils
from pogweb.renderer import Renderer
from pogweb.errors import EndpointError

import json
import typing
import logging
import socket
import traceback

__all__: typing.Final = ["WebApp"]


class WebApp(object):
    def __init__(self) -> None:
        self.routes = {}
        self._logger = logging.getLogger("pogweb")
        self._not_found = Utils.handle_not_found
        self._renderer = Renderer("./html/")

    def endpoint(self, route: str):
        """Add an endpoint handler to the application (Non-decorator styled)"""

        def decorator(func: typing.Callable):
            if route in self.routes:
                raise EndpointError(f"The endpoint {route} already exists")
            self.routes[route] = func
            return func

        return decorator

    def add_endpoint(self, route: str, func: typing.Callable) -> None:
        """Add an endpoint handler to the application (Non-decorator styled)"""
        if route in self.routes:
            raise EndpointError(f"The endpoint {route} already exists")
        self.routes[route] = func
        return func

    def handle_request(self, environ, start_fn, endpoint) -> typing.List[str]:
        """Handles all HTML/JSON HTTP requests"""
        if not endpoint == Utils.handle_not_found:
            request = Request(environ)
            data = endpoint(request)
            if isinstance(data, dict):
                start_fn("200 OK", [("Content-Type", "application/json")])
                data = json.dumps(data)
            else:
                start_fn("200 OK", [("Content-Type", "text/html")])
            Utils.log_request(self._logger, environ, 200)
            return [data]
        else:
            Utils.log_request(self._logger, environ, 404)
            return self._not_found(environ, start_fn)

    def handle_css_or_js(self, environ, start_fn) -> typing.List[str]:
        """Handles all HTTP requests for CSS or JS files"""
        path_to_file = environ["PATH_INFO"]
        extension = "javascript" if path_to_file.lower().endswith("js") else "css"
        try:
            with open("." + path_to_file) as f:
                start_fn("200 OK", [("Content-Type", f"text/{extension}")])
                Utils.log_request(self._logger, environ)
                return [f.read()]
        except:
            start_fn("404 Not Found", [("Content-Type", f"text/{extension}")])
            Utils.log_request(self._logger, environ, 404)
            return [f"{extension.capitalize()} file not found"]

    def handle_asset(self, environ, start_fn) -> typing.List[str]:
        """Handles all HTTP requests for asset-related files"""
        path_to_img = environ["PATH_INFO"]
        try:
            with open("." + path_to_img, "rb") as f:
                start_fn("200 OK", [("Content-Type", "text/webp")])
                Utils.log_request(self._logger, environ)
                return [f.read()]
        except:
            start_fn("404 Not Found", [("Content-Type", "text/plain")])
            Utils.log_request(self._logger, environ, 404)
            return ["Image file not found"]

    def render_html(self, file_name: str, **kwargs) -> str:
        """Renders HTML files/templates"""
        renderer = self._renderer
        data = renderer.render_html_file(file_name, kwargs)
        return data

    def set_html_dir(self, work_dir: str) -> None:
        """Changes the HTML file directory. The default is 'html/'"""
        self._renderer = Renderer(work_dir + "/")

    def __call__(self, environ, start_fn) -> typing.List[str]:
        """Called on EVERY single HTTP request"""
        try:
            if "text/html" in environ["HTTP_ACCEPT"]:
                endpoint = self.routes.get(environ.get("PATH_INFO")) or self._not_found
                return self.handle_request(environ, start_fn, endpoint)
            elif (
                "text/css" in environ["HTTP_ACCEPT"]
                or "text/javascript" in environ["HTTP_ACCEPT"]
            ):
                return self.handle_css_or_js(environ, start_fn)
            else:
                return self.handle_asset(environ, start_fn)
        except Exception:
            Utils.log_request(self._logger, environ, 500)
            traceback.print_exc()
            start_fn("500 Internal Server Error", [("Content-Type", "text/plain")])
            return ["500 Internal Server Error"]

    def run(self, *, port=8080) -> None:
        """Runs the application on Waitress server"""
        ip = socket.gethostbyname(socket.gethostname())
        logging.basicConfig(
            level=logging.DEBUG, format=f"%(name)s>> {ip} - %(message)s"
        )
        Utils.render_banner(ip, port)
        serve(self, port=port, _quiet=True)
