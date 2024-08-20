class key:
    def __init__(self):
        self.d={
            "LANGSMITH_API_KEY":"",
            "GROQ_API_KEY":"",
            }
    def get_key(self,str):
        try :
            return self.d[str]
        except:
            return ""