amount = int(input("How much money would you like to withdraw? "))

note1 = amount//50
note2 = (amount%50)//20
note3 = ((amount%50)//20)//10
note4 = (((amount%50)/20)//10)//5

print(f"Notes of £50: {note1}\nNotes of £20: {note2}\nNotes of £10: {note3}\nNotes of £5: {note4}")

