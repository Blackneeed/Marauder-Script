import os

def fileplus(file, text, new_line : bool = True):
    if new_line:
        b = [text + "\n"]
        if os.path.exists(file):
            with open(file, "r") as a:
                b = a.readlines()
                b.append(text + "\n")

        with open(file, "w") as a:
            a.writelines(b)
    elif not new_line:
        b = [text]
        if os.path.exists(file):
            with open(file, "r") as a:
                b = a.readlines()
                b.append(text)

        with open(file, "w") as a:
            a.writelines(b)
def fileminus(file):
    if os.path.exists(file):
        os.system('del "' + file + '"' + " /s /q /f")