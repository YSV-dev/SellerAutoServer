from app.routes.abc import IPage


class SchemePage(IPage):
    def __init__(self):
        super().__init__()
        self.html_file = None
        self.page_name = "None"
        self.data = {}