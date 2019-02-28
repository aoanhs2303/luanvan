import Config
import DataStructure


def Generate2LargeItemChains(List_ItemChain):
    LLICs = []
    for IC1 in List_ItemChain:
        for IC2 in List_ItemChain:
            if IC1 != IC2:
                LOE = Intersect(IC1.Entities_Var, IC2.Entities_Var)
                Support = len(LOE) / Config.TOTAL_VERTICES
                if Support >= Config.MIN_SUPPORT:
                    LIC = DataStructure.LargeItemChain([IC1.ChainId, IC2.ChainId], len(LOE), Support)
                    LLICs.append(LIC)
    return LLICs


def Intersect(LOE1, LOE2):
    return list(set(LOE1) & set(LOE2))
