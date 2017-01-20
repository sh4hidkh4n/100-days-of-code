def main():
	print("1-%s\n2-%s\n3-%s" % ("Add Log", "Add Timeline", "Exit"))
	logFileName = "log.md"
	timelineFileName = "timeline.md"
	option = int(input(">>> "))
	if option == 1:
		autoMode = str(input("Auto Detect Last Day?(Y/N)\n>>> ")).lower()
		if autoMode != 'n':
			print("""
		[*] Auto mode is only work if you cloned my repo!
		[*] If not then just make your log.md looks like mine.
					(@github.com/shahidkh4n)
				""")
			logFile = open(logFileName, "r")
			lastDayString = logFile.readlines()[-5:-4][0]
			print(lastDayString)
			logFile.close()
			import re
			lastDay = int(re.findall(r'Day [0-9]{1,3}', lastDayString)[0].split(" ")[1])
			currentDay = lastDay+1
			day = currentDay
			print("[+] Last Day was %s " % (lastDay))
		else:
			day = str(input("[-] Current Day (ex. 5)\n>>> "))	
		template = """
### Day {day}: {date}

**Today's Progress**: {progress}

**Thoughts:** {thoughts}"""
		progress = str(input("[-] Progress (I did something 'X')\n>>> "))
		thoughts = str(input("[-] Thoughts (What you feel about it?)\n>>> "))
		import time
		date = time.strftime("%B, %d %Y")
		with open(logFileName, "a") as log:
			log.write(template.format(day=day, date=date, progress=progress, thoughts=thoughts))
		print("[+] Successful")
		wantToCommit = str(input("[-] want to commit changes to Github?(y/n)\n>>> "))
		if wantToCommit.lower() != 'n':
		    print("*** You must have your github setup already! ***")
		    from subprocess import call
		    call('git status')
		    call('git add .')
		    msg = str(input("[-] Commit message\n>>> "))
		    call('git commit -a -m "{}"'.format(msg))
		    wantToPush = True if (str( input("[-] want to push changed to Github?(y/n)\n>>> ") )).lower()!='n' else False
		    if wantToPush:
		        call('git push')
	elif option == 2:
		import os
		if not os.path.isfile("timeline.md"):
			wantToCreateTimeline = str( input("** You dont have timeline.md file. Want to create one?\n>>> ") ).lower()
			if wantToCreateTimeline != 'n':
				with open('timeline.md', 'w') as t:
					t.write("Timeline\n========\n\n**Tasks**\n")
					t.write(" 1. Add all previous days tasks")
		autoMode = str(input("[-] Auto Detect Last Timeline?(Y/N)\n>>> ")).lower()
		if autoMode == 'y':
			lastTimeLineNumber = ""
			with open(timelineFileName, "r") as timelineFile:
				lastTimeLineNumber = int( timelineFile.readlines()[-1].strip().split('.')[0] )
			currentTimeLineNumber = lastTimeLineNumber+1
		else:
			currentTimeLineNumber = str(input("[-] Current Time Line Number?\n>>> "))
		
		template = """
 {timelineNumber}. {timelineDescription}"""
		timelineDescription = str(input("[-] Whats this task is all about?\n>>> "))
		with open(timelineFileName, "a") as timelineFile:
			timelineFile.write(template.format(timelineNumber=currentTimeLineNumber, timelineDescription=timelineDescription))
		print("[+] Successful")
	elif option == 3:
		print("<> Any feedback ? Send here @twitter/sh4hidkh4n")
		exit(0)

if __name__ == "__main__":
	doc = """#################
    This is under development. But its pretty usable.
    I used this on my previous days. So if you find
    any bug just tweet me @sh4hidkh4n with traceback 
    log. Thank you!
#################"""
	print(doc)
	while True:
		main()