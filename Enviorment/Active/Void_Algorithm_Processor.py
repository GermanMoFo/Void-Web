from void_scribe import NameGenerator, StoryGenerator



def __ProcessNameRequest__(Data):

    #Generate Names
    gen_names = NameGenerator.MarkovName(Name_Type=Data["Req_Arguments"]["Name_Type"], amount=Data["Req_Arguments"]["Amount"])

    return gen_names

def __ProcessSentenceRequest__(Data):
    #Generate Sentences
    gen_names = StoryGenerator.generateSentence(Sentence_Type=Data["Req_Arguments"]["Sentence_Type"], amount=Data["Req_Arguments"]["Amount"])

    return gen_names

_AlgorithmRequestMap_ = {"Name":__ProcessNameRequest__, "Sentence":__ProcessSentenceRequest__}

def RunAlgorithmRequest(Data):
    return _AlgorithmRequestMap_[Data["Req_Type"]](Data)