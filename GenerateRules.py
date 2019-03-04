import Config
import DataStructure
import Helper


def GenerateRule(AllCandidate):
    Rules = []

    for i in range(2, len(AllCandidate)):
        for Candidate in AllCandidate[i]:
            for ChainID in Candidate.List_Of_ChainIDs:
                Consequent = ChainID
                Antecedent = sorted(list(set(Candidate.List_Of_ChainIDs) ^ set([ChainID])))
                Confidence = Candidate.Support / Helper.Support(Antecedent, AllCandidate)
                if Confidence >= Config.MIN_CONFIDENCE:
                    Rule = DataStructure.Rule(Antecedent, Consequent, Confidence, Candidate.Support)
                    Rules.append(Rule)

    return Rules