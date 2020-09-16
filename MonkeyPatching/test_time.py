import unittest
from . practice_date_time import current_time
import datetime


class TestTime(unittest.TestCase):

    def currernt_time_patch(self):
        return datetime.datetime.utcnow()
    def test_current_time(self):
        result = self.mon
        excepted = datetime.datetime.utcnow()
        import pdb
        pdb.set_trace()

        self.assertEqual(result, excepted)



if __name__ == '__main__':
    unittest.main()
