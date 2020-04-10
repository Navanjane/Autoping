import subprocess
import time

def pingAuto():
	count=0
	packets=input("Enter no of packets -c: ")

	host=input("Enter Hostname: ")
	while True:
		count+=1
		p= subprocess.Popen(["ping","-c",packets,host],stdout=subprocess.PIPE)
		output,err = p.communicate()
		print(output)

		file1 = open("output.txt","a+")
		strout = str(output,'utf-8')
		countout = str(count)
		temp = "Attempt "+countout+"\n"+strout
	#file1.write("Attempt "+countout)
	#file1.write(strout)
		file1.write(temp)
		time.sleep(3)
		print("sleeping or 3 seconds.....\n")

pingAuto()
