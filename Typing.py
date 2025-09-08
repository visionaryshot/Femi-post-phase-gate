import time

sentence = "Somebody shout Master jesus!!!!!!!!."

print("\nWelcome to the Typing Speed Test!")
print("Type the following sentence above exactly as it shown:")
print("\n" + sentence + "\n")

start_time = time.time()

typed = input("Start typing here: ")

end_time = time.time()

time_taken = end_time - start_time
time_in_minutes = time_taken / 60

word_count = len(sentence.split())
wpm = word_count / time_in_minutes

correct_chars = 0
for count in range(min(len(sentence), len(typed))):
    if sentence[count] == typed[count]:
        correct_chars += 1

accuracy = (correct_chars / len(sentence)) * 100

print("\nResult ")
print(f"Time Taken: {round(time_taken, 2)} seconds")
print(f"Words Per Minute: {round(wpm, 2)} WPM")
print(f"Accuracy: {round(accuracy, 2)}%")
