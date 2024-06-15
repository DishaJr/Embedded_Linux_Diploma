import pyautogui
import time
import subprocess

def open_vs_code():
  pyautogui.press('win')
  pyautogui.write('code')
  pyautogui.press('enter')

def install_extension(extension_name):
    """Installs a VS Code extension from the command line using the code command."""
    subprocess.run(["code", "--install-extension", extension_name], check=True)

# Open VS Code
open_vs_code()
time.sleep(5)

extensions_to_install = ['clangd', 'C++ Helper', 'C++ TestMate', 'CMake tools', 'CMake']
for extension in extensions_to_install:
    install_extension(extension)
    print(f"Installed extension: {extension}")
