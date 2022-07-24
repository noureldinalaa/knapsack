from pulp import *

def knapsack_Milp(c,weight,val):


    # creating an instance for the variable
    problem = LpProblem('knapsack',LpMaximize)
    # Crating a decision variable
    x = LpVariable.dicts('x',range(len(val)),lowBound=0,upBound=1,cat=LpInteger)
    #objective
    problem += pulp.lpSum(val[i] *x[i] for i in range(len(val)) ), "obj"

    # constraint
    problem += pulp.lpSum(weight[i] * x[i] for i in range(len(weight)) ) <= c,"constraint"

    #solve the problem
    problem.solve()

    # The status of the solution is printed to the screen
    print("Status:", LpStatus[problem.status])

    for v in problem.variables():
        print(v.name, "=", v.varValue)

    # The optimised objective function value is printed to the screen
    print("object = ", value(problem.objective))





if __name__ == '__main__':

    #P_0 dataset
    c = 165
    weight = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]  # 10 weights
    val = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72] # 10 values
    knapsack_Milp(c,weight,val)
