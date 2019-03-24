import Config
import DataStructure


def GenerateItemChains(EndpointEntity, Relations_Parameter, Entities_Parameter, Level, LLICs, Map_EntityInfo):
    Entities_Var = Entities_Parameter
    if Config.MIN_LEVEL <= Level <= Config.MAX_LEVEL:
        Support = len(Entities_Var) / Config.TOTAL_VERTICES

    if Support >= Config.MIN_SUPPORT:
        ItemChain = DataStructure.ItemChain(len(LLICs) + 1, Entities_Var, Relations_Parameter, EndpointEntity, Support)
        LLICs.append(ItemChain)

    if Level < Config.MAX_LEVEL:
        Relations_Var = UnionIncomingEdgesOf(Entities_Var, Map_EntityInfo)
        for Relation in Relations_Var:
            r = list(Relation.keys())[0]
            e = Relation.get(r)
            GenerateItemChains(EndpointEntity, Relations_Parameter + ">" + r, e, Level + 1, LLICs, Map_EntityInfo)


def UnionIncomingEdgesOf(Entities_Var, Map_EntityInfo):
    Relations_Var = []
    Relations = set()
    Result = []
    for Entity in Entities_Var:
        ListRandE = Map_EntityInfo.get(Entity)
        try:
            lenOfLE = len(ListRandE)
        except:
            lenOfLE = 0

        if lenOfLE > 0:
            Relations_Var.append(ListRandE)
            Relations.add(list(ListRandE[0].keys())[0])

    for r in Relations:
        Result.append({r: list()})

    for r1 in Result:
        for r2 in Relations_Var:
            for key in r2:
                try:
                    k = list(key.keys())[0]
                    r1[k] = r1[k] + key.get(k)
                except:
                    pass

    return Result
