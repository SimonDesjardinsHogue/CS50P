def main():
    s = str(input())
    print (convert(s))

def convert(s):
    shap = s.replace(":)", "🙂")
    ssad = shap.replace(":(", "🙁")
    conv =  ssad
    return conv

main()
