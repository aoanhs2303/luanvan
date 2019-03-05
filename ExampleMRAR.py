import Config
import DataStructure as DS
import GenerateItemChains as GIC
import Generate2LargeItemChains as G2LIC
import GenerateRules as GR
import Helper
import datetime


# Config.setNumberOfVTOTAL_VERTICESertices(range(19))

def MRAR():
    # EI01 = DS.EntityInfo("Humid", [{"Climate Type": ["Tehran", "Shiraz"]}])
    # EI02 = DS.EntityInfo("Tehran", [{"Nearby": ["Yazd"]}])
    # EI03 = DS.EntityInfo("Shiraz", [{"Nearby": ["Kerman"]}, {"Live in": ["Mr A"]}])
    # EI04 = DS.EntityInfo("Yazd", [{"Live in": ["Hasan"]}])
    # EI05 = DS.EntityInfo("Kerman", [{"Live in": ["Reza", "Saraee"]}])
    # EI06 = DS.EntityInfo("Hasan", [])
    # EI07 = DS.EntityInfo("Reza", [])
    # EI08 = DS.EntityInfo("Good", [{"Health Condition": ["Hasan", "Reza"]}])
    # EI09 = DS.EntityInfo("Project A", [{"Work On": ["Mr A"]}])
    # EI10 = DS.EntityInfo("Mr A", [{"Cooperator": ["Saraee"]}])
    # EI11 = DS.EntityInfo("Saraee", [{"Supervised By": ["Reza", "Ali"]}])
    # EI12 = DS.EntityInfo("Ali", [])
    # EI13 = DS.EntityInfo("IUT", [{"Study in": ["Reza", "Ali", "Ahmad"]}, {"Patronage": ["Project B"]}])
    # EI14 = DS.EntityInfo("Project B", [{"Work On": ["Mr B"]}])
    # EI15 = DS.EntityInfo("Nematbakhsh", [{"Supervised By": ["Ahmad"]}])
    # EI16 = DS.EntityInfo("Ahmad", [])
    # EI17 = DS.EntityInfo("Isfahan", [{"Live in": ["Ali", "Ahmad", "Nematbakhsh"]}])
    # EI18 = DS.EntityInfo("MIT", [{"Patronage": ["Project A", "Project B"]}])
    # EI19 = DS.EntityInfo("Mr B", [{"Cooperator": ["Nematbakhsh"]}])

    EI01 = DS.EntityInfo("Humid", [{"Climate Type": ["Tehran", "Shiraz"]}])
    EI02 = DS.EntityInfo("Tehran", [{"Nearby": ["Yazd"]}])
    EI03 = DS.EntityInfo("Shiraz", [{"Nearby": ["Kerman"]}])
    EI04 = DS.EntityInfo("Yazd", [{"Live in": ["Hasan"]}])
    EI05 = DS.EntityInfo("Kerman", [{"Live in": ["Reza", "Saraee"]}])
    EI06 = DS.EntityInfo("Hasan", [{"Knows": ["Reza"]}])
    EI07 = DS.EntityInfo("Reza", [])
    EI08 = DS.EntityInfo("Good", [{"Health Condition": ["Hasan", "Reza"]}])
    EI09 = DS.EntityInfo("Project A", [{"Work On": ["Mr A"]}])
    EI10 = DS.EntityInfo("Mr A", [{"Cooperator": ["Saraee"]}, {"Knows": ["Nematbakhsh"]}])
    EI11 = DS.EntityInfo("Saraee", [{"Supervised By": ["Reza", "Ali"]}])
    EI12 = DS.EntityInfo("Ali", [])
    EI13 = DS.EntityInfo("IUT", [{"Study in": ["Reza", "Ali", "Ahmad"]}, {"Patronage": ["Project B"]}])
    EI14 = DS.EntityInfo("Project B", [{"Work On": ["Mr B"]}])
    EI15 = DS.EntityInfo("Nematbakhsh", [{"Knows": ["Mr B", "Saraee"]}, {"Supervised By": ["Ahmad"]}])
    EI16 = DS.EntityInfo("Ahmad", [{"Knows": ["Ali"]}])
    EI17 = DS.EntityInfo("Isfahan", [{"Live in": ["Ali", "Ahmad", "Nematbakhsh"]}])
    EI18 = DS.EntityInfo("MIT", [{"Patronage": ["Project A", "Project B"]}])
    EI19 = DS.EntityInfo("Mr B", [{"Cooperator": ["Nematbakhsh"]}])

    List_EntityInfo = [EI01, EI02, EI03, EI04, EI05, EI06, EI07, EI08, EI09, EI10, EI11, EI12, EI13, EI14, EI15, EI16, EI17, EI18, EI19]

    Map_EntityInfo = dict()
    for EntityInfo in List_EntityInfo:
        Map_EntityInfo[EntityInfo.endPointEntity] = EntityInfo.listRelationsAndEntities

    LLICs = []
    AllCandidate = []

    for EntityInfo in List_EntityInfo:
        for Relation in EntityInfo.listRelationsAndEntities:
            r = list(Relation.keys())[0]
            e = Relation.get(r)
            GIC.GenerateItemChains(EntityInfo.endPointEntity, r, e, 1, LLICs, Map_EntityInfo)

    ItemChains = LLICs.copy()
    AllCandidate.append(list())
    AllCandidate.append(ItemChains)

    LLICs = G2LIC.Generate2LargeItemChains(LLICs)
    AllCandidate.append(LLICs.copy())

    L = 0
    while L < len(LLICs):  # until len(Candidates) == 0
        L = L + 1
        Candidates = list()
        lengthOfArray = len(LLICs)
        for i in range(lengthOfArray):
            for j in range(i + 1, lengthOfArray - 1):
                if LLICs[i].List_Of_ChainIDs[:L] == LLICs[j].List_Of_ChainIDs[:L]:
                    Candidates.append(Helper.CombineAndSort(LLICs[i], LLICs[j], L))
        LLICs = list()
        for CIS in Candidates:
            if len(CIS.LOE) / Config.TOTAL_VERTICES >= Config.MIN_SUPPORT:  # all subset of CIS are Large
                LLICs.append(CIS)

        AllCandidate.append(LLICs)
    currentDT = datetime.datetime.now()
    print("candidate: " + str(currentDT))
    Rules = GR.GenerateRule(AllCandidate)
    return Rules


if __name__ == '__main__':
    currentDT = datetime.datetime.now()
    print("start: " + str(currentDT))
    MRAR()
    currentDT = datetime.datetime.now()
    print("end: " + str(currentDT))
    print('done')
