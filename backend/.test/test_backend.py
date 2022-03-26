import sys
sys.path.append('../')
from app import *


#
# unit test to verify watermark_image() converts image 
#
def test_watermark_image():
    test_input = open('test_input','r').read()
    test_output = open('test_output','r').read()

    assert watermark_image(test_input, "test") == test_output 