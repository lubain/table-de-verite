class FormulaParser:
    @staticmethod
    def extract_subformulas(formula):
        subformulas = set()
        stack, current_subformula = [], ""
        for char in formula:
            if char == '(':
                if current_subformula: stack.append(current_subformula)
                current_subformula = char
            elif char == ')':
                current_subformula += char
                subformulas.add(current_subformula)
                if stack: current_subformula = stack.pop() + current_subformula
                else:
                    subformulas.add(current_subformula)
                    current_subformula = ""
            else:
                current_subformula += char
        if current_subformula: subformulas.add(current_subformula)
        return sorted(subformulas, key=len)

    @staticmethod
    def find_abr(hyp, a="", b="", r="", isA=True, isB=False):
        for h in hyp:
            if h not in ["v","^","-",">","<","="]:
                if isA: a += h
                if isB: b += h
            else:
                r += h
                isA = False
                isB = True
        return a, b, r