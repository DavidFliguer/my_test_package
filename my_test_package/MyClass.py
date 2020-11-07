import os
import json


class MyClass:

    def do_work(self):
        path = os.path.join(os.path.dirname(__file__), 'my_file.txt')
        with open(path, 'r') as content_file:
            content = content_file.read()
        print(content)

    def do_some_other_work(self):
        path = os.path.join(os.path.dirname(__file__), 'data', 'my_other_file.txt')
        with open(path, 'r') as content_file:
            content = content_file.read()
        print(content)

    def do_work_problematic(self):
        # This won't work since when packaging, the file is not included
        path = os.path.join(os.path.dirname(__file__), 'some_not_included_json.json')
        with open(path, 'r') as content_file:
            content = json.load(content_file)  # content_file.read()
        print(content["data"])
