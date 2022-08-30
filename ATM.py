print("🙏🙏🙏Welcome to SBI Bank ATM🙏🙏🙏")
balance=50000
card=input("select your card👉 1.ATM💳,2.credit card💳:")
if card=="1" or card=="2":
    language=input("select your language👉 1.english🤬, 2.hindi:")
    print()
    if language=="1" :
        account=input("select your account👉1.current,2.saving:")
        if account =="1" or account=="2":
            transaction=(input("select your transaction👉 1.balance enquari💰,2.withdraw money💵,:"))
            if transaction=="1":
                pin=int(input("enter your four digit pin🤫:"))
                if pin==1234:
                    print("total balance is💰👉",balance)
                    print("your transaction is completed 😊please collect your card💳")
                    sleep=input("do you want sleep👉1.yes or 2.no: ")
                    if sleep=="1":
                        print("your transaction is completed")
                        print(" please collect your sleep🧾 and card💳")
                    else:
                        print("your transaction is completed please collect your card💳")
                else:
                    print("please enter valid pin😯")
                    print("try again🤬")
            elif transaction=="2":
                pin=int(input("enter your four digit pin🤔:"))
                if pin==1234:
                    amount=int(input("enter total amount in the form of 100,200💰,500,2000💵:"))
                    if amount>=0 or amount<=50000:
                        if amount%100==0:
                            print("please collect your amount💰")
                            print("your current balance is 💰",balance-amount)
                        else:
                            print("pleas enter valid amount😮")
                        sleep=input("do you want sleep👉 1.yes, 2.no:")
                        if sleep=="1":
                            print("please collect your sleep📼")
                            print("your transaction is completed😊 please collect your card💳")
                        else:
                            print("your transaction is completed😊 please collect your card💳")
                    else:
                        print("please enter valid amount🤬")
                else:
                    print("please enter valid pin😑")
                    print("try again🤬")
    if language=="2":
        account=input("apna khata chune👉 1.vartman khata, 2.bachat khata:")
        if account=="1" or account=="2":
            len_den=input("apna len den chune👉1.💰balance puchtach🤔, 2. p💰aise nikalana:")
            if len_den=="1":
                pin=int(input("apna char ank pin dale🤫:"))
                if pin==1234:
                    print("apka kul shesh💰 hai",balance)
                    print("apka len den purn hua")
                    rasid=input("aapko rasid chahiye👉1.ha😁 2. nahi😑")
                    if rasid=="1":
                        print("apka len den purn hua😮")
                        print("krupaya apni rasid aur apna card nikal le😊")
                    else:
                        print("apka len den purn hua krupaya apna card nikal le😊")
                else:
                    print("sahi pin dale🤬")
            elif len_den=="2":
                pin=int(input("apna char ank pin dale🤔:"))
                if pin==1234:
                    print("apka pin sahi hai🤫")
                    rashi=int(input("100,200,500,2000 ke rup me kul rashi darj kare: "))
                    if rashi>=0 or rashi<=50000:
                        if rashi%100==0:
                            print("krupaya apni rashi nikal le")
                            print("apke khate me kul rashi",balance-rashi)
                        rasid=input("aapko rasid chahiye👉1.ha,2.nahi:")
                        if rasid=="1":
                            print("apka len den pura hua")
                            print("krupaya apni rashid🧾 aur apna card nikal le")
                        else:
                            print("apka len den pura hua 😊kripaya apna card nikal le")
                    else:
                        print("krupaya manya🤐 rashi darj kare")
                else:
                    print("manya pin🤔 darj kare")
    # else:
        # print("you have only english or hindi language 😮please choose correct option🤬")               
else:
    print("please re-enter your card💳")