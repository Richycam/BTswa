# backend/models/siem.py

class SIEM:
    def __init__(self, tool="", link=""):
        self.tool = tool
        self.link = link

    def get_tool(self):
        return self.tool

    def get_link(self):
        return self.link

    def set_tool(self, tool):
        self.tool = tool

    def set_link(self, link):
        self.link = link
