import requests

def get_request():
    url = 'https://superheroapi.com/api/2619421814940190/'
    params = {}
    headers = {'Authorization': '2619421814940190'}
    return requests.get(url, params=params, headers=headers)

def search_id_intelligence(name_list):
    dictonary = {}

    for name in name_list:
        Hero = requests.get('https://superheroapi.com/api/2619421814940190/search/' + name).json()
        id = Hero['results'][0]['id']
        Hero = requests.get('https://superheroapi.com/api/2619421814940190/' + id).json()
        intelligence = Hero['powerstats']['intelligence']
        dictonary.setdefault(name)
        dictonary[name] = {'id' : id, 'intelligence' : intelligence}
    return dictonary

def sorting(dictonary):
    new_dictonary = {}
    sorted_keys = []
    
    for name in dictonary.keys():
        new_dictonary.setdefault(name)
        new_dictonary[name] = int(dictonary[name]['intelligence'])
    
    sorted_keys = sorted(new_dictonary, key = new_dictonary.get, reverse=True)
    return print('The hero with the most intelligence:', sorted_keys[0], '=', new_dictonary[sorted_keys[0]])

hero_list = ['Hulk', 'Captain America', 'Thanos']
dictonary = search_id_intelligence(hero_list)
sorting(dictonary)