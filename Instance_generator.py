# ---------------------------------------- #
# ---------- Instance generator ---------- #
# ---------------------------------------- #

from random import *
import sys


def distance(p1, p2): return (
    (p2[0]-p1[0])*(p2[0]-p1[0])+(p2[1]-p1[1])*(p2[1]-p1[1]))**0.5


num_argv = len(sys.argv)

if num_argv != 4 and num_argv != 5 and num_argv != 6:
    print("Incorrect params input")
    print("Right input:")
    print("               Number of demands")
    print("               Max number of radars (optional)")
    print("               Max reach radius of radar signal (optional) (float) [1-50]")
    print("               Number of points in x direction")
    print("               Number of points in y direction")
    sys.exit(0)

# ----- Params -----
num_demands = int(sys.argv[1])
if num_argv == 4:
    num_points_x = int(sys.argv[2])
    num_points_y = int(sys.argv[3])
    num_max_rad = num_demands//2
elif num_argv == 5:
    num_max_rad = int(sys.argv[2])
    num_points_x = int(sys.argv[3])
    num_points_y = int(sys.argv[4])
else:
    num_max_rad = int(sys.argv[2])
    radars_radius_max = float(sys.argv[3])
    num_points_x = int(sys.argv[4])
    num_points_y = int(sys.argv[5])
# ----------------------

num_points_total = num_points_x*num_points_y  # Same as num_pos_rad

min_x = 0
min_y = 0
max_x = 100
max_y = 100

step_x = (max_x-min_x)/(num_points_x-1)
step_y = (max_y-min_y)/(num_points_y-1)

if num_argv != 6:
    radars_radius_max = (step_x*step_x + step_y*step_y)**0.5

print("Points generation started")
points = [[(w*step_x, k*step_y) for k in range(num_points_y)]
          for w in range(num_points_x)]
print(str(num_points_total) + " " + "generated points \n")

print("Max num of radars: " + str(num_max_rad) + "\n")
print("Max reach radius of radar signal: " + str(radars_radius_max) + "\n")

print("Random demands generation started")
points_demands = [(random()*(max_x-min_x)+min_x, random()
                   * (max_x-min_x)+min_x) for k in range(num_demands)]
print(str(num_demands) + " " + "random demands generated\n")

print("Signal quality indexes started")
a = []  # Coefficients
for k in range(num_demands):
    cont = 1
    for w in range(num_points_x):
        for z in range(num_points_y):
            d = distance(points[w][z], points_demands[k])
            if d < radars_radius_max:
                a.append(["a" + str(k+1) + "_" + str(cont),
                          1 - d/radars_radius_max])
            cont += 1
num_id_quality = len(a)
print(str(num_id_quality) + " " + "signal quality indexes generated \n")

print("Visualization file writing started")
with open("InstancesPoints/instance_Points"+str(num_points_total)+"_"+str(num_demands) + "_" + str(num_max_rad), 'w') as f:
    f.write(str(radars_radius_max))
    f.write("\n")
    f.write(str(num_points_total))
    f.write("\n")

    for k in points:
        for w in k:
            f.write(str(w[0]) + " " + str(w[1]) + "\n")

    f.write(str(num_demands))
    f.write("\n")

    for k in points_demands:
        f.write(str(k[0]) + " " + str(k[1]) + "\n")
print("Visualization file writing finished " + "instance_Points" +
      str(num_points_total)+"_"+str(num_demands) + "_" + str(num_max_rad) + "\n")

print("Instance file writing started")
with open("Instances/instance"+str(num_points_total)+"_"+str(num_demands) + "_" + str(num_max_rad), 'w') as f:
    f.write(str(num_max_rad))
    f.write("\n")
    f.write(str(num_points_total))
    f.write("\n")

    f.write(str(num_demands))
    f.write("\n")

    f.write(str(num_id_quality))
    f.write("\n")
    for k in a:
        f.write(k[0] + " " + str(k[1]) + "\n")

print("Instance file writing finished" + str(num_points_total) +
      "_" + str(num_demands) + "_" + str(num_max_rad) + "\n")
