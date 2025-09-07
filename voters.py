candidates = []
voters = []
votes = {}
voted_voters = []


def register_candidate():
    print(" Candidate Registration ")
    name = input("Enter candidate name: ")
    age = int(input("Enter age: "))
    education = input("Enter highest Education qualification : ")
    party = input("Enter political party: ")
    sponsored = input("Is the candidate sponsored by the party? (yes/no): ")
    criminal_record = input("Any criminal record involving dishonesty or fraud? (yes/no): ")
    tax_years = int(input("How many years of tax evidence? "))

    if age >= 25 and education.upper().strip() == "ssce" or "ond" or "hnd" or "bsc" or "msc" or "phd" and sponsored.upper().strip() == "yes" and criminal_record.upper().strip() == "no" and tax_years >= 3:
        candidates.append(name)
        votes[name] = 0
        print(f"{name} has been successfully registered.\n")
    else:
        print("Candidate does not meet the requirements.\n")


def register_voter():
    print("\nVoter Registration ")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    nationality = input("Are you a Nigerian citizen? (yes/no): ")
    state = input("Which state are you from: ").lower().strip()
    valid_states = [
        "abia", "adamawa", "akwa ibom", "anambra", "bauchi", "bayelsa", "benue",
        "borno", "cross river", "delta", "ebonyi", "edo", "ekiti", "enugu", "fct",
        "gombe", "imo", "jigawa", "kaduna", "kano", "katsina", "kebbi", "kogi",
        "kwara", "lagos", "nasarawa", "niger", "ogun", "ondo", "osun", "oyo",
        "plateau", "rivers", "sokoto", "taraba", "yobe", "zamfara"
    ]

    if age >= 18 and nationality.lower().strip() == "yes" and state in valid_states:
        voters.append(name)
        print("You are eligible")
        print(f"{name} is registered and eligible to vote.\n")
    else:
        print("You are not eligible to vote.\n")

def vote_process():
    print("Voting ")
    name = input("Enter your name: ")
    if name in voters and name not in voted_voters:
        print("Candidates:")
        for candidate in candidates:
            print(f" {candidate}")
        choice = input("Enter the name of the candidate you want to vote for: ")
        if choice in candidates:
            votes[choice] += 1
            voted_voters.append(name)
            print("Vote cast successfully!\n")
        else:
            print("Invalid candidate.\n")
    elif name in voted_voters:
        print("Thief, how many times you wan vote\nYou have already voted.\n")
    else:
        print("You are not a registered voter.\n")
 
def count_votes():
    print("\n Counting Votes ")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} vote(s)")
    print()

def show_results():
    print("\n Election Result ")
    if votes:
        max_votes = max(votes.values())
        winners = [name for name, count in votes.items() if count == max_votes]
        if len(winners) == 1:
            print(f"The winner is {winners[0]} with {max_votes} votess!")
        else:
            print("Draw-Draw:")
            for winner in winners:
                print(f"{winner} ({max_votes} vote(s))")
    else:
        print("No votes have been cast yet.\n")


def intro():
    eligible_candidates = []
    while True:
        print("WELCOME TO INEC PORTAL")
        print(" Voting System Menu")
        print("1. Register Candidate")
        print("2. Register Voter")
        print("3. Vote")
        print("4. Count Votes")
        print("5. Show Election Result")
        print("6. Exit")
        users_choice = input("Select any option: ")

        if users_choice == "1":
            eligible_candidates.append(register_candidate())
        elif users_choice == "2":
            register_voter()
        elif users_choice == "3":
            vote_process()
        elif users_choice == "4":
            count_votes()
        elif users_choice == "5":
            show_results()
        elif users_choice == "6":
            print("Exit")
            break
        else:
            print("Invalid choice. Try again.\n")

intro()


