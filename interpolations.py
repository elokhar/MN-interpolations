import random
import numpy as np
import math as m  
import matplotlib.pyplot as plt
import pandas as pd


def generate_plot(csv_name, method, points_percent, points_placement):
    
    data = pd.read_csv(csv_name+".csv")
    distances = data["Dystans (m)"]
    heights = data["Wysokość (m)"]

    method_str = translate(method)
    placement_str = translate(points_placement)

    plt.ylim(ymin=min(heights),ymax=max(heights)*1.01)
    plt.plot(distances,heights)
    ip_heights = interpolate(method,distances,heights,points_percent,points_placement)
    plt.plot(distances,ip_heights)
    plt.title(method_str+", p="+str(points_percent)+"%, "+placement_str)
    plt.savefig(method+"_"+str(points_percent)+"%_"+points_placement+"_"+csv_name)
    plt.show()
    


def translate(text):    
    return {
        "even": "rozmieszenie równomierne",
        "random": "rozmieszenie losowe",
        "chebyshev": "węzły Czebyszewa",
        "lagrange": "Interpolacja Lagrange'a",
        "spline": "Interpolacja splajnami"
    }[text] 


def interpolate(method, data_x, data_y, points_percent, points_placement):
    data_len = len(data_x)
    ip_xs = []
    ip_ys = []
    result = []
    points_distance = int(100/points_percent)
    if(points_placement=="even"):       
        for i in range(0,data_len,points_distance):
            ip_xs.append(data_x[i])
            ip_ys.append(data_y[i])
    elif(points_placement=="chebyshev"):
        n = int(data_len*points_percent/100)
        a = 0
        b = data_len-1
        for k in range(n,0,-1):
            index = int((a+b)/2+(b-a)/2*m.cos((2*k-1)*m.pi/(2*n)))
            if(data_x[index] in ip_xs):
                continue
            ip_xs.append(data_x[index])
            ip_ys.append(data_y[index])
    elif(points_placement=="random"):
        ip_xs.append(data_x[0])
        ip_ys.append(data_y[0])
        points_count = data_len/(100/points_percent)-1
        while(points_count>0):
            rand_index = int(random.uniform(0,data_len-1))
            rand_x = data_x[rand_index]
            if(rand_x not in ip_xs):
                if rand_x>ip_xs[-1]:
                    ip_xs.append(rand_x)
                    ip_ys.append(data_y[rand_index])
                else:
                    for i in range(len(ip_xs)):
                        if rand_x<ip_xs[i]:
                            ip_xs.insert(i, rand_x)
                            ip_ys.insert(i, data_y[rand_index])
                            break
                points_count -= 1    

    if(method=="lagrange"):
        result = lagrange(ip_xs, ip_ys, data_x)
    elif(method=="spline"):
        result = spline(ip_xs, ip_ys, data_x)
        diff = len(data_x)-len(result)
        if(diff>0):
            for i in range(diff):
                result.append(None)

    return result
    

def lagrange(ip_xs, ip_ys, result_xs):
    result_ys = []
    for k in range(len(result_xs)):
        result_y = 0
        for i in range(len(ip_xs)):
            result_y += ip_ys[i]*phi(i,ip_xs,result_xs[k])
        result_ys.append(result_y)
    return result_ys


def phi(i, xs, z):   #ok
    xi = xs[i]
    result = 1
    for j in range(len(xs)):
        if(j!=i):
            xj = xs[j]
            result *= z-xj
            result /= xi-xj
    return result


def spline(ip_xs, ip_ys, result_xs):
    result_ys = []
    i = 0
    while(i<len(ip_xs)-2):
        h = ip_xs[i+1]-ip_xs[i]
        M = [[1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [1, h, h**2, h**3, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, h, h**2, h**3],
        [0, 1, 2*h, 3*(h**2), 0, -1, 0, 0],
        [0, 0, 2, 6*h, 0, 0, -2, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 6*h]]
        x0 = ip_xs[i]
        x1 = ip_xs[i+1]
        x2 = ip_xs[i+2]
        fx0 = ip_ys[i]
        fx1 = ip_ys[i+1]
        fx2 = ip_ys[i+2]
        b = []
        b.append(fx0)
        b.append(fx1)
        b.append(fx1)
        b.append(fx2)
        b = b + [0,0,0,0]
        p = np.linalg.solve(M,b)
        for j in range(len(result_xs)):
            z = result_xs[j]
            if z<x0:
                pass
            else:
                if z<x1:
                    result_ys.append(p[0]+p[1]*(z-x0)+p[2]*((z-x0)**2)+p[3]*((z-x0)**3))
                elif i==len(ip_xs)-4:
                    i-=1
                    break
                elif z<x2:
                    result_ys.append(p[4]+p[5]*(z-x1)+p[6]*((z-x1)**2)+p[7]*((z-x1)**3))
                else:
                        break
        i+=2
    
    return result_ys

        

