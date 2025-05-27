#Zhicheng Zhu & Aidan Williams
#Dog Breeds
#2/27/2025

dog_breeds = ["Affenpinscher","AfghanHound","AiredaleTerrier","AkbashDog","Akita","AlapahaBlueBloodBulldog","AlaskanHusky","AlaskanMalamute","AmericanEskimoDog","AmericanFoxhound","AmericanPitBullTerrier","AmericanWaterSpaniel","AnatolianShepherdDog","AustralianKelpie","AustralianShepherd","Azawakh","Basenji","BassetBleudeGascogne","Beagle","Beauceron","BedlingtonTerrier","BelgianMalinois","BelgianTervuren","BerneseMountainDog","BlackandTanCoonhound","Bloodhound","BluetickCoonhound","Boerboel","BorderTerrier","BostonTerrier","BouvierdesFlandres","Boxer","BoykinSpaniel","BraccoItaliano","Briard","Brittany","Bullmastiff","CairnTerrier","CaneCorso","CardiganWelshCorgi","CatahoulaLeopardDog","CaucasianShepherd","CavalierKingCharlesSpaniel","ChineseCrested","Chinook","ChowChow","ClumberSpaniel","CockerSpaniel","CotondeTulear","Dalmatian","DogoArgentino","EnglishShepherd","EnglishSpringerSpaniel","Eurasier","FieldSpaniel","FinnishLapphund","GermanPinscher","GermanShepherdDog","GermanShorthairedPointer","GiantSchnauzer","GlenofImaalTerrier","GoldenRetriever","GordonSetter","GreatDane","GreatPyrenees","Greyhound","Harrier","Havanese","IrishSetter","IrishWolfhound","ItalianGreyhound","JapaneseChin","Keeshond","Komondor","Kuvasz","LabradorRetriever","LagottoRomagnolo","Leonberger","LhasaApso","Maltese","MiniatureSchnauzer","Newfoundland","NorfolkTerrier","Papillon","PembrokeWelshCorgi","PharaohHound","Plott","Pug","RedboneCoonhound","RhodesianRidgeback","Rottweiler","Samoyed","Schipperke","ScottishDeerhound","ShihTzu","SilkyTerrier","SoftCoatedWheatenTerrier","SpanishWaterDog","Vizsla","Weimaraner"]
dog_weights = [6 , 50 , 40 , 90 , 65 , 55 , 38 , 65 , 20 , 65 , 30 , 25 , 80 , 31 , 35 , 33 , 22 , 35 , 20 , 80 , 17 , 40 , 40 , 65 , 65 , 80 , 45 , 110 , 12 , 10 , 70 , 50 , 25 , 55 , 70 , 30 , 100 , 13 , 88 , 25 , 50 , 80 , 13 , 10 , 50 , 40 , 55 , 20 , 9 , 50 , 80 , 44 , 35 , 40 , 35 , 33 , 25 , 50 , 45 , 65 , 32 , 55 , 45 , 110 , 85 , 50 , 40 , 7 , 35 , 105 , 7 , 4 , 35 , 80 , 70 , 55 , 24 , 120 , 12 , 4 , 11 , 100 , 11 , 3 , 25 , 40 , 40 , 14 , 45 , 75 , 75 , 50 , 10 , 70 , 9 , 8 , 30 , 30 , 50 , 55 ]
filtered_list = []
#medium = 26 - 60
#large =>60

#Loop through weight list finding tiny dogs

def dog_size():
    x = input(" What kind of dog are you looking for? (tiny, small, medium, or large) :  ")
    if x ==  "tiny" :
        for i in range(len(dog_weights)):
            if dog_weights[i] <= 10:
                filtered_list.append(dog_breeds[i])

        print(filtered_list)

    if x ==  "small" :
        for i in range(len(dog_weights)):
            if dog_weights[i] <= 26 and dog_weights[i] > 11:
                filtered_list.append(dog_breeds[i])

        print(filtered_list)

    if x ==  "medium" :
        for i in range(len(dog_weights)):
            if dog_weights[i] <= 60 and dog_weights[i] > 26:
                filtered_list.append(dog_breeds[i])

        print(filtered_list)

    if x ==  "large" :
        for i in range(len(dog_weights)):
            if dog_weights[i] >= 60:
                filtered_list.append(dog_breeds[i])

        print(filtered_list)

dog_size()
