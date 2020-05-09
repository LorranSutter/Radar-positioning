from gurobipy import *
import time
import sys


def read_file_instance(arq):
    with open(file_name, 'r') as f:
        num_max_rad = int(f.readline())
        num_pos_rad = int(f.readline())
        num_demand = int(f.readline())
        num_id_quality = int(f.readline())
        a = [[] for k in range(num_id_quality)]
        for k in range(num_id_quality):
            line = f.readline().split()
            indexes = [int(line[0].split('_')[0][1:]),
                       int(line[0].split('_')[1])]
            a[k] = [indexes[0], indexes[1], float(line[1])]
    return num_max_rad, num_pos_rad, num_demand, num_id_quality, a


def solve(m, num_demand, num_pos_rad, num_max_rad, num_id_quality):
    id_current_constr = 1
    #m.params.TimeLimit = 1
    #m.params.Method = -1
    m.params.Heuristics = 0

    # ----- Create variables problem -----
    y = [m.addVar(vtype=GRB.BINARY, name="y"+str(i+1))
         for i in range(num_demand)]  # Demands
    x = [m.addVar(vtype=GRB.BINARY, name="x"+str(j+1))
         for j in range(num_pos_rad)]  # Radar positions
    z = [m.addVar(vtype=GRB.BINARY, name="z"+str(k[0])+"_"+str(k[1]))
         for k in a]  # Signal quality

    # ----- Update model with variables -----
    m.update()

    # ----- Objective function -----
    m.setObjective(sum([i for i in y]) + sum([a[k][2]*z[k]
                                              for k in range(num_id_quality)]), GRB.MAXIMIZE)

    # ----- Constraint - there must be a radar xj for the quality zij -----
    for k in range(num_id_quality):
        m.addConstr(x[a[k][1]-1] - z[k], GRB.GREATER_EQUAL,
                    0, "R"+str(id_current_constr))
        id_current_constr += 1

    # ----- Constraint - the sum of all qualities zij must be equals to the temand yi -----
    # ----- ensures that there will be a radar with the best signal serving each demand when it is possible -----
    for i in range(num_demand):
        m.addConstr(sum([z[k] for k in range(num_id_quality) if a[k]
                         [0] == i+1]) - y[i], GRB.EQUAL, 0, "R"+str(id_current_constr))
        id_current_constr += 1

    # ----- Constraint - total of radars xj must be equals to num_max_rad -----
    m.addConstr(sum([x[i] for i in range(num_pos_rad)]),
                GRB.EQUAL, num_max_rad, "R"+str(id_current_constr))
    id_current_constr += 1

    m.optimize()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Incorret params input")
        print("Right input:")
        print("                 Instances/instancia<numPoints>_<numDemands>_<numMaxRad>")
        sys.exit(0)

    file_name = sys.argv[1]

    num_max_rad, num_pos_rad, num_demand, num_id_quality, a = read_file_instance(
        file_name)

    # ----- Init model -----
    m = Model("Model")

    print("\n------------------ Optimization started ------------------\n")
    t = time.time()
    solve(m, num_demand, num_pos_rad, num_max_rad, num_id_quality)
    t = time.time() - t
    print("------------------- Optimization finished -------------------\n")

    print("\n------------------- Results -------------------")
    print("Execution time: " + str(t))
    print("Objective function value:" + str(m.objVal))
    print("Gap value: " + str(m.MIPGap))
    print("--------------------------------------------------\n")

    if m.Status == GRB.OPTIMAL:
        m.write("Solutions/" + file_name[11:] + "_out.sol")
        print("Written file Solutions/" + file_name[11:] + "_out.sol")
