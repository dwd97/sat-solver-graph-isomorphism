import subprocess
from argparse import ArgumentParser

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

    if NR_VERTICES_1 = NR_VERTICES_0:
        if NR_EDGES_1 = NR_EDGES_0:
            return True
    
    return False
    

def encode(instance):
    cnf = []

    for i in range(0, NR_VERTICES_0):
        for x in range(0, NR_VERTICES_1):
            

def v(i,j):
    return i*NR_VERTICES + j

def call_solver(cnf, nr_vars, output_name, solver_name, verbosity):
    # TODO: call specified solver

def print_result(result):
    # TODO: print in specified result

if __name__ == "__main__":
    parser = ArgumentParser()
    
    parser.add_argument(
       "-i",
       "--input",
       default="input1.in",
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
        default=1,
        type=int,
        choices=range(0,2),
        help=(
            "Verbosity from sat solver."
        ),
    )

    args=parser.parse_args()

    if(!load_instance(args.input)):
        print("Not a valid input! Number of vertices or number of edges are not correct.")
        return 1

    cnf, nr_vars = encode(instance)

    result = call_solver(cnf, nr_vars, args.output, args.solver, args.verb)

    print_result(result)
