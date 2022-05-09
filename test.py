print("Tuckersoft ask how many weeks will it take you\n")
lead_time = input("To finish the completed version?\n")
if lead_time:
 lead_time = int(lead_time)
 if lead_time >= 21:
  print("Thats too long, we cant do a deal. Game Over.")
 elif lead_time <= 20:
  print("Congratulations, you got yourself a deal.")
 else:
  print("Please enter number of weeks")
