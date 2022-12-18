def main():
    msg=input("")
    user(msg)

def user(msg):
    new_msg=msg.replace(" ","...")
    print(new_msg)

main()
