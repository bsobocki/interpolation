import math

"""
NIFS3 (pl. Naturalna Interpolacyjna Funkcja Sklejana 3-go stopnia)

Polynomial interpolating function using given points (x, f(x)) 

Spline : https://en.wikipedia.org/wiki/Spline_interpolation#Algorithm_to_find_the_interpolating_cubic_spline
"""
class Interpolation:
    def __init__(self,x,y):
        """ 
        x, y : lists of coordinates 
        """
        self.x = x # sorted with ascending order
        self.y = y # corresponding values ​​= f(x)
        """ 
        Moments :  s''(Xi) where s(X) is the interpolating polynomial needed to calculate s(x) 
        """
        self.Momoents = Interpolation.table_of_moments(x,y)

    """ make object callable """
    def __call__(self,xx):
        for i in range(1,len(self.x)):
            """ check which part of the function you should use """
            if xx <= self.x[i]:
                return Interpolation.s(i, self.x, self.y, self.Momoents,xx)
        return Interpolation.s(len(self.x)-1, self.x, self.y, self.Momoents,xx)

    @staticmethod
    def f_table(x,y):
        """ returns 2d list contains differential quotients of the interpolated functions """
        n = len(x)
        f = []
        for i in range(0,n):
            f += [[y[i], None, None]]
        for i in range(1,n):
            f[i][1] = ( f[i][0] - f[i-1][0] ) / (x[i] - x[i-1])
        for i in range(2,n):
            f[i][2] = ( f[i][1] - f[i-1][1] ) / (x[i] - x[i-2])
        return f

    @staticmethod
    def p_q_table(x,y):
        """ returns lists p and q needed to calculate moments (Mi - ith moment = s''(Xi)) """
        n = len(x)-1
        f = Interpolation.f_table(x,y)
        p,q = [None],[None]
        p += [3 * f[2][2]]                              # p1
        q += [(1 - (x[1]-x[0]) / (x[2]-x[0]) ) / 2]     # q1
        for i in range(2,n):
            li = ( x[i]-x[i-1] ) / (x[i+1]-x[i-1])
            di = 6 * f[i+1][2]
            q += [( 1 - li ) / (2 + li*q[i-1])]
            p += [(di - li*p[i-1]) / ( 2 + li*q[i-1] )]
        return p,q

    @staticmethod
    def table_of_moments(x,y):
        """ 
        Moments of the interpolating polynomial Mi == s''(Xi) 
        where s(Xi) is the interpolate polynomial
        """
        n = len(x)
        Momoents = list(range(0,n))
        Momoents[n-1] = 0
        Momoents[0] = 0
        p,q = Interpolation.p_q_table(x,y)
        for i in range(n-2, 0, -1):
            Momoents[i] = p[i] + q[i]*Momoents[i+1] 
        return Momoents

    @staticmethod
    def s(k, x, y, Momoents, xx):
        """ k-th part of the interpolating polynomial """
        h = x[k] - x[k-1]
        x_xk = xx - x[k-1]
        xk_x = x[k] - xx
        return 1/h*( 1/6 * Momoents[k-1] * xk_x**3  +  
                     1/6 * Momoents[k]   * x_xk**3  +  
                     ( y[k-1] - 1/6 * Momoents[k-1] * (h**2) ) * xk_x +
                     ( y[k]   - 1/6 * Momoents[k]   * (h**2) ) * x_xk )


""" sx and sy arguments generator """
def t(n):
    for i in range (0, n):
        yield i/n
