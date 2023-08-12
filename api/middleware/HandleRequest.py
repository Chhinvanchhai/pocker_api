
from flask import jsonify
from api.shared.Utils import Utils
class HandleRequest(Utils): 

    # def __init__(self, utils:Utils):
    #     self.utils = utils

    def onRequest(self, req):
        try: 
        
            if req.method == "POST":
                self.logs("request: "+ str(req.json))
        except Exception as e: {
            self.logs("errors:"+str(e))
        }
       

    def onResponse(self, res):
        try: 
            self.logs("response:"+ str(res.data))
        except Exception as e: {
            self.logs("errors: "+str(e))
        }