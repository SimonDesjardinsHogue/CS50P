def main():
    file = input("File name: ").strip().lower()

    if file == ".gif":
        print("image/gif")
    elif file == ".jpg" or file == ".jpeg":
        print("image/jpeg")
    elif file == ".png":
        print("image/png")
    elif file == ".pdf":
        print("application/pdf")
    elif file == ".txt":
        print("application/txt")
    elif file == ".zip":
        print("application/zip")
    else:
        print("application/octet-stream")



main()
