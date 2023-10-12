# Generateur d'affirmation by ruth
robot = input("Quel est votre nom ? ")
print()
print("Bonjour", robot, "je suis un Robot je genère  des affirmations positive! pour cela vous repondrez à mes questions.")

activity = input("quel est votre activité preféré ? ")
print()
if activity == "dev":
   print("félicitations", robot, "vous êtes le meilleur", activity, "Continuez ainsi")
days = input("quel jour de la semaine aimez vous le plus ? ")
print()
if days == "samedi":
   print("wahou c'est bien le weekend profitez au max de votre preferé faite vous plaisir comme vous le voulez... mais soyez prudents! ")
   print()
elif days == "Lundi":
      print("Lundi le plus beau de la semaine ou nous puisons nos force pour demarer la semaine... Vive le lundi!!!!!!")
      print()
elif days == "Mardi":
      print("Mardi un jour magifique qui  t'aide à commencer en pleine energie la semaine...")
      print()
elif days == "Mercredi":
      print("Mercredi c'est un jour calme apaisant...!")
      print()
elif days == "jeudi":
      print("jeudi c'est un jour magique ou nous avons la chance de faire des choses magnifique..Soyez des gens biens !")
      print()
elif days == "Vendredi":
      print("ça sent beaucoup le weekend et aussi la fatigue... aller profiter bien de votre vos jour de repos.. soyez Aimable !!!")

else:
  print("Continuez vos Etudes si vous avez les moyens, poussez encore loin..très loin mdrr")
  print()
  print("Soyez des amoureux!!!!")


