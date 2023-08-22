import random
import time

replies_8ball = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it ",
                 "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
                 "Reply hazy, try again",
                 "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                 "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful "]


def magic_8ball():
    print("================================ Magic 8 - Ball ================================")
    print("By: Sameed Ahmed                                                 USN: 2VX22CB043")
    i = 0
    while True:

        # Short trick to add "again" to the message when running for the second time.
        if i == 0:
            mini_str = ""
        else:
            mini_str = " again"
            i += 1

        run_inp = input("\nDo you want to Shake the Magic 8-Ball{}? \n [press Enter to shake again, or enter q "
                        "to quit]\n".format(mini_str))
        if run_inp.lower() == 'q':
            print("Ending program [Destroying the Magic 8-Ball] ....")
            time.sleep(2)
            print("Thank you for using my Magic 8-Ball program!")
            exit(0)
        else:
            print("\nShaking the Magic 8 ball")
            time.sleep(2)
            print("\nWaiting for magic to happen...")
            time.sleep(2)
            print("\n\nThe Magic 8-Ball says:")
            print("\t{}".format(random.choice(replies_8ball)))


magic_8ball()
