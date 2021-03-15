print("Hello MIT Cell:\n")
w=''
q=input("please type your message: ")      # user message
a=int(input("\n enter value to shift transform message : "))  # value taken from user how much is to be shifted
for i in range(len(q)):                       # moving into the message
    if q[i].isalnum():                          # if alphabet or numeric value present
       w+=chr(ord(q[i])+ a)                    # we shifted it to value given by the user

    elif q[i] == " ":                          # if any space is present in message replacing it with @
        w=w+"@"
    elif q[i]==".":                            # full stop is replaced by #
        w=w+"#"
    else:
        w=w+q[i]                               # concatenating rest the of the message as it is
print("You send -" + w)
