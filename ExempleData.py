import DataStructure as DS


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

List_EntityInfo = [EI01, EI02, EI03, EI04, EI05, EI06, EI07, EI08, EI09, EI10, EI12, EI13, EI14, EI15, EI16, EI17, EI18]