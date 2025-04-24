from logic.solver import LogicSolver

def display_truth_table(B, variables):
    for i in range(len(B[0])):
        print(" | ".join(str(B[j][i]) for j in range(len(variables))))

def main():
    hypothese = "p <=> (!q v (p -> !r))"
    solver = LogicSolver(hypothese)
    B, variables = solver.solve()
    
    print("Variables:", variables)
    print("\nTable de vérité:")
    display_truth_table(B, variables)

if __name__ == "__main__":
    main()