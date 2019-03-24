import DataStructure
import Config


def CombineAndSort(LOC1, LOC2, L):
    listChainID = sorted(list(set(LOC1.List_Of_ChainIDs + LOC2.List_Of_ChainIDs[L:L + 1])))
    LOE = list(set(LOC1.LOE) & set(LOC2.LOE))
    Support = len(LOE) / Config.TOTAL_VERTICES
    LIC = None
    if Support >= Config.MIN_SUPPORT:
        LIC = DataStructure.LargeItemChain(listChainID, LOE, Support)
    return LIC


def Support(LOC, ItemChain):
    LOE = set()
    for ChainId in LOC:
        for E in ItemChain[ChainId-1].Entities_Var:
            LOE.add(E)

    return len(LOE)/Config.TOTAL_VERTICES


def writeRule2File(Rules, ItemChain):
    file = open('Rule_75.txt', 'w', encoding='utf-8')
    for R in Rules:
        line = ""
        for A in R.Antecedent:
            for IC in ItemChain:
                if A == IC.ChainId:
                    listRelation = IC.Relations_Parameter.split('>')
                    for Re in reversed(listRelation):
                        line += "(" + Re
                    line += '(' + str(IC.EndpointEntity) + ')' * (len(listRelation) + 1)
        line += ' --> '
        for IC in ItemChain:
            if R.Consequent == IC.ChainId:
                listRelation = IC.Relations_Parameter.split('>')
                for Re in reversed(listRelation):
                    line += "(" + Re
                line += "(" + str(IC.EndpointEntity) + ')' * (len(listRelation) + 1)

        line += ", {C=" + str(R.Support) + "}\n"
        file.writelines(line)
    file.close()



