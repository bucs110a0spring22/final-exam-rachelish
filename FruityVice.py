import requests

class FruityVice:
  def __init__(self):
    self.url = 'https://cat-fact.herokuapp.com/facts'
  def get(self):
    r = requests.get(self.url)
    response = r.json()
      

    for i in response:
      user = input("Want to hear a cat fact?: ")

      if user.upper() == "Y" :
        print(i['text'])
      else:
          break      

        
    #print('name')


