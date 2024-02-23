#!/usr/bin/python
import requests, json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class SW_Repo_Helper():
    def __init__(self, config):
        self.url = config["TPC_SW_Repo_API"]["soureURI"]
        cert_file_path = config["TPC_SW_Repo_API"]["client_cert"]
        key_file_path = config["TPC_SW_Repo_API"]["client_key"]
        self.x509 = (cert_file_path, key_file_path)
    
    def get_packages(self, category, model):
        try:
            url = self.url + "packages?category=" + category + "&model=" + model        
            resp = requests.get(url=url, cert=self.x509, verify=False)
        except (Exception) as error:
            print("[ERROR] " + str(error))
            return False, error

        return True, resp.content.decode("utf-8") 
    
    def get_profile(self):
        url = self.url + "profile"
        try:
            resp = requests.get(url=url, cert=self.x509, verify =False)
        except (Exception) as error:
            print("[ERROR] " + str(error))
            return False, error

        return True, resp.content.decode("utf-8") 
    
    def isNewVersion(self, asis_version, tobe_version):
        a_version = asis_version.split('.')
        b_version = tobe_version.split('.')
        pos = 0
        for a in a_version:
            if pos > (len(b_version)-1):
                return False
            b = int(b_version[pos])
            if b > int(a) :
                return True
            elif b < int(a):
                return False
                
            pos = pos + 1
        
        if pos == len(b_version):
            return False
        else:
            return True
    
    def isFitMinVersion(self, asis_version, minVersion):
        status = self.isNewVersion(asis_version, minVersion)
        if status:
            return False
        else:
            return True
    
    def normalizeVersion(self, in_version):
        out_version = in_version
        if out_version.lower().startswith('v'):
            out_version = out_version[1:]
        
        return out_version
    
    def scan_tpe_package(self, current_fw_version, current_tpe_version, model):
        matchedPackage = {}
        status, tpe_response = self.get_packages("tpe", model)
        normal_fw_version = self.normalizeVersion(current_fw_version)
        if (status):
            tpe_response_content = json.loads(tpe_response)
            tpe_data = tpe_response_content["data"]
            asis_tpe_version = current_tpe_version.replace("-", ".")
            for tpe in tpe_data:            
                # is this a new version?  
                tobe_tpe_version = tpe["version"] + "." + tpe["buildNumber"]
                if self.isNewVersion(asis_tpe_version, tobe_tpe_version):
                    # does dependency ok?
                    if self.isFitMinVersion(normal_fw_version, tpe["dependency"]["minFirmwareVersion"]):                    
                        matchedPackage["category"] = "tpe"
                        matchedPackage["packageName"] = tpe["packageName"]
                        matchedPackage["version"] = tpe["version"] + "-" + tpe["buildNumber"]
                        matchedPackage["displayName"] = tpe["displayName"]
                        matchedPackage["size"] = tpe["size"]
                        matchedPackage["yamlUrl"] = tpe["yamlUrl"]
                        print("[INFO] Safe to Upgrade")
                        return matchedPackage
                    else:
                        print("[INFO] FW version not fit, No Go")
                    
        return None
    
    def scan_mil_package(self, current_fw_version, model):
        matchedPackage = {}
        status, mil_response = self.get_packages("mil", model)
        normal_fw_version = self.normalizeVersion(current_fw_version)
        if (status):
            mil_response_content = json.loads(mil_response)
            mil_data = mil_response_content["data"]
            for mil in mil_data:            
                # is this a new version?
                if self.isNewVersion(normal_fw_version, mil["firmwareVersion"]):
                    # does dependency ok?
                    if self.isFitMinVersion(normal_fw_version, mil["dependency"]["minFirmwareVersion"]):
                        matchedPackage["category"] = "mil"
                        matchedPackage["packageName"] = mil["packageName"]
                        matchedPackage["version"] = mil["firmwareVersion"]
                        matchedPackage["displayName"] = mil["displayName"]
                        matchedPackage["size"] = mil["size"]
                        matchedPackage["yamlUrl"] = mil["yamlUrl"]
                        print("[INFO] Safe to Upgrade")
                        return matchedPackage
                    else:
                        print("[INFO] FW version not fit, No Go")
                    
        return None
