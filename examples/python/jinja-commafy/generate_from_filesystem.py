from jinja2 import Environment, FileSystemLoader
import os

root = os.path.dirname(os.path.abspath(__file__))
env = Environment( loader = FileSystemLoader(root) )

env.filters['commafy'] = lambda v: "{:,}".format(v)

template = env.get_template('page.html')


print(template.render(
        distance = 12345678,
    ))

