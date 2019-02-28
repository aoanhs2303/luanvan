import Config
import DataStructure


def GenerateRule(List_LargeItemChains):
    Rules = []
    for LIC in List_LargeItemChains:
        for ChainID in LIC.List_Of_ChainIDs:
            Consequent = ChainID
            Antecedent = LIC.List_Of_ChainIDs.remove(Consequent)
            Confidence = LIC.Support / (len(Antecedent) / Config.TOTAL_VERTICES)
            if Confidence >= Config.MIN_CONFIDENCE:
                Rule = DataStructure.Rule(Antecedent, Consequent, Confidence, LIC.Support)
                Rules.append(Rule)

    return Rules