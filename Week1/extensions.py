def main():
    file = input("File name: ").strip().lower()
    filesplit = file.split('.')[1]

    if filesplit == "gif":
        print("image/gif")
    elif filesplit == "jpg" or filesplit == "jpeg":
        print("image/jpeg")
    elif filesplit == "png":
        print("image/png")
    elif filesplit == "pdf":
        print("application/pdf")
    elif filesplit == "txt":
        print("text/plain")
    elif filesplit == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")



main()
