from __future__ import print_function
import hashlib


class testfailure(Exception):
    pass


class privatetestfailure(Exception):
    pass


class test(object):
    passed = 0
    numtests = 0
    failfast = False
    private = False

    @classmethod
    def setfailfast(cls):
        cls.failfast = True

    @classmethod
    def setprivatemode(cls):
        cls.private = True

    @classmethod
    def asserttrue(cls, result, msg=""):
        cls.numtests += 1
        if result is True:
            cls.passed += 1
            print("1 test passed.")
        else:
            print("1 test failed. {}".format(msg))
            if cls.failfast:
                if cls.private:
                    raise privatetestfailure(msg)
                else:
                    raise testfailure(msg)

    @classmethod
    def assertequals(cls, var, val, msg=""):
        cls.asserttrue(var == val, msg)

    @classmethod
    def assertequalshashed(cls, var, hashed_val, msg=""):
        cls.assertequals(cls._hash(var), hashed_val, msg)

    @classmethod
    def printstats(cls):
        print("{0} / {1} test(s) passed.".format(cls.passed, cls.numtests))

    @classmethod
    def _hash(cls, x):
        return hashlib.sha1(str(x).encode("utf-8")).hexdigest()
