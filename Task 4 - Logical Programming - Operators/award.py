swimming_time = int(input("What is your swimming time? ")) #First collect swimming time
print(swimming_time, "minutes.")

cycling_time = int(input("What is your cycling time? ")) #Second, collect cycling time.
print(cycling_time, "minutes.")

running_time = int(input("What is your running time? ")) #Third, collect running time.
print(running_time, "minutes.")

qualifying_time = swimming_time + cycling_time + running_time #Then collect the total triathlon time.
print("Your" + " " + "qualifying time is" + " " + str(qualifying_time) + " " + "minutes.")

if qualifying_time <= 100:                              #Then carry out if statements to comply with time ranges
    print("Provinical Colours")

elif qualifying_time >= 101 and qualifying_time <= 105:
    print("Provincial Half Colours")

elif qualifying_time >= 106 and qualifying_time <= 110:
    print("Provincial Scroll")

else:
    print("No award.")