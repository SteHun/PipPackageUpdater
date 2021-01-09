import subprocess, os
print("collecting installed packages...")
packages_str = subprocess.check_output("python -m pip list --format freeze", shell=True, universal_newlines=True)
packages_list = [""]
add_letter = True

for letter in packages_str:
    if letter == "=":
        add_letter = False
    elif letter == "\n":
        add_letter = True
        packages_list.append("")
    elif add_letter:
        packages_list[len(packages_list)-1] += letter
del(packages_list[len(packages_list)-1])