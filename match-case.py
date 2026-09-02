#matchcase bilkul switch case ki tarah hai 
n = str(input("Enter a word: "))
match n:
    case "om":
        print("Myself")
    case "sumi":
        print("friend")
    case "bhaskar":
        print("2nd name")
    case _: #yeh default ki tarah kaam krta ha or isme break ki jarurat nhi
        print("unknown namne")