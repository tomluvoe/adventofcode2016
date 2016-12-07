import numpy

def day3_1():
    triangles = 0
    with open('day3.dat','r') as data:
        for d in data:
            xyz = sorted(map(int, d.split()))
            if int(xyz[0]) + int(xyz[1]) > int(xyz[2]):
                triangles += 1
    print "Number of triangles #1:", triangles

def day3_2():
    triangles = 0
    data = numpy.loadtxt('day3.dat')
    data = numpy.vsplit(data,data.shape[0]/3)
    for d in data:
        d = numpy.transpose(d)
        for t in d:
            xyz = sorted(map(int, t))
            if int(xyz[0]) + int(xyz[1]) > int(xyz[2]):
                triangles += 1
    print "Number of triangles #2:", triangles

if __name__ == "__main__":
    day3_1()
    day3_2()
