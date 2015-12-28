# pyCAOS - An organic chemistry reaction simulator, written in Python
# Copyright (C) 2014, 2015 Dan Obermiller
#
# The full license is available in the root directory of the repository

__author__ = "Dan Obermiller"

__all__ = ['test_acid_base_reactions', 'test_CML', 'test_compounds',
           'test_isomorphism', 'test_periodic_helpers', 'test_components']


# Utility methods for running tests
def helper(globs, verbosity=1):
    import sys
    import types
    import unittest

    test_classes_to_run = [value for key, value in globs.items()
                           if (isinstance(value, (type, types.ClassType))
                               and issubclass(value, unittest.TestCase))]

    loader = unittest.TestLoader()
    big_suite = unittest.TestSuite(loader.loadTestsFromTestCase(test_class)
                                   for test_class in test_classes_to_run)

    runner = unittest.TextTestRunner(sys.stdout, verbosity=verbosity)
    runner.run(big_suite)


def stdout_capture():
    import contextlib
    import sys
    import io

    @contextlib.contextmanager
    def capture():
        oldout, olderr = sys.stdout, sys.stderr

        try:
            out=[io.StringIO(), io.StringIO()]
            sys.stdout, sys.stderr = out
            yield out

        finally:
            sys.stdout, sys.stderr = oldout, olderr
            out[0] = out[0].getvalue()
            out[1] = out[1].getvalue()
    return capture


def raises(f, args=None, kwargs=None, exc_type=Exception):
    if args is None:
        args = []
    if kwargs is None:
        kwargs = {}
    try:
        f(*args, **kwargs)
    except exc_type:
        return True
    else:
        return False
