### importing requried moudule
import os
import time
import webbrowser
from pytube import YouTube


## creating banner 
def banner():
    os.system("clear")
    print("""
      
          ░░░░░░███████]▄▄▄▄▄▄▄▄          
         ▂▄▅█████████▅▄▃▂                   
         I███████████████████].            
          ◥ ⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...               
          version - o.1                            
          created by satyabrata mitra  
       choose one option !!    
        1.vedio download 
        2.support us
        3.exit    
          """)
#creating maun fun to downlod youtube 
def main_fun():
     #try:

            link = str(input("enter vedio link :" , ))
            youtube = YouTube(link)
            print(f"getting vedio info !!")
            time.sleep(1)
            print(f"video title : {youtube.title}")
            time.sleep(1)
            print(f"vedio views : {youtube.views}")
            time.sleep(1)
            print(f"vedio decripetions : {youtube.description}")
            time.sleep(1)
            print(f"vedio id : {youtube.video_id}")
            time.sleep(1)
            print(f"vedio tumnail download :{youtube.thumbnail_url}")
            time.sleep(1)
            loction = str("where you want to download the vedio :")
            choise  =str(input("do you want only audio (y/n):"))

            if choise =="y" or choise=="yes" or choise=="YES":
                # try:  
                  only_audio = youtube.streams.filter(only_audio=True).first()
                  only_audio.download(loction,filename=f"{youtube.title}.mp3")
                  print(f"your audio has sussesfully downloaded on {loction} and file name is {youtube.title}.mp3")
                  time.sleep(2)
                # except:
                 #     os.abort()
                  #    os.system("clear")
                   #   print("opps !! chake your internet connection !!")
                      
                 
            elif choise =="n" or choise=="no" or choise=="NO":
             #    try:
                  
                        both_vedio_audio = youtube.streams.get_highest_resolution()
                        both_vedio_audio.download(loction)
                        time.sleep(2)
                        print(f"your vedio has succesfully downloaded on {loction} and file name is {youtube.title}.mp4")
         #        except:
          ##           os.system("clear")
            #          print("an erroe accursed !! | or chake your internet connection!!")
        #    else:
              #   os.system("clear")
               #  print("an error accoursed !! or chake your internet connection !!")

            
    # except:
     #     os.abort()
      #    os.system("clear")
       #   print("an error comes !!")
 
# creating the menu 

def menu(): 
    options = input("options : ")
    if options == "1":
          main_fun()
          
    elif options == "2":
          webbrowser.open("https://www.youtube.com/@hackwithlassan")
        
    elif options == "3":  
          print("Thanks for using my  tool !!")
    else:
        os.system('clear')
        print("invalid option")



         
if __name__ == "__main__":
    banner()
    menu()