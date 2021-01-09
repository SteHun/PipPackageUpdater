from subprocess import check_output
from os import system
print("collecting installed packages...")
packages_str = check_output("python -m pip list --format freeze", shell=True, universal_newlines=True)
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

print("downloading and installing updates...")
command = "python -m pip install -U "
for item in packages_list:
    command += f"{item} "
system(command)
print("don't forget to run pip check every once in a while!")