import Config
import DataStructure


def Generate2LargeItemChains(List_ItemChain):
    LLICs = []
    lengthOfArray = len(List_ItemChain)
    for i in range(lengthOfArray):
        for j in range(i + 1, lengthOfArray):
            LOE = Intersect(List_ItemChain[i].Entities_Var, List_ItemChain[j].Entities_Var)
            Support = len(LOE) / Config.TOTAL_VERTICES
            if Support >= Config.MIN_SUPPORT:
                LIC = DataStructure.LargeItemChain([List_ItemChain[i].ChainId, List_ItemChain[j].ChainId], LOE, Support)
                LLICs.append(LIC)

    return LLICs


def Intersect(LOE1, LOE2):
    return list(set(LOE1) & set(LOE2))
