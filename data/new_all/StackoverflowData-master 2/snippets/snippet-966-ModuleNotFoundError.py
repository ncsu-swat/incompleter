#Source: https://stackoverflow.com/questions/63715326/functional-logger-raises-filenotfounderror-in-pytest
# test_code.py
import unittest

from workers.code import Worker


class CodeTest(unittest.TestCase):
    def test__init__(self):
        worker = Worker()
        assert worker.logger.handlers  # this fails with FileNotFound Error

    def test_do_something(self):
        worker = Worker()  # this also fails even when delay=True on FileHandler
        assert worker.do_something()