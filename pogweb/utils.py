"""
Copyright 2021 K.M Ahnaf Zamil

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

from datetime import datetime
import pogweb
import logging


def render_banner(ip: str, port: int) -> None:
    banner = f"""
██████╗  ██████╗  ██████╗ ██╗    ██╗███████╗██████╗            v{pogweb.__version__}
██╔══██╗██╔═══██╗██╔════╝ ██║    ██║██╔════╝██╔══██╗           © K.M Ahnaf Zamil {datetime.now().year} 
██████╔╝██║   ██║██║  ███╗██║ █╗ ██║█████╗  ██████╔╝           Thank you for using PogWeb
██╔═══╝ ██║   ██║██║   ██║██║███╗██║██╔══╝  ██╔══██╗           Stay pog, POGGIES!!!!
██║     ╚██████╔╝╚██████╔╝╚███╔███╔╝███████╗██████╔╝           
╚═╝      ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═════╝            Running with Waitress on http://{ip}:{port}/
                                                    
    """
    print(banner)


def handle_not_found(environ, start_fn) -> list:
    start_fn("404 Not Found", [("Content-Type", "text/plain")])
    return ["404 Not Found"]


def log_request(logger: logging.Logger, environ: dict, status_code: int = 200) -> None:
    logger.debug(
        f"{environ['REQUEST_METHOD']}: {environ['SERVER_PROTOCOL']} '{environ['PATH_INFO']}{'?' + environ['QUERY_STRING'] if environ['QUERY_STRING'] else ''}' [{status_code}]"
    )
