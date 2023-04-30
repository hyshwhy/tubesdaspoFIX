import Load
import Commands
import Database

Database.init()
Load.load()


while True:
  masukan = input(">>> ")
  Commands.run(masukan)
  if masukan=="exit":
    break
  