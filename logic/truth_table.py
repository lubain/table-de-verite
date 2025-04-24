class TruthTable:
    def __init__(self, variables):
        self.variables = variables
        self.B, self.variable_positive = self._generate_table()

    def _generate_table(self):
        n, variable_positive = 0, []
        for i in range(len(self.variables)):
            if self.variables[i][0] != "!":
                variable_positive.append(self.variables[i])
                n += 1
        variable_negative = [self.variables[i] for i in range(len(self.variables)) if self.variables[i][0] == "!"]
        length = 2 ** n
        A, B = [], []
        
        for i in range(n):
            zero = length // (2 ** (i + 1))
            a, tmp, temp = [0], [], []
            for j in range(length):
                if (j == 0 or a[j] > a[j - 1] or a[j] == 0):
                    a.append(a[j] + 1)
                    if a[j] == zero:
                        a[j + 1] = a[j] - 1
                        tmp.append(1)
                        continue
                    tmp.append(0)
                else:
                    tmp.append(1)
                    a.append(a[j] - 1)
            B.append(tmp)
            if "!"+variable_positive[i] in variable_negative:
                for j in range(len(B[0])):
                    if B[i][j] == 0: temp.append(1)
                    else: temp.append(0)
                A.append(temp)
        B.extend(A)
        variable_positive.extend(variable_negative)
        return B, variable_positive