import DataStructure
import Config


def CombineAndSort(LOC1, LOC2, L):
    listChainID = sorted(list(set(LOC1.List_Of_ChainIDs + LOC2.List_Of_ChainIDs[L:L + 1])))
    LOE = list(set(LOC1.LOE) & set(LOC2.LOE))
    Support = len(LOE) / Config.TOTAL_VERTICES
    LIC = DataStructure.LargeItemChain(listChainID, LOE, Support)
    return LIC


def Support(LOC, List_LargeItemChain, ItemChains):
    if len(LOC) == 1:
        for IC in ItemChains:
            if LOC[0] == IC.ChainId:
                return len(IC.Entities_Var) / Config.TOTAL_VERTICES
    else:
        for IC in List_LargeItemChain:
            if LOC == IC.List_Of_ChainIDs:
                return len(IC.LOE) / Config.TOTAL_VERTICES
    return 0
