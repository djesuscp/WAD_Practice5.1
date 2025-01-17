import subprocess
from datetime import datetime

def run(message, command):
    currentDate = datetime.now()
    currentDateFormated = currentDate.strftime("%Y-%m-%d %H:%M:%S")
    try:
        if message == '' and 'commit' not in command:
            result = subprocess.run(command, text=True, shell=True, check=True, capture_output=True)
            if 'add' in command:
                print(f'Log> Git add -A succesfull.')
            elif 'push' in command:
                print(f'Log> Git push completed.')
        elif message == '' and 'commit' in command:
            result = subprocess.run(f'{command}"Emergency save dated: {currentDateFormated}"', text=True, shell=True, check=True, capture_output=True)
            print(f'Log> {result.stdout}')
        else:
            result = subprocess.run(f'{command}"{message}. Dated: {currentDateFormated}"', text=True, shell=True, check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f'Error> {e.stderr}')

if __name__ == '__main__':
    run('', f'git add -A')
    run(input('Input commit message> '), f'git commit -m')
    run('', f'git push')