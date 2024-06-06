import pytest
import os


if __name__ == '__main__':
    pytest.main(["-s", "-v", os.path.join(os.path.dirname(__file__), "testcase")])
