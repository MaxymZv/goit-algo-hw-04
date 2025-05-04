import sys
from pathlib import Path
import colorama


def sort_function(item):
      return (item.is_file(), item.name.lower())

def visualize_directory(directory_path: str, indent: int = 0):
    directory_path = Path(directory_path).resolve()
    if not directory_path.exists() or not directory_path.is_dir():
            return colorama.Fore.RED + f'Папка {directory_path} не існує.' + colorama.Style.RESET_ALL
    print(colorama.Fore.CYAN + f'\n{directory_path}' + colorama.Style.RESET_ALL)

    for item in sorted(directory_path.iterdir(), key=sort_function):
        prefix = "  " * indent
        if item.is_dir():
            print(prefix + colorama.Fore.BLUE + f'{item.name}' + colorama.Style.RESET_ALL)
            visualize_directory(item, indent + 1)
        else:
            print(prefix + colorama.Fore.GREEN + f'{item.name}' + colorama.Style.RESET_ALL)
if __name__ =='__main__':
    if len(sys.argv) != 2:
        print(colorama.Fore.RED + "Використання: visualizing_path.py <шлях_до_директорії>" + colorama.Fore.RESET)
    else:
     visualize_directory(sys.argv[1])
          
        
        
        
