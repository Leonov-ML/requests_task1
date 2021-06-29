import requests

your_token = "2619421814940190"

def get_data_hero(search_hero, token):
    hero_dict = {}
    for name_hero in search_hero:
        url = 'https://superheroapi.com/api/'
        full_url = url + token + "/search/" + name_hero
        r = requests.get(full_url)
        hero_json = r.json()
        hero_lst = []
        try:
            for current_hero in hero_json['results']:
                if current_hero['name'] == name_hero:
                    hero_lst.append(int(current_hero['powerstats']['intelligence']))
                    hero_dict[name_hero] = hero_lst

        except KeyError:
            print(f' Персонажа  {name_hero} нет')

    return hero_dict

if __name__ == '__main__':
    name = ['Hulk', 'Captain America', 'Thanos']
    hero_result = get_data_hero(search_hero=name, token=your_token)
    print(f'Cамый умный супергерой: {max(hero_result, key=(hero_result).get)}')