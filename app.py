import subprocess
import optparse
import calendar
import subprocess

def add_todo(insert):
	global to_do_dict
	to_do_dict={}

	print("*********************************")
	to_do_dict['monday']=input("Monday: ")
	to_do_dict['tuesday']=input("Tuesday: ")
	to_do_dict['wednesday']=input("Wednesday: ")
	to_do_dict['thursday']=input("Thursday: ")
	to_do_dict['friday']=input("Friday: ")
	to_do_dict['saturday']=input("Saturday: ")
	to_do_dict['sunday']=input("Sunday: ")

	print("*********************************")
	insert=False

	return insert,to_do_dict


def save_todo(todo):
	print("[+] Saving.......")
	print(to_do_dict)
	with open('to_do_dict.txt' , 'w') as f:
		for i in todo.keys():
			f.write(i)
			f.write('/')
		for i in todo.values():
			print(i)
			f.write(i)
			f.write('/')
		f.close()
	

def run_todo(run):
	print("[+] Running.......")
	with  open('to_do_dict.txt','r') as file:
		data = file.read().split('/')[7:]
		
	
	days= ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
	from datetime import date
	today = date.today()

	
	day = calendar.day_name[today.weekday()]
	print(day)
	html_data= """
	<!doctype html>
	<html>	
	<head>
	<link href="https://fonts.googleapis.com/css?family=Gugi" rel="stylesheet">
	<style>

		body{
		 background-color: black;
		}


			table {
		  table-layout: fixed;
		  width: 100%;
		  margin-top: 10%;
		  border-collapse: collapse;
		  border: 3px solid green;
		  color: white;
		  font-family: 'Roboto', sans-serif;
		}

		thead {
			color: #ddf95c;
			font-family: 'Quicksand', sans-serif;

		}



		thead th:nth-child(1) {
		  width: 30%;
		}

		thead th:nth-child(2) {
		  width: 20%;
		}

		thead th:nth-child(3) {
		  width: 30%;
		}

		thead th:nth-child(4) {
		  width: 20%;
		}
		thead th:nth-child(5) {
		  width: 35%;
		}
		thead th:nth-child(6) {
		  width: 35%;
		}

		th, td {
		  padding: 20px;
		}

		tbody td {
		  text-align: center;
		}

		tfoot th {
		  text-align: right;
		}

		#container{
			overflow: hidden;
		}
		#btable{
			float:left;
			width: 700px;
		}

		#stable{
			float: right;
			width: 400px;
			margin-top: 200px;
			margin-right: 20px;
		}

</style>
	</head>
	<body>
	<h1 style="font-size: 2em;color: #8700ff;font-family: 'Gugi', cursive;position: absolute;
	top: 5%;
	left: 40%;">YOUR PLANS FOR TODAY </h1>
	<table>
	<tbody style="display='center'">
			<tr>
			<td>Monday</td>
			<td>"""+data[0]+"""</td>

			</tr>
			<tr>
			<td>Tuesday</td>
			<td>"""+data[1]+"""</td>
			</tr>


			<tr>
			<td>Wednesday</td>
			<td>"""+data[2]+"""</td>
			</tr>

			<tr>
			<td>Thursday</td>
			<td>"""+data[3]+"""</td>
			</tr>


			<tr>
			<td>Friday</td>
			<td>"""+data[4]+"""</td>
			</tr>

			<tr>
			<td>Saturday</td>
			<td>"""+data[5]+"""</td>
			</tr>

			<tr>
			<td>Sunday</td>
			<td>"""+data[6]+"""</td>
			</tr>

	</tbody>
	</table>
	<h1 style="font-size: 2em;color: #8700ff;font-family: 'Gugi', cursive;position: absolute;top: 80%;left: 40%;">"""+day+""": </h1><h1 style="font-size: 2em;color: #8700ff;font-family: 'Gugi', cursive;position: absolute;top: 80%;left: 55%;">"""+data[days.index(day)]+"""</h1>
	</body>



	</html>

	"""
	with open('index.html', 'w+') as f:
		f.write(html_data)
	run= False

	subprocess.Popen(['start', 'index.html'],shell=True)
	return run




def main():
	global to_do_dict
	parser = optparse.OptionParser('usage -I insert new todo_app, -R run')
	parser.add_option('-I', dest="insert",type='string')
	parser.add_option('-R',dest="run",type='string')


	(options,args) = parser.parse_args()
	print(options.insert==None)
	if  (options.insert == None):
		insert=False
	elif options.insert.lower() == 'true':
		insert=True 
	else:
		insert=False


	while insert:
		insert,to_do_dict=add_todo(insert)
		save_todo(to_do_dict)
		print('Done Saving you can Run it Now to Get Daily Notifications on what to do :D')
	
	run=True
	if (options.run == None):
		run=False
	elif options.run.lower() == 'true':
		run=True
	else:
		run=False
	while run:
		run=run_todo(run)


main()

