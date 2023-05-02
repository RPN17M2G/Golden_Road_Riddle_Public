import os
import time

def main ():
   print("Starting docker compose, opening docker desktop and opening the react web application on your default browser!")

   #Check if docker Desktop is installed in C:/Program Files
   have_docker = os.path.exists("C:\Program Files\Docker")
   have_docker_desktop = os.path.exists("C:\Program Files\Docker\Docker\Docker Desktop.exe")

   if not have_docker:
       print("Please install Docker Desktop and try again.\nDocker desktop install url is: https://www.docker.com/products/docker-desktop/")
       return 1
   elif not have_docker_desktop:
       print( "Docker is installed but didnt find this file: C:\Program Files\Docker\Docker\Docker Desktop.exe")
       return 1
   
   os.startfile("C:\Program Files\Docker\Docker\Docker Desktop.exe")

   os.system("docker compose  up -d --build") #Building docker compose

   time.sleep(2) #So there will be no waiting for the react to start
   os.system("START http://localhost:3000") #Open react web application

   input("Press enter to close all the programs(excpet for the web tab): ") #Just waits to input

   os.system("docker-compose down") #Closing the container with the react client and the flask server

   print("Succusfully closed.")


if __name__ == '__main__':
    main()