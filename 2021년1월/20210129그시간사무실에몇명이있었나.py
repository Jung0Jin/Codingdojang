# https://codingdojang.com/scode/418?answer_mode=hide

import unittest

def sec(src):
    h, m, s = map(int, src.split(":"))
    return h*60*60+m*60+s


class Office:
    def __init__(self):
        self.emp = []

    def add(self, e):
        self.emp.append(e)

    def count(self, t):
        t = sec(t)
        result = 0
        for e in self.emp:
            if e.s <= t <= e.e:
                result += 1
        return result


class Employee:
    def __init__(self, s, e):
        self.s = sec(s)
        self.e = sec(e)


def compute(src, t):
    office = Office()
    src = src.strip()
    for line in src.split("\n"):
        s, e = line.split(" ")
        office.add(Employee(s, e))
    return office.count(t)


class Test(unittest.TestCase):
    def test1(self):
        office = Office()
        e1 = Employee("09:12:23", "11:14:35")
        office.add(e1)
        self.assertEquals(1, office.count("11:05:20"))

    def test2(self):
        src = """
09:12:23 11:14:35
10:34:01 13:23:40
10:34:31 11:20:10
"""     
        self.assertEquals(3, compute(src, "11:05:20"))


if __name__ == "__main__":
    unittest.main()
