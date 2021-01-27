"""
Copyright 2021 K.M Ahnaf Zamil

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

from jinja2 import Template


class Renderer(object):
    """Responsible for rendering templates with Jinja2"""

    def __init__(self, work_dir: str) -> None:
        self._dir = work_dir

    def read_html_file(self, file_name: str) -> str:
        with open(self._dir + file_name) as f:
            return f.read()

    def render_html_file(self, file_name: str, kwargs: dict) -> str:
        data = self.read_html_file(file_name)
        template = Template(data)
        return template.render(kwargs)
