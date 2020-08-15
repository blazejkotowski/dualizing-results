from jinja2 import Environment, FileSystemLoader
import os
import random

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'layouts')
env = Environment(loader = FileSystemLoader(templates_dir))

main_template = env.get_template('main_layout.html')
num_examples = 50
for i in range(1, num_examples+1):
  filename = os.path.join(root, 'examples', f"{i}.html")
  with open(filename, 'w') as fh:
    fh.write(main_template.render(index=i))


listening_test = env.get_template('listening_test.html')
num_listening_tests = 10
used_examples = [-1]
for i in range(1, num_listening_tests+1):
  orig_index = -1
  while orig_index in used_examples:
    orig_index = random.randint(0, num_examples) + 1

  random1_index = -1
  while random1_index in [-1, orig_index]:
    random1_index = random.randint(0, num_examples) + 1
  random2_index = -1
  while random2_index in [-1, orig_index, random1_index]:
    random2_index = random.randint(0, num_examples) + 1


  filename = os.path.join(root, 'tests', f"{i}.html")

  with open(filename, 'w') as fh:
    fh.write(listening_test.render(
      i=i,
      orig_index=orig_index,
      random_index_1=random1_index,
      random_index_2=random2_index,
      num_listening_tests=num_listening_tests,
      ))

  used_examples.append(orig_index)