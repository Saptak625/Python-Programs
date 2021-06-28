from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

for num in range(42):
  sheet["A"+str(num+2)] = num+1

sheet["B1"] = "Cults Saptak is Currently Involved In"

listOfCults = ["Lifeism", "Future-Citiesism", "GRAINESism", "42ism", "Being-a-personism", "Folding-paperism", "Typing-keys-for-a-programism", "Spreadsheetism", "Arguing-in-a-formal-mannerism", "Operation-snackism", "Encryptionism", "Interacting-with-peopleism", "ICBMism", "Poisoning-Pigeons-in-the-Parkism", "Writing-with-consumer-blue-pens-ism", "Making-random-programs-for-no-reasonism", "Stalkerism", "Computerism", "Staying-at-home-in-a-pandemicism", "Lobochevsky-ism", "Defenestrationism", "Skipping-math-class-to-do-random-puzzlesism", "Githubism", "Mathematicsism", "Overcomplicating-a-problemism", "Communism-Sympathesizerism", "Having-100-tabs-open-at-any-one-timeism", "GETTING-VERBEDism", "Getting-rejectedism", "Notificationism", "Being-in-a-cultism", "Getting-yelled-by-the-bus-driver-for-not-sitting-in-a-seat-ism"]

print(len(listOfCults))

for i in range(len(listOfCults)):
  sheet["B"+str(i+2)] = listOfCults[i]


workbook.save(filename="hello_world.xlsx")
