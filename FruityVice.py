import requests

class FruityVice:
  def __init__(self):
    self.url = 'https://cat-fact.herokuapp.com/facts'
  def get(self):
    r = requests.get(self.url)
    response = r.json()
      
    for i in response:
      user = input("Want to hear a cat fact? (Y/N): ")
      if user.upper() == "Y" :
          print(i['text'])
      else:
          user2 = input("Well, do you want to hear a food fact? (Y/N)")
          if user2.upper() == "Y":
            print(i[])
                

        
    #print('name')


