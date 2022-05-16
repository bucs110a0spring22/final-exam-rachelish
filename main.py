import requests
#for shuffling possible answers later
import random 
import FruityVice
import Cats

def main():
  catAPI = Cats.Cats()
  results = catAPI.get()

  fruitsAPI = FruityVice.FruityVice()
  results2 = fruitsAPI.get()

main()
  


