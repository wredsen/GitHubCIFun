# content of test_sample.py
import numpy as np
from githubcifun import ContentClass
 
def test_config():
    content_test = ContentClass("hallo")
    assert content_test.name != "ciao"
