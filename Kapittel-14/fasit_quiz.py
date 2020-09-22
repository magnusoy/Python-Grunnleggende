from random import shuffle

try:
    import requests  # Husk å importer modul
except ModuleNotFoundError:
    print("Last ned modulen. pip install requests")

score = 0
on_question = 1
TOTAL_QUESTIONS = 10
playing = True
URL_API = f"https://opentdb.com/api.php?amount={TOTAL_QUESTIONS}"

while playing:
    print("\nVelkommen til Quiz!\n")
    response = requests.get(URL_API)
    content = dict(response.json())
    results = content["results"]
    for result in results:
        print(f"{on_question}/{TOTAL_QUESTIONS}")
        category = result["category"]
        question = result["question"]
        correct_answer = result["correct_answer"]
        answers = list([*result["incorrect_answers"], result["correct_answer"]])
        shuffle(answers)
        print("\n" + category)
        print(question)
        for index, answer in enumerate(answers):
            print(f"{index+1}: {answer}")

        user_choise = 0
        asking = True

        while asking:
            try:
                user_choise = int(input(f"Hvilket svar er riktig (1-{len(answers)})?\n"))
                user_picked = answers[user_choise-1]
                asking = False
            except IndexError:
                print(f"\nIngen alternativ på valg nummer {user_choise}\nPrøv på nytt!")
            except ValueError:
                print(f"\nFeil input. Vennligst skriv et tall!")

        if user_picked == correct_answer:
            score += 1
        print(f"\nPoeng: {score}")
        on_question += 1
            
    print(f"\nTotal score: {score}\n")
    still_playing = input("Fortsett å spille? [Ja/Nei]\n")
    if still_playing.lower() != "ja":
        playing = False
    else:
        score = 0
        on_question = 1

print("\nSnakkes!")