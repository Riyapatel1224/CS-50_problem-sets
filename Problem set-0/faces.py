#input string from user
def main():
    face=input("")
    convert(face)
#implement function "convert"
def convert(face):
    face=face.replace(":)","🙂")
    face=face.replace(":(","🙁")
    print(face)

main()
