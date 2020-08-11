from jinja2 import Environment, FileSystemLoader
import os

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root)
env = Environment(loader = FileSystemLoader(templates_dir))
template = env.get_template('layout.html')

for i in range(1, 51):
  filename = os.path.join(root, 'examples', f"{i}.html")
  with open(filename, 'w') as fh:
    fh.write(template.render(index=i))