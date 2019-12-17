import unittest as ut
from ../code/img_reader import Img_reader

class Test_neighbors_points(ut.TestCase):
    reader = Img_reader("")
    
    def test_neighbors1(self):
        self.assertTrue(self.reader._is_neighbor((2,2), (2,1)))

    def test_neighbors2(self):
        self.assertFalse(self.reader._is_neighbor((0,1), (2,1)))

    def test_neighbors3(self):
        self.assertTrue(self.reader._is_neighbor((2,3), (3,2)))

    def test_neighbors4(self):
        self.assertTrue(self.reader._is_neighbor((2,2), (2,3)))


class Test_connection_objects(ut.TestCase):
    reader = Img_reader("")

    def test_no_connection(self):
        self.assertEqual(self.reader._are_connected([],[]), -1)

    def test_connection1(self):
        self.assertEqual(
            self.reader._are_connected( 
                obj1=[(0,1), (0,2), (0,3)],   
                obj2=[(1,1), (1,2), (2,2), (2,3)] ),
                1+1)

    def test_connection2(self):
        self.assertEqual(
            self.reader._are_connected(
                obj1=[(0,1), (1,1), (2,2)],
                obj2=[(2,1), (3,0), (3,1), (3,2)] ),
                1+2)

    def test_connection3(self):
        self.assertEqual(
            self.reader._are_connected(
                obj1=[(2,1), (3,0), (3,1), (3,2)],
                obj2=[(2,3), (1,3), (0,3)] ),
                1+2)

    def test_connection4(self):
        self.assertEqual(
            self.reader._are_connected(
                obj1=[(2,1), (3,0), (3,1), (3,2)],
                obj2=[(0,3),(1,3), (2,3)] ),
                1+4)

class Test_merge_objects(ut.TestCase):

    def do_test(self, objects, expected):
        #init
        reader = Img_reader("")
        reader.objects = objects
        #do
        reader._merge_objects()
        #test
        self.assertEqual(reader.objects, expected)


    def test_merge_two_objects1(self):
        self.do_test(
            objects=[[(0,1),(0,2),(0,3)],  [(1,1),(1,2),(2,2),(2,3)]],
            expected=[[(0,3),(0,2),(0,1),(1,1),(1,2),(2,2),(2,3)] ])

    def test_merge_two_objects2(self):
        self.do_test(
            objects=[[(0,1),(1,1),(2,2)],  [(2,1),(3,0),(3,1),(3,2)]],
            expected=[[(0,1),(1,1),(2,2),(2,1),(3,0),(3,1),(3,2)]])
    
    def test_merge_three_objects_1(self):
        """
        [1 0 0 3]
        [0 1 0 3]
        [0 2 1 3]
        [2 2 2 0]
        """
        self.do_test(
            objects=[[(0,1),(1,1),(2,2)],  [(2,1),(3,0),(3,1),(3,2)],  [(2,3),(1,3),(0,3)]],
            expected=[[(0,1),(1,1),(2,2),(2,1),(3,0),(3,1),(3,2),(2,3),(1,3),(0,3)]])

    def test_merge_three_objects_2(self):
        """ 
        [1 0 0 3]
        [0 1 0 3]
        [0 2 1 3]
        [2 2 2 0]
        """
        self.do_test(
            objects=[[(0,1),(1,1),(2,2)],  [(2,1),(3,0),(3,1),(3,2)],  [(0,3),(1,3), (2,3)]],
            expected=[[(0,1),(1,1),(2,2),(2,1),(3,0),(3,1),(3,2),(2,3),(1,3),(0,3)]])


if __name__ == "__main__":
    ut.main()