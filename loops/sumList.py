import unittest


"""
    Gitt en liste med tall, summer opp alle de positive elementene i listen.
    Hvis listen er tom skal svaret være 0.
"""
def positive_sum(liste):
    num = 0
    for x in liste:
        if x > 0:
            num + x
    return num

class CountingList(unittest.TestCase):
    def basic_test_cases(self):
        self.assertEqual(positive_sum([1,2,3,4,5]),15)
        self.assertEqual(positive_sum([1,-2,3,4,5]),13)
        self.assertEqual(positive_sum([-1,2,3,4,-5]),9)
        
    def empty_case(self):
        self.assertEqual(positive_sum([]),0)      
        
    def negative_case(self):
        self.assertEqual(positive_sum([-1,-2,-3,-4,-5]),0)

        

if __name__ == '__main__':
    unittest.main()