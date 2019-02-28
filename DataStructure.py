class Node:
    def __init__(self, id, asin, similar, review):
        self.id = id
        self.asin = asin
        self.similar = similar
        self.review = review


class Review:
    def __init__(self, rating, helpful):
        self.rating = rating
        self.helpful = helpful


class RelationAndEntities:
    def __init__(self, relation, listEntities):
        self.relation = {relation: listEntities}


class EntityInfo:
    def __init__(self, endPointEntity, listRelationsAndEntities):
        self.endPointEntity = endPointEntity
        self.listRelationsAndEntities = listRelationsAndEntities


class ItemChain:
    def __init__(self, ChainId, Entities_Var, Relations_Parameter, EndpointEntity, Support):
        self.ChainId = ChainId
        self.Entities_Var = Entities_Var
        self.Relations_Parameter = Relations_Parameter
        self.EndpointEntity = EndpointEntity
        self.Support = Support


class LargeItemChain:
    def __init__(self, List_Of_ChainIDs, Intersection_Count, Support):
        self.List_Of_ChainIDs = List_Of_ChainIDs
        self.Intersection_Count = Intersection_Count
        self.Support = Support


class Rule:
    def __init__(self, Antecedent, Consequent, Confidence, Support):
        self.Antecedent = Antecedent
        self.Consequent = Consequent
        self.Confidence = Confidence
        self.Support = Support