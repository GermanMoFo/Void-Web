from void_scribe import NameGenerator
from Void_Logger import Void_Log_Info


def __ProcessNameRequest__(Data):
    #Generate Names
    name_type, amount = Data["Req_Arguments"]["Name_Type"], Data["Req_Arguments"]["Amount"]
    gen_names = NameGenerator.generateMarkovNames(name_type, amount)
    Void_Log_Info(f"Generated {amount} {name_type} Names For Request")
    return gen_names

def __ProcessSentenceRequest__(Data):
    return None
    #Generate Sentences
    sentence_type, amount = Data["Req_Arguments"]["Sentence_Type"], Data["Req_Arguments"]["Amount"]
    gen_names = StoryGenerator.generateSentence(Sentence_Type=sentence_type, amount=amount)
    #Void_Log_Info(f"Generated {amount} {sentence_type} Sentences For Request")
    return gen_names

_AlgorithmRequestMap_ = {"Name":__ProcessNameRequest__, "Sentence":__ProcessSentenceRequest__}


def RunAlgorithmRequest(Data):
    return _AlgorithmRequestMap_[Data["Req_Type"]](Data)