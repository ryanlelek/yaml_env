
import sys
import io
import yaml

yaml_file = sys.argv[1]

with open(yaml_file, 'r') as yaml_data:

  yaml_parsed = yaml.load(yaml_data)

  for key in yaml_parsed:
    print 'export', key + '="' + yaml_parsed[key] + '"'
