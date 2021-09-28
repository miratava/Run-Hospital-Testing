import re
import requests
import xml.etree.ElementTree as ET
import declxml

class Agent:

    def __init__(self):
        self.id = None
        self.name = None
        self.type_id = None
        self.href = None
        self.web_url = None
        self.ip = None

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_ip(self, ip):
        self.ip = ip

    def get_ip(self):
        return self.ip


class Connection:

    teamcity_headers = {"Authorization": "Bearer eyJ0eXAiOiAiVENWMiJ9.SG5nSEJkY0xaZEFzWWYwY0pnTGI4VTdjNlJn.OWRjZjg0YTAtNjU4Ni00ZTljLWE0OTktODRlNzI3ODAxMWVj", \
                        "Content-Type": "application/xml"}

    def __init__(self):
        self.agent_xml_url = "http://192.168.1.116:8111/app/rest/agents?includeDisconnecd=false" 
        self.parameters_url = "http://192.168.1.116:8111/app/rest/buildTypes/id:RunHospitalTesting_StartOfTesting/parameters"
        self.default_pool_url = "http://192.168.1.116:8111/app/rest/agentPools/id:0/agents"
        self.agents = []

    def get_xml(self, url):
        xml_string = requests.get(url, headers=self.teamcity_headers).text
        return xml_string

    def map_agent_from_xml(self):
        agent_xml = self.get_xml(self.agent_xml_url)
        processor = declxml.array(declxml.user_object('agent', Agent, [
            declxml.string('.', attribute='id', alias='id'),
            declxml.string('.', attribute='name', alias='name'),    
            declxml.string('.', attribute='typeId', alias='type_id'),
            declxml.string('.', attribute='href', alias='href'),
            declxml.string('.', attribute='webUrl', alias='web_url')]), nested='agents')
        self.agents = declxml.parse_from_string(processor, agent_xml)
        return

    def get_agent_ip(self, agent):
        server = "http://192.168.1.116:8111"
        agent_ip = ""
        xml = self.get_xml(server + agent.href)
        agent_attributes = ET.fromstring(xml).attrib
        agent_ip = agent_attributes.get("ip")
        agent.set_ip(str(agent_ip))
        return

    def post_argument(self, url, data):
        r = requests.post(url, headers=self.teamcity_headers, data=data)
        return r.text

    def post_ip_as_arguments(self):
        main_agent_name = "main_agent"
        for agent in self.agents:
            self.get_agent_ip(agent)
            if re.match(main_agent_name, agent.get_name()):
                continue
            else:
                payload = '<property name="agent' + agent.get_id() + '" value="' + str(agent.get_ip()) + '"/>'
                response = self.post_argument(self.parameters_url, data=payload)
                print(response)
        return


def main():
    connection = Connection()
    connection.map_agent_from_xml()
    connection.post_ip_as_arguments()


main()