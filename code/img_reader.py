import matplotlib.image as plt_img
import matplotlib.pyplot as plt
import re

class Img_reader:
    objects = []
    img = []

    def __init__(self, src):
        prog = re.compile(".+\.py")
        if prog.match(src) : 
            self.img = plt_img.imread(src)
            self._read_objects()
            self._merge_objects()

    def _merge_objects(self):
        for i in range(len(self.objects)):
            for j in range(len(self.objects)):
                if not j==i:
                    conn = self._are_connected(self.objects[i], self.objects[j])
                    if conn == 0+2: 
                        self.objects[i].reverse()
                        self.objects[i] += self.objects[j].copy()
                        self.objects[j] = []
                    elif conn == 1+2: 
                        self.objects[i] += self.objects[j].copy()
                        self.objects[j] = []
                    elif conn == 0+4:
                        self.objects[j] += self.objects[i].copy()
                        self.objects[i] = []
                    elif conn == 1+4:
                        self.objects[j].reverse()
                        self.objects[i] += self.objects[j].copy()
                        self.objects[j] = []
        self.objects = [obj for obj in self.objects if len(obj) > 0]


    def _are_connected(self, obj1, obj2):
        # if one of them are empty there aren't connected 
        if len(obj1) == 0 or len(obj2) == 0: return -1

        # predicates
        start1_start2 = self._is_neighbor( obj1[0], obj2[0] )
        start1_end2 = self._is_neighbor( obj1[0], obj2[ len(obj2)-1 ] )
        end1_start2 = self._is_neighbor( obj1[ len(obj1)-1 ], obj2[0] )
        end1_end2 = self._is_neighbor( obj1[ len(obj1)-1 ], obj2[ len(obj2)-1 ] )

        # start1 == 0, end1 == 1, start2 == 2, end2 == 4
        if start1_start2: return 0+2
        if end1_start2: return 1+2
        if start1_end2: return 0+4
        if end1_end2: return 1+4

        return -1
                        

    def _is_neighbor(self, a1,a2):
        return abs(a1[0] - a2[0]) <=1 and abs(a1[1] - a2[1]) <= 1


    def _read_objects(self):
        for y in range(self.img.shape[0]):
            for x in range(self.img.shape[1]):
                if self._not_white(x, y):
                    self._read_object(x, y)


    def _read_object_rek(self, x, y): # DFS
        can_go_right = x+1 < self.img.shape[1]
        can_go_down = y+1 < self.img.shape[0]
        can_go_up = y > 0
        can_go_left = x > 0
        pixels = []
        if self._not_white(x, y):
            pixels.append( (x, y) )
            # colour readed pixel on white
            self.img[y][x] = self._white_pixel()
            
            # up
            if can_go_up:
                pixels += self._read_object(x, y-1)
            # right
            if can_go_right:
                pixels += self._read_object(x+1, y)
            # down
            if can_go_down:
                pixels += self._read_object(x, y+1)
            # left-down
            if can_go_left and can_go_down:
                pixels += self._read_object(x-1, y+1)
            # right-up
            if can_go_right and can_go_up :
                pixels += self._read_object(x+1, y-1)
            # right-down
            if can_go_right and can_go_down:
                pixels += self._read_object(x+1, y+1)
            # left
            if can_go_left:
                pixels += self._read_object(x-1, y)
            # left-up
            if can_go_left and can_go_up:
                pixels += self._read_object(x-1, y-1)

        self.objects.append(pixels)


    def _read_object(self, x, y):
        # predicates
        can_go_right = x+1 < self.img.shape[1]
        can_go_down = y+1 < self.img.shape[0]
        can_go_up = y > 0
        can_go_left = x > 0

        # list of black pixels
        blacks = []

        # the beginning of the contour
        start = (x,y)
        # the end of the contour
        end = (x,y)

        # go for a walk and get all pixels!
        while self._not_white(x, y):
            # add pixel to the list
            blacks.append((x,y))

            # set current pixel as white
            self.img[y][x] = self._white_pixel()

            # check next pixel (first)
            if can_go_up and self._not_white(x, y-1):
                y -= 1
            elif can_go_right and self._not_white(x+1, y): 
                x += 1
            elif can_go_down and self._not_white(x, y+1): 
                y += 1
            elif can_go_left and can_go_down and self._not_white(x-1, y+1): 
                x, y = x-1, y+1
            elif can_go_right and can_go_up and self._not_white(x+1, y-1): 
                x, y = x+1, y-1
            elif can_go_right and can_go_down and self._not_white(x+1, y+1): 
                x, y = x+1, y+1
            elif can_go_left and self._not_white(x-1, y): 
                x -= 1
            elif can_go_left and can_go_up and self._not_white(x, y): 
                x, y = x-1, y-1
                
        if len(blacks) > 0: 
            self.objects.append(blacks)


    def _not_white(self, x, y):
        return not all(self.img[y][x])


    def _white_pixel(self):
        return [1.0, 1.0, 1.0]

"""
    def black_neighbors(self, x, y):
        neighbors = []
        can_go_right = x+1 < self.img.shape[1]
        can_go_down = y+1 < self.img.shape[0]
        can_go_up = y > 0
        can_go_left = x > 0
        if can_go_right and self._not_white(x+1, y): neighbors.append((x+1, y))
        if can_go_down  and self._not_white(x, y+1) : neighbors.append((x, y+1))
        if can_go_right and can_go_down and self._not_white(x+1, y+1): neighbors.append(x+1, y+1)
        if can_go_left  and can_go_down and _not_white(x-1, y): neighbors.append((x-1, y))
        if can_go_left  and _not_white(x-1, y) : neighbors.append((x-1, y))
        if can_go_left  and can_go_up and self._not_white(x-1, y-1): neighbors.append((x-1, y-1))
        if can_go_up    and self._not_white(x, y-1): neighbors.append((x, y-1))
        if can_go_up    and can_go_right and self._not_white(x+1, y-1): neighbors.append((x+1, y-1))
"""