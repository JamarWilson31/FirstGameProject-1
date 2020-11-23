print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

health = 10



if age >= 18:
  print("Hello", name, "you are old enough to play!")

  wants_to_play = input("Do you want to play? ").lower()
  if wants_to_play == "yes":
    print("Awesome lets play!")
    print("You are starting with", health, "health. Goodlluck!")

    left_or_right = input("First choice... Left or Right (left/right)?")
    if left_or_right == "left":
      ans = input("Nice, you follow the path and reach a hidden Basketball court by the sea... Do you make your way towards the courts or do you walk towards the water (basketball/water)? ")

      if ans == "basketball":
        print("As you approached the basketball court you noticed Lebron James playing basketball and asked you to shoot with him... Upon shooting with Lebron he lets you in on a secret island with treasure nearby.")

      elif ans == "water":
        print("You take in the amazing view of the water and a noticed an inhabited island in your horizon. As you stare in amazement, a snake bites you, you managed to get away losing 5 health.")
        health -= 5
      
      ans = input("You notice a row boat and a bridge to the island. Which way do you head (boat/bridge)? ")
      if ans == "boat":
        print("You start rowing and realized the cork of the boat is missing. You start to sink and lose 5 health.")
        health -=5
      
        if health <= 0:
          print("You now have 0 health and lost the game...")
        
        else:
          print("But made it to the Island of treasure... you win!")


      else: 
        print("As you walk along the bridge open's up for a oncoming boat... You fall in the water and drown... What a terrible decision! #Gameover") 




    else:
        print("You lost")



  



  else:
    print("Cya...")

    
else:
  print("You are not old enough to play...")

