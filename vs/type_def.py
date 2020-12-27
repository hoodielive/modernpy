def confirm() -> bool:
    yes = { "yes", "y" }
    no = { "no", "n" }
    while ( answer := input("Confirm: ")).lower() not in (yes | no):
        print("Please respond with yes or no.")
    return answer in yes

confirm()
