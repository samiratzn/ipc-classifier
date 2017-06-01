"""This path modification is intended to give context to the test suite and allow the import
of the package
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sample
