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
            r = list(Relation.relation.keys())[0]
            e = Relation.relation.get(r)
            GenerateItemChains(EndpointEntity, Relations_Parameter + " " + r, e, Level + 1, LLICs, List_EntityInfo)


def UnionIncomingEdgesOf(Entities_Var, List_EntityInfo):
    Relations_Var = []
    for EntityInfo in List_EntityInfo:
        for Entity in Entities_Var:
            if Entity == EntityInfo.endPointEntity:
                Relations_Var.append(EntityInfo.listRelationsAndEntities)

    for r1 in Relations_Var:
        for r2 in Relations_Var:
            if r1 != r2 and list(r1[0].relation.keys())[0] == list(r2[0].relation.keys())[0]:
                k = list(r1[0].relation.keys())[0]
                Relations_Var.remove(r1)
                Relations_Var.remove(r2)
                Relations_Var.append({k: r1[0].relation.get(k) + r2[0].relation.get(k)})
    return Relations_Var
    # return Relations_Var[0] if len(Relations_Var) > 0 else []
