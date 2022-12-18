def main():
    filename = input("File name: ")
    extension(filename)


def extension(filename):
    if filename.strip().lower().endswith(".gif"):
        print("image/gif")
    elif filename.strip().lower().endswith(".jpeg"):
        print("image/jpeg")
    elif filename.strip().lower().endswith(".jpg"):
        print("image/jpeg")
    elif filename.strip().lower().endswith(".pdf"):
        print("application/pdf")
    elif filename.strip().lower().endswith(".zip"):
        print("application/zip")
    elif filename.strip().lower().endswith(".txt"):
        print("text/plain")
    elif filename.strip().lower().endswith(".png"):
        print("image/png")
    else:
        print("application/octet-stream")


main()
