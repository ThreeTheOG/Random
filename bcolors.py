class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINKING = '\33[5m'
    EXPERIMENTWITHME = WARNING + UNDERLINE

print(f'{bcolors.EXPERIMENTWITHME}WARNING{bcolors.ENDC}{bcolors.WARNING}: You are being warned for a reason, check logs.{bcolors.ENDC}')