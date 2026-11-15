import subprocess
from argparse import ArgumentParser

def load_instance(input_file_name):
    # TODO: read from input file, define format

def encode(instance):
    #TODO: return (cnf, nr_vars), encode using specified CNF

def call_solver(cnf, nr_vars, output_name, solver_name, verbosity):
    # TODO: call specified solver

def print_result(result):
    # TODO: print in specified result

if __name__ == "__main__":
    parser = ArgumentParser()
    
    parser.add_argument(
       "-i",
       "--input",
       default="input.in",
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

    instance = load_instance(args.input)

    cnf, nr_vars = encode(instance)

    result = call_solver(cnf, nr_vars, args.output, args.solver, args.verb)

    print_result(result)
