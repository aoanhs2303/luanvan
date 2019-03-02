import Config
import DataStructure
import Helper


def GenerateRule(List_LargeItemChains, ItemChains):
    Rules = []
    for LIC in List_LargeItemChains:
        for ChainID in LIC.List_Of_ChainIDs:
            Consequent = ChainID
            Antecedent = sorted(list(set(LIC.List_Of_ChainIDs) ^ set([ChainID])))
            Confidence = LIC.Support / Helper.Support(Antecedent, List_LargeItemChains, ItemChains)
            if Confidence >= Config.MIN_CONFIDENCE:
                Rule = DataStructure.Rule(Antecedent, Consequent, Confidence, LIC.Support)
                Rules.append(Rule)

    return Rules