import platformimport osos.system('termux-setup-storage')os.system('git pull')try:os.system('touch .prox.txt')except:passarc = str(platform.uname().machine)if 'arm' in arc:	__import__("Troyy").keyx()elif 'aarch' in arc:	__import__("Troy").keyx()else:	exit(f' Unknow device machine {arc}')
