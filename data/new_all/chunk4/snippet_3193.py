#Source: https://stackoverflow.com/questions/77499720/cloudpickles-load-method-results-in-filenotfounderror-on-linux-systems
import os
import cloudpickle

filename = 'name.ext'
assert(os.path.isfile(filename))
with open(filename, 'rb') as file:
    deserialized_object = cloudpickle.load(file)