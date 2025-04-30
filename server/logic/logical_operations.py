class LogicalOperations:
    @staticmethod
    def implique(a, b): 
        return 0 if a == 1 and b == 0 else 1

    @staticmethod
    def et_logique(a, b): 
        return a * b

    @staticmethod
    def ou_logique(a, b): 
        return 1 if a == 1 or b == 1 else 0

    @staticmethod
    def equivalence(a, b): 
        return 1 if a == b else 0

    @staticmethod
    def combiner(B, va, vb, a, b, r, pred):
        solution = []
        if len(va) == 0: va = pred[int(a)]
        if len(vb) == 0: vb = pred[int(b)]
        for i in range(len(B[0])):
            if r == "<=>": operation = LogicalOperations.equivalence(va[i], vb[i])
            if r == "|": operation = LogicalOperations.ou_logique(va[i], vb[i])
            if r == "&": operation = LogicalOperations.et_logique(va[i], vb[i])
            if r == "=>": operation = LogicalOperations.implique(va[i], vb[i])
            solution.append(operation)
        return solution