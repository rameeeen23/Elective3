#JOHN DAVE B. FUERTE

#Dictionary

#github.com/rameeeen23

#johndavefuerte@gmail.com

print ("\n\t\t Great Tomb of Nazarick\n\t\t\tFloor Guardians \n\n 1. Albedo \t\t 2. Shalltear Bloodfallen \n 3. Demiurge \t\t 4. Cocytus \n 5. Aura Bella Fiora \t 6. Mare Bella Fiore \n 7. Victim \t\t 8. Gargantua \n 9. Pandora's Actor \n")
def nazarick():

    dave = {"1": " Name: Albedo \n Gender: Female \n Height: 170cm \n Race: Succubus \n Occupation: Guardian Overseer", "2" : " Name: Shalltear Bloodfallen \n Gender: Female \n Height: 140cm \n Race: True Vampire \n Occupation: 1st-3rd Floor Guardian", "3" : " Name: Demiurge \n Gender: Male \n Height: 181cm \n Race: Arch Devil \n Occupation: 7th Floor Guardian", "4" : " Name: Cocytus \n Gender: Male \n Height: 2.5m \n Race: Vermin Lord \n Occupation: 5th Floor Guardian ", "5" : " Name: Aura Bella Fiora \n Gender: Female \n Height: 104cm \n Race: Dark Elf \n Occupation: 6th Floor Guardian ", "6" : " Name: Mare Bello Fiore \n Gender: Male \n Height: 104cm \n Race: Dark Elf \n Occupation: 6th Floor Guardian", "7" : " Name: Victim \n Gender: Unknown \n Height: 1m \n Race: Angel \n Occupation: 8th Floor Guardian", "8" : " Name: Gargantua \n Gender: None \n Height: 30m \n Race: Golem \n Occupation: 4th Floor Guardian", "9" : " Name: Pandora's Actor \n Gender: Male \n Height: 177cm \n Race: Doppleganger \n Occupation: Guardian of the Treasury",}

    ainz = input("\n NO.  ")
    if ainz == 1:
        print dave["1"]
    elif ainz == 2:
        print dave["2"]
    elif ainz == 3:
        print dave["3"]
    elif ainz == 4:
        print dave["4"]
    elif ainz == 5:
        print dave["5"]
    elif ainz == 6:
        print dave["6"]
    elif ainz == 7:
        print dave["7"]
    elif ainz == 8:
        print dave["8"]
    elif ainz == 9:
        print dave["9"]
    else:
        print ("Wait for more!!!")
        return nazarick()
    return nazarick()

    
nazarick()