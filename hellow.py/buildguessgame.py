secret_word = "Rajkumar"
guess = ''
gusses_count =0
gusses_limit =3
out_of_gusses = False
while secret_word != guess and not(out_of_gusses):
    if gusses_count<gusses_limit:
        guess= input("Enter the guess : ")
        gusses_count += 1
    else :
        out_of_gusses = True


if out_of_gusses :
    print("you lose the game Try next time ")
else :
    print("you win this game")