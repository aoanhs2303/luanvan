import Config
import DataStructure
import ExampleMRAR as MRAR


def GenerateItemChains(EndpointEntity, Relations_Parameter, Entities_Parameter, Level, LLICs, List_EntityInfo):
    Entities_Var = Entities_Parameter
    if Config.MIN_LEVEL <= Level <= Config.MAX_LEVEL:
        Support = len(Entities_Var) / Config.TOTAL_VERTICES

    if Support >= Config.MIN_SUPPORT:
        ItemChain = DataStructure.ItemChain(len(LLICs) + 1, Entities_Var, Relations_Parameter, EndpointEntity, Support)
        LLICs.append(ItemChain)

    if Level < Config.MAX_LEVEL:
        Relations_Var = UnionIncomingEdgesOf(Entities_Var, List_EntityInfo)
        for Relation in Relations_Var: #đoạn này còn loáng choáng
            r = list(Relation.keys())[0]
            e = Relation.get(r)
            GenerateItemChains(EndpointEntity, Relations_Parameter + " " + r, e, Level + 1, LLICs, List_EntityInfo)


def UnionIncomingEdgesOf(Entities_Var, List_EntityInfo):
    Relations_Var = []
    for EntityInfo in List_EntityInfo:
        for Entity in Entities_Var:
            if Entity == EntityInfo.endPointEntity and len(EntityInfo.listRelationsAndEntities) > 0:
                Relations_Var.append(EntityInfo.listRelationsAndEntities)
    Relations = set()
    Result = []
    for r in Relations_Var:
        Relations.add(list(r[0].relation.keys())[0])

    for r in Relations:
        Result.append({r: list()})

    for r1 in Result:
        for r2 in Relations_Var:
            for key in r2:
                try:
                    k = list(key.relation.keys())[0]
                    r1[k] = r1[k] + key.relation.get(k)
                except:
                    pass
            # k = list(r2[0].relation.keys())[0]
            # r1[list(r2[0].relation.keys())[0]] = r1[k] + r2[0].relation.get(k)

    return Result
