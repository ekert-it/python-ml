'''Alle verfügbaren Module anziegen'''
import sys

# List all available modules:
module_list=sys.modules
print (type(module_list))
for module in sorted(module_list):
    print (module)
