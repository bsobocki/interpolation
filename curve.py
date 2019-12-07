import interpolation as intrpltn
import matplotlib.pyplot as plt
import img_reader as img_r

def draw_curve(src, num, dim=(600,450)):
    reader = img_r.Img_reader(src)
    fig = plt.figure()
    for i in range(len(reader.objects)):
        if len(reader.objects[i])>=3*num:
            xs = [ a[0] for a in reader.objects[i] ]
            ys = [ a[1] for a in reader.objects[i] ]

            x = []
            y = []

            for i in range(0,len(xs),num):
                x.append(xs[i])
            for i in range(0,len(ys),num):
                y.append(ys[i])

            sx = intrpltn.Interpolation( list( intrpltn.t(len(x)) ), x)
            sy = intrpltn.Interpolation( list( intrpltn.t(len(y)) ), y)

            xx = [sx(c) for c in intrpltn.t(len(x)*1000)]
            yy = [sy(c) for c in intrpltn.t(len(y)*1000)]

            plt.plot(xx,yy)
            plt.xlim([0,dim[0]])
            plt.ylim([dim[1],0])

    plt.show()
