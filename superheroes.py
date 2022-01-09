import requests

TOKEN = "2619421814940190"

class Superheroes():
    def __init__(self,name,token):
        self.name = name
        self.token = token

    def get_intelligence_by_name(self,name):
        url = f"https://superheroapi.com/api/{self.token}/search/{self.name}"
        response = requests.get(url).json()
        for item in response['results']:
            return item['powerstats']['intelligence']

if __name__=="__main__":

    Hulk = Superheroes("Hulk",TOKEN)
    Captain_America = Superheroes("Captain America",TOKEN)
    Thanos = Superheroes("Thanos",TOKEN)

    intelligence_dict={ Hulk.name: int(Hulk.get_intelligence_by_name("Hulk")),
                        Captain_America.name : int(Captain_America.get_intelligence_by_name("Captain America")),
                        Thanos.name : int(Thanos.get_intelligence_by_name("Thanos"))}

    max_intelligence = max(intelligence_dict.values())
    for item in intelligence_dict:
        if int(intelligence_dict[item]) == max_intelligence:
            print(f"Самый умный из супергероев {item}")



