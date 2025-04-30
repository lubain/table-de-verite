class VariableExtractor:
    @staticmethod
    def extract(hypothese):
        e = [x for x in hypothese.replace("(", "").replace(")", "").replace("|", " ").replace("&", " ").replace("<=>", " ").replace("=>", " ").split()]
        for i in range(len(e)):
            pivot = e[i]
            for j in range(i + 1, len(e)):
                if e[j] == pivot: e[j] = ""
        variables = [element for element in e if element != ""]

        for i, t in enumerate(variables):
            if t[0] == "!":
                pivot, isZero = t, True
                for j in range(len(variables)):
                    if j != i:
                        if pivot == "!"+variables[j]:
                            isZero = False
                            break
                        else: isZero = True
                if isZero: variables.insert(i, variables[i].replace("!", ""))
        variables.sort()
        return variables