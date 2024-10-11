# backend/models/banner.py

class Banner:
    def __init__(self, banner1="", banner2="", header=""):
        self.banner1 = banner1
        self.banner2 = banner2
        self.header = header

    def get_banner1(self):
        return self.banner1

    def get_banner2(self):
        return self.banner2

    def get_header(self):
        return self.header

    def set_banner1(self, banner1):
        self.banner1 = banner1

    def set_banner2(self, banner2):
        self.banner2 = banner2

    def set_header(self, header):
        self.header = header
