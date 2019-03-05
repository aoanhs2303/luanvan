import DataStructure
import Config


def CombineAndSort(LOC1, LOC2, L):
    listChainID = sorted(list(set(LOC1.List_Of_ChainIDs + LOC2.List_Of_ChainIDs[L:L + 1])))
    LOE = list(set(LOC1.LOE) & set(LOC2.LOE))
    Support = len(LOE) / Config.TOTAL_VERTICES
    LIC = DataStructure.LargeItemChain(listChainID, LOE, Support)
    return LIC


def Support(LOC, ItemChain):
    LOE = set()
    for ChainId in LOC:
        for IC in ItemChain:
            if ChainId == IC.ChainId:
                for E in IC.Entities_Var:
                    LOE.add(E)
                break

    return len(LOE)

