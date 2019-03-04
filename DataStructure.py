class Node:
    def __init__(self, id, asin, similar, review):
        self.id = id
        self.asin = asin
        self.similar = similar
        self.review = review


class EntityInfo:
    def __init__(self, endPointEntity, listRelationsAndEntities):
        self.endPointEntity = endPointEntity
        self.listRelationsAndEntities = listRelationsAndEntities


class ItemChain:
    def __init__(self, ChainId, Entities_Var, Relations_Parameter, EndpointEntity, Support):
        self.ChainId = ChainId
        self.Entities_Var = set(Entities_Var)
        self.Relations_Parameter = Relations_Parameter
        self.EndpointEntity = EndpointEntity
        self.Support = Support


class LargeItemChain:
    def __init__(self, List_Of_ChainIDs, LOE, Support):
        self.List_Of_ChainIDs = List_Of_ChainIDs
        self.LOE = LOE
        self.Support = Support


class Rule:
    def __init__(self, Antecedent, Consequent, Confidence, Support):
        self.Antecedent = Antecedent
        self.Consequent = Consequent
        self.Confidence = Confidence
        self.Support = Support
