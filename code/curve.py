import interpolation as intrpltn
import matplotlib.pyplot as plt
import img_reader as img_r

def draw_curve(src, num=1, dim=(600,450)):
    reader = img_r.Img_reader(src)
    fig = plt.figure()
    for i in range(len(reader.objects)):
        if len(reader.objects[i])>=3*num:
            xs = [ a[0] for a in reader.objects[i] ]
            ys = [ a[1] for a in reader.objects[i] ]

            # we can use less points than all pixels
            x = [xs[i] for i in range(0,len(xs),num)]
            y = [ys[i] for i in range(0,len(ys),num)]

            # interpolating polynomials
            sx = intrpltn.Interpolation( list( intrpltn.t(len(x)) ), x)
            sy = intrpltn.Interpolation( list( intrpltn.t(len(y)) ), y)

            # points from interpolating polynomial for coordinates
            xx = [sx(c) for c in intrpltn.t(len(x)*1000)]
            yy = [sy(c) for c in intrpltn.t(len(y)*1000)]

            # set point 0,0 on the top left corner
            plt.xlim([0,dim[0]])
            plt.ylim([dim[1],0])
            
            plt.plot(xx,yy)

    plt.show()
