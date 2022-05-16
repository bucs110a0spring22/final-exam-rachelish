import requests

class FruityVice:
  def __init__(self):
    self.url = f'https://www.fruityvice.com//api/fruit/all'
  def get(self):
    r = requests.get(self.url)
    response = r.json()

    loop = True

    while loop:
      for i, a in enumerate(response):
        print(i, a['name'])
      user = int(input('Choose a fruit (input a number from 0-30): '))
      
      forbidden_fruit = [5, 9, 13, 14]
      for i in range(len(forbidden_fruit)):
        if user == forbidden_fruit[i]:
          print("DON'T GIVE THIS TO YOUR PET")
          loop = False
        break


