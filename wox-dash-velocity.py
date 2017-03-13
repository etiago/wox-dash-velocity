#encoding=utf8
import os
import re
from urllib.parse import quote
from wox import Wox,WoxAPI

#Your class must inherit from Wox base class https://github.com/qianlifeng/Wox/blob/master/PythonHome/wox.py
#The wox class here did some works to simplify the communication between Wox and python plugin.
class Main(Wox):

    def start_velocity_without_keys(self, query):
        os.startfile("dash-plugin://query={}".format(quote(query)))

    def start_velocity_with_keys(self, query, keys):
        os.startfile("dash-plugin://keys={}&query={}".format(keys,quote(query)))
        
    # A function named query is necessary, we will automatically invoke this function when user query this plugin
    def query(self,query):
        #dash_keywords = key.
        keywords = re.findall(r'(.*): ', query)

        result = {"Title": "Velocity",
                  "IcoPath":"Images/Velocity.png"}
        
        if (len(keywords) > 0):
            clean_query = query.replace(keywords[0]+": ","")
            result["SubTitle"] = "Get Velocity ({}) docs for {}".format(keywords[0],clean_query)
            result["JsonRPCAction"] = {"method": "start_velocity_with_keys",
                                       "parameters": [clean_query, keywords[0]],
                                       "dontHideAfterAction": False}
        else:
            result["SubTitle"] = "Get Velocity docs for {}".format(query)
            result["JsonRPCAction"] = {"method": "start_velocity_without_keys",
                                       "parameters": [query],
                                       "dontHideAfterAction": False}
        return [result]
        
#Following statement is necessary
if __name__ == "__main__":
    Main()
