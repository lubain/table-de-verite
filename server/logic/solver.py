from .variable_extractor import VariableExtractor
from .truth_table import TruthTable
from .formula_parser import FormulaParser
from .logical_operations import LogicalOperations

class LogicSolver:
    def __init__(self, hypothese):
        self.hypothese = hypothese
        self.variables = VariableExtractor.extract(hypothese)
        self.truth_table = TruthTable(self.variables)
        self.parser = FormulaParser()
        
    def find_valeur_ab(self, a, b, sub_variable):
        va, vb = [], []
        if b == "":
            if len(sub_variable) > 0:
                if a[0] == "!":
                    a = a.replace("!", "")
                    for j in range(len(self.truth_table.B[0])):
                        if sub_variable[int(a)][j] == 0: va.append(1)
                        else: va.append(0)
                else: va = [sub_variable[int(a)][j] for j in range(len(self.truth_table.B[0]))]
                return va, vb
        for i, v in enumerate(self.truth_table.variable_positive):
            if v == a:
                va = [self.truth_table.B[i][j] for j in range(len(self.truth_table.B[i]))]
            if v == b and b != "":
                vb = [self.truth_table.B[i][j] for j in range(len(self.truth_table.B[i]))]
        return va, vb

    def solve(self):
        subformul = self.parser.extract_subformulas(self.hypothese)
        subformul[len(subformul)-1] = self.hypothese
        sub = subformul.copy()
        temp = [f"{i}" for i in range(len(subformul))]
        solution, sub_variable, i = [], [], 0

        while i < len(subformul):
            sub[i] = sub[i].replace("(", "").replace(")", "").replace(" ", "")
            a, b, r = self.parser.find_abr(sub[i])
            va, vb = self.find_valeur_ab(a, b, sub_variable)
            if a != "" and b != "": 
                solution = LogicalOperations.combiner(self.truth_table.B, va, vb, a, b, r, sub_variable)
            else: 
                solution = va
            sub_variable.append(solution)
            i += 1
            for j in range(i, len(subformul)):
                sub[j] = sub[j].replace("(", "").replace(")", "").replace(" ", "")
                if subformul[i-1] in subformul[j] and subformul[i-1] != subformul[j]:
                    sub[j] = sub[j].replace(sub[i-1], temp[i-1])

        self.truth_table.B.extend(sub_variable)
        self.truth_table.variable_positive.extend(subformul)
        return self.truth_table.B, self.truth_table.variable_positive