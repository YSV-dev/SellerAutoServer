from abc import ABC

from flask import render_template


class IPage(ABC):
    def __init__(self):
        self.html_file = None
        self.page_name = "None"
        self.data = {}

    def render_page(self):
        return render_template(self.html_file, page_name=self.page_name, data=self.data)

