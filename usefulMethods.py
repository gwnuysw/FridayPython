import json
class responseHandler:
	def __init__(self):
		self.response = {
    			"version": "2.0",
    			"template":{
          			"outputs":[{
         			}]
    			}
		}
	def setSimpleText(self,text):
		self.response["template"]["outputs"][0]["simpleText"] = {
			"text":text
		}
	def setSimpleImg(self,url,altText="이미지없음"):
		self.response["template"]["outputs"][0]["simpleImage"] = {
			"imageUrl":url,
			"altText":altText
		}
	def setbasicCard(self, description):
		self.response["template"]["outputs"][0]["basicCard"] = {
			"description": description,
			"buttons":[]
		}
	def addButton(self,label,blockId):
		self.response["template"]["outputs"][0]["basicCard"]["buttons"].append({
			"label":label,
			"action":"block",
			"blockId":blockId
		})
	def getResponse(self):
		return self.response

def getSysNumber(requestData):
	payload = json.loads(requestData)
	sys_number = json.loads(payload["action"]["params"]["sys_number"])
	return sys_number["amount"]
def get자료형(requestData):
	payload = json.loads(requestData)
	numberType = payload["action"]["params"]["numberType"]
	return numberType
def getUtterance(requestData):
	payload = json.loads(requestData)
	utterance = payload["userRequest"]["utterance"]
	return utterance
