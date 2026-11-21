import subprocess
from argparse import ArgumentParser
import sys

def load_instance(input_file_name):
    
    global NR_VERTICES_0, NR_EDGES_0, NR_VERTICES_1, NR_EDGES_1, EDGES_0, EDGES_1 # graf 0 and graf 1
    with open(input_file_name, "r") as f:
        lines = f.readlines()
        zeroth_graph = lines[0].split()
        NR_VERTICES_0 = int(zeroth_graph[0])
        NR_EDGES_0 = int(zeroth_graph[1])
        EDGES_0 = []
        for i in range(1, NR_EDGES_0 + 1):
            line = lines[i].split()
            EDGES_0.append((int(line[0]), int(line[1])))

        first_graph = lines[NR_EDGES_0 + 1].split()
        NR_VERTICES_1 = int(first_graph[0])
        NR_EDGES_1 = int(first_graph[1])
        EDGES_1 = []
        for i in range(NR_EDGES_0 + 2, NR_EDGES_0 + NR_EDGES_1 + 2):
            line = lines[i].split()
            EDGES_1.append((int(line[0]), int(line[1])))

    if NR_VERTICES_1 == NR_VERTICES_0:
        if NR_EDGES_1 == NR_EDGES_0:
            return True
    
    return False
    

def encode(instance):
    cnf = []
    nr_vars = NR_VERTICES_0 * NR_VERTICES_1

    # at least one projection
    for i in range(0, NR_VERTICES_0):
        clause = []
        for j in range(0, NR_VERTICES_1):
            clause.append(v(i,j))
        clause.append(0)
        cnf.append(clause)
    
    # at most one projection from graph 0
    for i in range(0, NR_VERTICES_0):
        for j in range(0, NR_VERTICES_1):
            for k in range(j+1, NR_VERTICES_1):
                cnf.append([-v(i,j), -v(i,k), 0])

    # at most one projection at graph 1
    for i in range(0, NR_VERTICES_1):
        for j in range(0, NR_VERTICES_0):
            for k in range(j+1, NR_VERTICES_1):
                cnf.append([-v(j,i), -v(k,i), 0])

    # disallow all projections where one of them has the edge and the second one does not
    for a in range(0, NR_VERTICES_0):
        for b in range(0, NR_VERTICES_1):
            for c in range(0, NR_VERTICES_0):
                for d in range(0, NR_VERTICES_1):
                    if(is_edge(a,c,EDGES_0) != is_edge(b,d,EDGES_1)):
                        cnf.append([-v(a,b), -v(c,d), 0])

    return (cnf, nr_vars)
                
def is_edge(i,j,EDGES):
    if((i,j) in EDGES or (j,i) in EDGES):
        return True
    return False

def v(i,j):
    return i*NR_VERTICES_0 + j + 1

def v_reverse(n):
    n -= 1
    i = n // NR_VERTICES_0
    j = n % NR_VERTICES_0
    return (i,j)

def generate_file(cnf, nr_vars, output_name):
    with open(output_name, "w") as f:
        f.write("p cnf " + str(nr_vars) + " " + str(len(cnf)) + '\n')
        for clause in cnf:
            f.write(' '.join(str(lit) for lit in clause) + '\n')

def call_solver(output_name, solver_name, verbosity):
    return subprocess.run(['./' + solver_name, '-model', '-verb=' + str(verbosity), output_name], stdout=subprocess.PIPE)

def print_result(result):
    for line in result.stdout.decode('utf-8').split('\n'):
        print(line)

    if(result.returncode == 20):
        print("Unsatisfiable")
        return
    
    model = []
    for line in result.stdout.decode('utf-8').split('\n'):
        if line.startswith("v"):
            vars = line.split(" ")
            vars.remove("v")
            model.extend(int(v) for v in vars)
    model.remove(0)
    
    print("Izomorfní přejmenování vrcholů")
    for var in model:
        if(var > 0):
            (i,j) = v_reverse(var)
            print(f"{i}->{j}")

if __name__ == "__main__":
    parser = ArgumentParser()
    
    parser.add_argument(
       "-i",
       "--input",
       default="sample_inputs/input0.in",
       type=str,
       help=(
            "The instance file."
       ),
    )

    parser.add_argument(
        "-o",
        "--output",
        default="formula.cnf",
        type=str,
        help=(
            "Output file of the CNF formula."
        ),
    )

    parser.add_argument(
        "-s",
        "--solver",
        default="glucose-syrup",
        type=str,
        help= (
            "Used sat solver."
        )
    )
    parser.add_argument(
        "-v",
        "--verb",
        default=0,
        type=int,
        choices=range(0,2),
        help=(
            "Verbosity from sat solver."
        ),
    )

    args=parser.parse_args()
    
    instance = load_instance(args.input)
    if(instance is False):
        print("Not a valid input!")
        sys.exit(1)

    cnf, nr_vars = encode(instance)
    
    generate_file(cnf, nr_vars, args.output)

    result = call_solver(args.output, args.solver, args.verb)
    
    print_result(result)
