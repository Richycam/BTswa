# backend/models/map.py

class Map:
    def __init__(self, map1=""):
        self.map1 = map1

    def get_map(self):
        return self.map1

    def set_map(self, map_content):
        self.map1 = map_content
