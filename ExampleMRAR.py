import Config
import DataStructure as DS
import GenerateItemChains as GIC
import Generate2LargeItemChains as G2LIC
import GenerateRules as GR
import Helper


# Config.setNumberOfVTOTAL_VERTICESertices(range(19))

def MRAR():
    EI01 = DS.EntityInfo("Humid", [DS.RelationAndEntities("Climate Type", ["Tehran", "Shiraz"])])
    EI02 = DS.EntityInfo("Tehran", [DS.RelationAndEntities("Nearby", ["Yazd"])])
    EI03 = DS.EntityInfo("Shiraz", [DS.RelationAndEntities("Nearby", ["Kerman"])])
    EI04 = DS.EntityInfo("Yazd", [DS.RelationAndEntities("Live in", ["Hasan"])])
    EI05 = DS.EntityInfo("Kerman", [DS.RelationAndEntities("Live in", ["Reza"]),
                                    DS.RelationAndEntities("Live in", ["Saraee"])])
    EI06 = DS.EntityInfo("Hasan", [DS.RelationAndEntities("Knows", ["Reza"])])
    EI07 = DS.EntityInfo("Reza", [])
    EI08 = DS.EntityInfo("Good", [DS.RelationAndEntities("Health Condition", ["Hasan", "Reza"])])
    EI09 = DS.EntityInfo("Project A", [DS.RelationAndEntities("Work On", ["Mr A"])])
    EI10 = DS.EntityInfo("Mr A", [DS.RelationAndEntities("Cooperator", ["Saraee"]),
                                  DS.RelationAndEntities("Knows", ["Nematbakhsh"])])
    EI11 = DS.EntityInfo("Saraee", [DS.RelationAndEntities("Supervised By", ["Reza", "Ali"])])
    EI12 = DS.EntityInfo("Ali", [])
    EI13 = DS.EntityInfo("IUT", [DS.RelationAndEntities("Study in", ["Reza", "Ali", "Ahmad"]),
                                 DS.RelationAndEntities("Patronage", ["Project B"])])
    EI14 = DS.EntityInfo("Project B", [DS.RelationAndEntities("Work On", ["Mr B"])])
    EI15 = DS.EntityInfo("Nematbakhsh", [DS.RelationAndEntities("Knows", ["Mr B", "Saraee"]),
                                         DS.RelationAndEntities("Supervised By", ["Ahmad"])])
    EI16 = DS.EntityInfo("Ahmad", [DS.RelationAndEntities("Knows", ["Ali"])])
    EI17 = DS.EntityInfo("Isfahan", [DS.RelationAndEntities("Live in", ["Ali", "Ahmad", "Nematbakhsh"])])
    EI18 = DS.EntityInfo("MIT", [DS.RelationAndEntities("Patronage", ["Project A", "Project B"])])

    List_EntityInfo = [EI01, EI02, EI03, EI04, EI05, EI06, EI07, EI08, EI09, EI10, EI11, EI12, EI13, EI14, EI15, EI16, EI17, EI18]

    global LLICs
    LLICs = []
    AllLICs = []
    for EntityInfo in List_EntityInfo:
        for Relation in EntityInfo.listRelationsAndEntities:
            r = list(Relation.relation.keys())[0]
            e = Relation.relation.get(r)
            GIC.GenerateItemChains(EntityInfo.endPointEntity, r, e, 1, LLICs, List_EntityInfo)

    AllLICs = LLICs = G2LIC.Generate2LargeItemChains(LLICs)

    L = 1
    while L < len(LLICs):  # until len(Candidates) == 0
        L = L + 1
        Candidates = []
        for LIC1 in LLICs:
            for LIC2 in LLICs:
                if LIC1 != LIC2 and LIC1.List_Of_ChainIDs[:L - 1] == LIC2.List_Of_ChainIDs[:L - 1]:
                    Candidates.append(Helper.CombineAndSort(LIC1.List_Of_ChainIDs[:L], LIC2.List_Of_ChainIDs[L-1:L]))

        LLICs = []
        for CIS in Candidates:
            if len(CIS) / Config.TOTAL_VERTICES >= Config.MIN_SUPPORT:  # all subset of CIS are Large
                LLICs = LLICs + CIS

        AllLICs = AllLICs + LLICs

    Rules = GR.GenerateRule(AllLICs)
    return Rules


if __name__ == '__main__':
    MRAR()
