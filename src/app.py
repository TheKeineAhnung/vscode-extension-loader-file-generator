from generator.generator import generate_shell_file, generate_powershell_file
from generator.get_extensions import get_own_extentions

print("Welcome to the vscode extension loader file generator!")
print("This creates a shell or powershell file that you can use to install all installed extensions (you can also remove as many as you like).")
print("You can only install all extensions or none once you have generated the file.")
print("You can use this, for example, as a backup for your own extensions or to share your extensions with friends.")

author = input("Please enter the author's name: ")
while author.strip() == "":
  author = input("Please enter the author's name: ")
save_path = input("Please enter the path where you want to save the file: ")
while save_path.strip() == "":
  save_path = input("Please enter the path where you want to save the file: ")
save_name = input("Please enter the name of the file (default vscode-extension-installer): ")

file_type = input("Please enter the type of file you want to create (shell or powershell): ")

extensions = get_own_extentions()

check_extensions = input("Do you want to check the extensions before creating the shell file? (y/n) ")
if check_extensions.lower().strip() == "y":
  new_extensions = extensions.copy()
  for extension in extensions:
    extension_keep_input = input(f"Keep '{extensions[extension]['author']}.{extensions[extension]['name']}@{extensions[extension]['version']}'? (y/n) ")
    
    if extension_keep_input.lower().strip() == "n":
      del new_extensions[extension]
  extensions = new_extensions

generated_file = False

if file_type.lower().strip() in ["shell", "sh"]:
  if (save_name.strip() == ""):
    generated_file = generate_shell_file(author_name=author, save_path=save_path, extensions=extensions)
  else:
    generated_file = generate_shell_file(author_name=author, save_path=save_path, extensions=extensions, save_name=save_name)
elif file_type.lower().strip() in ["powershell", "ps1"]:
  if (save_name.strip() == ""):
    generated_file = generate_powershell_file(author_name=author, save_path=save_path, extensions=extensions)
  else:
    generated_file = generate_powershell_file(author_name=author, save_path=save_path, extensions=extensions, save_name=save_name)

if generated_file:
  print("File was successfully generated.")
else: 
  print("An error occured while generating the file.")

input("Press enter to close this window...")