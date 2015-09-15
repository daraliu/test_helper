from __future__ import print_function
import hashlib


class TestFailure(Exception):
    pass


class PrivateTestFailure(Exception):
    pass


class Test(object):
    passed = 0
    numTests = 0
    failFast = False
    private = False

    @classmethod
    def setFailFast(cls):
        cls.failFast = True

    @classmethod
    def setPrivateMode(cls):
        cls.private = True

    @classmethod
    def assertTrue(cls, result, msg=""):
        cls.numTests += 1
        if result is True:
            cls.passed += 1
            print("1 test passed.")
        else:
            print("1 test failed. {}".format(msg))
            if cls.failFast:
                if cls.private:
                    raise PrivateTestFailure(msg)
                else:
                    raise TestFailure(msg)

    @classmethod
    def assertEquals(cls, var, val, msg=""):
        cls.assertTrue(var == val, msg)

    @classmethod
    def assertEqualsHashed(cls, var, hashedVal, msg=""):
        cls.assertEquals(cls._hash(var), hashedVal, msg)

    @classmethod
    def printStats(cls):
        print("{0} / {1} test(s) passed.".format(cls.passed, cls.numTests))

    @classmethod
    def _hash(cls, x):
        return hashlib.sha1(str(x).encode("utf-8")).hexdigest()
