import subprocess
import time

def pingAuto():
	count=0
	time_val =0
	packets=input("Enter no of packets -c: ")
	host=input("Enter Hostname: ")
	time_val=int(input("Enter Time Interval (in Seconds): "))
	while True:
		count+=1
		p= subprocess.Popen(["ping","-c",packets,host],stdout=subprocess.PIPE)
		output,err = p.communicate()
		print(output)

		file1 = open("output.txt","a+")
		strout = str(output,'utf-8')
		countout = str(count)
		temp = "Attempt "+countout+"\n"+strout
		file1.write(temp)
		time.sleep(time_val)
		print("sleeping for ",time_val," second(s).....\n")

pingAuto()
