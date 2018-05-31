import sys;

print(sys.path)
print(sys.modules)

'''
sys.modules is a dictionary of all the modules that have been imported in this Python instance. The keys are
the module names as strings; the values are the module objects themselves.
'''