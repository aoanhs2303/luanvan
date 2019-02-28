import re
import Config
import DataStructure
import GenerateItemChains as GIC
import Generate2LargeItemChains as G2LIC
import GenerateRules as GR
import Helper

def gen_read_lines(file_name):
    with open(file_name) as fp:
        for line in fp:
            yield line.strip()


def is_para_starting(line):
    return True if re.match("^paragraph\d+:$", line) else False


def gen_read_para(file_name):
    gen = gen_read_lines(file_name)

    para = []
    for line in gen:
        if is_para_starting(line):
            if para:
                yield para
            para = []
        if ". " in line:
            para = []
            continue
        para.append(line)

    yield para


para_gen = gen_read_para("data.txt")
allNode = []
for para in para_gen:
    __id = 0
    __asin = 0
    __similars = []
    __reviews = []
    for line in para:
        data = line.strip()
        if data != "":
            try:
                data = data.split(":")
                key = data[0].strip()
                value = data[1].strip()
                if key == "Id":
                    __id = value
                elif key == "ASIN":
                    __asin = value
                elif key == "similar":
                    __similars = value.split("  ")[1:]
                elif key.split("  ")[1].strip() == "cutomer":
                    rating = data[2].split("  ")[0].strip()
                    helpful = data[4].strip()
                    review = DataStructure.Review(rating, helpful)
                    __reviews.append(review)
            except:
                pass
        else:
            if id != 0:
                node = DataStructure.Node(__id, __asin, __similars, __reviews)
                allNode.append(node)

Config.setNumberOfVertices(allNode)

List_EntityInfo = []
for node in allNode:
    EntityInfo1 = DataStructure.EntityInfo(node.asin, [DataStructure.RelationAndEntities("Similar", node.similar), DataStructure.RelationAndEntities("Has Review", node.review)])
    numRatingLessThan3Star = 0
    numRating3Star = 0
    numRating4Or5Star = 0
    for r in node.review:
        if int(r.rating) < 3:
            numRatingLessThan3Star += 1 + round(int(r.helpful)/2)
        elif int(r.rating) == 3:
            numRating3Star += 1 + round(int(r.helpful)/2)
        else:
            numRating4Or5Star += 1 + round(int(r.helpful)/2)
    EntityInfo2 = DataStructure.EntityInfo("Rating less than 3 star", [DataStructure.RelationAndEntities("Rating", numRatingLessThan3Star)])
    EntityInfo3 = DataStructure.EntityInfo("Rating 3 star", [DataStructure.RelationAndEntities("Rating", numRating3Star)])
    EntityInfo4 = DataStructure.EntityInfo("Rating 4, 5 star", [DataStructure.RelationAndEntities("Rating", numRating4Or5Star)])
    List_EntityInfo.append(EntityInfo1)
    List_EntityInfo.append(EntityInfo2)
    List_EntityInfo.append(EntityInfo3)
    List_EntityInfo.append(EntityInfo4)


LLICs = []
AllLICs = []
for EntityInfo in List_EntityInfo:
    for Relation in EntityInfo.listRelationsAndEntities:
        GIC.GenerateItemChains(EntityInfo.endPointEntity, Relation, EntityInfo.endPointEntity, 1)

AllLICs = LLICs = G2LIC.Generate2LargeItemChains(LLICs)

L = 1
while True: #until len(Candidates) == 0
    L = L + 1
    Candidates = []
    for LIC1 in LLICs:
        for LIC2 in LLICs:
            if LIC1 != LIC2:
                Candidates.append(Helper.CombineAndSort(LIC1.List_Of_ChainIDs, LIC2.List_Of_ChainIDs))

    LLICs = []
    for CIS in Candidates:
        if len(CIS)/Config.TOTAL_VERTICES >= Config.MIN_SUPPORT: #all subset of CIS are Large
            LLICs = LLICs + CIS

    AllLICs = AllLICs + LLICs

Rules = GR.GenerateRule(AllLICs)


