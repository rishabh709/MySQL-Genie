def end():
	return('''———————————————————————————————————————————————————————
	
	''')
def enter_2coninue():
	while True:
			br1 = input("Press Enter to continue")
			if br1 =="":
				break
			else:
				print("\nYou have Entered",br1,"\nPlease press only Enter\n")
				continue
	return" "
def table(result, on =""):
	if type(result)!=list:
		result_list =[]
		result_list.append(result)
		result = [result_list]
	elif result==[]:
		return("---- Empty ----")
	if on!= "":
		cur.execute("desc "+on)
		fda = cur.fetchall()
		tb_name_lst =[]
		for i in fda:
			tb_name_lst.append(i[0])
		tb_name_lst = tuple(tb_name_lst)
		result.insert(0,tb_name_lst)
	dst=[]
	for i in range (len(result[0])):
		kst=[]
		for i1 in result:
			kst.append(str(i1[i]))
		m = max(kst, key=len)
		dst.append(m)
	top=""
	for i in range(len(dst)):
		length = len(dst[i])
		gap="-"*(length+2)
		b_first ="+"+gap+"+"
		top = top + b_first
		top = top.replace("++","+")
	c1=""
	cnt = 0
	for i in result:
		f=0
		b1=""
		for i1 in range (len(i)):
			data = i[i1]
			f = top.find("+",f+1)
			b1 = b1 + "| " + str(data)
			cnt = cnt + 1
			while len(b1) != f:
				b1 = b1 + " "
		c1 =c1+"\n"+ b1 + "|"
		if on != "":
			if cnt==len(i):
				c1=c1+"\n"+top
		final =top+c1+"\n"+top
	return(final)

def clean_screen():
	os.system('cls')

def DB(data):
	cur.execute("show databases")
	f0data,dbl= cur.fetchall(),[]
	for d in f0data:
		for d1 in d:
			dbl.append(d1)
	if data.isdigit():
		print("\n~~~~EROOR~~~~\n",data,"is not eligible for Database")
		print("\nIt should not be any Digit",)
	elif data in dbl:
		print("\n~~~~EROOR~~~~\nDatabase",data,"already exist")

	else:
		print("\n~~~~EROOR~~~~\nDatabase",data,"dose'nt exist")
	return" "

def execution(cmd,x=""):
	cur.execute(cmd)
	fe_d = cur.fetchall()
	if x !="":
		return(table(fe_d,x))
	return(table(fe_d))

def check_duplicate_in_tables(enterd_table_name):
	cur.execute("show tables")
	f_data = cur.fetchall()
	enterd_con2lst = []
	enterd_con2lst.append(enterd_table_name)
	if f_data == []:
		duplicate = False
		return duplicate
	else:
		for d in f_data:
			if enterd_con2lst == list(d):
				duplicate = True
				return duplicate

def conditional_input(print_obj,condition):
	while True:
		if condition == "int":
			user_input = input(print_obj)
			try:
				eval_obj = eval(user_input)
			except NameError:
				print("\n----Error----\n Invalid Entry \n Enter only Intigers\n")
			except SyntaxError:
				print("\n----Error----\n Invalid Entry \n Enter only Intigers\n")
				continue
			if type(eval_obj) == int:
				return user_input
			else:
				print("\n----Error----\n Invalid Entry \n Enter only Intigers\n")
				continue
def open_table(TableName):
	def list2str(xinput):
		string = ""
		for i in range (len(xinput)):
			string = string + xinput[i]
		return string
	cur.execute("select * from "+TableName)
	result = cur.fetchall()
	cur.execute("desc "+TableName)
	fda = cur.fetchall()
	tb_name_lst =[]
	for i in fda:
		tb_name_lst.append(i[0])
	tb_name_lst = tuple(tb_name_lst)
	max_list=[]
	result.insert(0,tb_name_lst)
	for i in range (len(result[0])):
		temp_list=[]
		for i1 in result:
			temp_list.append(str(i1[i]))
		max_list.append(max(temp_list, key=len))
	
	top=""
	for i in range(len(max_list)):
		length = len(max_list[i])
		gap="-"*(length+2)
		b_first ="+"+gap+"+"
		top = top + b_first
		top = top.replace("++","+")
	c1=""
	final_table=""
	old_len=1
	table_columns_count = 0
	i0gap = i1gap = 4
	for i in result:
		count = 0
		f=0
		b1=""
		for counti in i:
			count = count + 1
		for i1 in range (len(i)):
			data = i[i1]
			f = top.find("+",f+1)
			b1 = b1 + "| " + str(data)
			while len(b1) != f:
				b1 = b1 + " "
		num_gap = " "
		LenOfCount = len(str(table_columns_count))
		if LenOfCount>old_len:
			if LenOfCount%2 == 0:
				i0gap = (i0gap-1)
			elif LenOfCount%2 !=0:
				i1gap = (i1gap-1)
		elif LenOfCount == 1:
			pass
		while (len(i0gap*" "+str(table_columns_count)+i1gap*" ")) !=9:
			i1gap = i1gap + " "
		final_table = final_table +"\n"+"	"+num_gap+top +"\n"+i0gap*" "+str(table_columns_count)+i1gap*" "+b1+"|"
		old_len = len(str(table_columns_count))
		table_columns_count = table_columns_count + 1
		# ~ ADDING LAST OR END LINE(TOP)
	final_table = final_table + "\n"+" 	"+num_gap+top
	if final_table.startswith("\n"):
		final_table = final_table[1:]
	
	try:
		ff = 0
		len_divided_top = []
		for i in range (count):
			f1 = top.find("+",ff)
			f2 = top.find("+",f1+1)
			len_divided_top.append(top[f1+1:f2])
			ff= f1+1
	except:
		print("err")
		pass
	dec_to_chr = 65
	for i in range (len(len_divided_top)):
		top_div_div_lst = list(len_divided_top[i])
		div = len(top_div_div_lst)
		if div%2 == 0:
			place = (div//2)-1
			top_div_div_lst[place] = chr(dec_to_chr)
			topuplst = (list2str(top_div_div_lst)).replace("-"," ")
			len_divided_top[i] = " "+topuplst
			dec_to_chr = dec_to_chr + 1
		elif div%2 != 0:
			place = (div//2)
			top_div_div_lst[place] = chr(dec_to_chr)
			topuplst = (list2str(top_div_div_lst)).replace("-"," ")
			len_divided_top[i] = " "+topuplst
			dec_to_chr = dec_to_chr + 1
	print("	"+num_gap+(list2str(len_divided_top)))
	print(final_table)

def DB1(data):
	cur.execute("show databases")
	f0data,dbl= cur.fetchall(),[]
	for d in f0data:
		for d1 in d:
			dbl.append(d1)
	if data in dbl:
		pass
	else:
		print("\n~~~~EROOR~~~~\nDatabase",data,"dose'nt exist")
	return" "		
		
def share_py_txt():
	share_py_txt00 = '''
try:
	import mysql.connector
except Exception as err:
	print(err)
	print("\\n----ERORR----")
try:
	u = input("Enter User Name: ")
	paswd = input("Enter Passwd: ")
	mycon = mysql.connector.connect(host = "localhost", user = u, passwd = paswd)
except Exception as err:
	print(err)
	print("\\n----ERORR----")
	print("Enterd Username OR Passwd is Incorrect")
	exit()
cur = mycon.cursor()
cur.execute("show databases")
fetched = cur.fetchall()
for i in fetched:
	print(i)
try:
	db = input("Enter Database where you want to paste: ")
	mycon = mysql.connector.connect(host = "localhost", user = u, passwd = paswd, database = db)
	cur = mycon.cursor()
except Exception as err:
	print(err)
	print("\\n----ERORR----")
	print("Database",db,"Dosen't exist")
	exit()
share_query =("create table "+share_table_name+"(")
for f in fdata:
	f = list(f)
	if f[2] == 'NO':
		f[2] = "not null"
	else:
		f[2] ="null"
	if f[3] == "PRI":
		f[3] = "primary key"
	f.pop(4)
	type_edit = str(f[1])
	find_b = type_edit.find("b")
	t = type_edit[find_b+1:]
	t = t.replace("'","")
	f[1] = t
	f = str(tuple(f))
	f = f.replace("'","")
	f = f.replace(",","")
	f = f[1:-1]
	f = f.strip()
	share_query = share_query+f+", "
share_query = share_query.strip()
if share_query.endswith(","):
	share_query = share_query[:-1] + ")"
	cur.execute(share_query)
# ~ EXCUTE AND CREATE TABLE AND INSERT INTO THE TABLE
fields = []
for i in fdata:
	fields.append(i[0])
fields = str(tuple(fields))
fields = fields.replace("'","")
for columns in fields_data:
	insertation_query = "insert into "+share_table_name+fields+" values"+str(columns)
	cur.execute(insertation_query)
	mycon.commit()
print("____Sucessfull____")
conti = input("press enter to exit: ")
mycon.close()
'''
	return share_py_txt00




# ~ --------------------------------------------------------------------
import maskpass
import os
xx = os.popen("pip list")
xx = xx.read()
if "mysql-connector-python" not in xx:
	os.system("pip install mysql-connector-python")
if "maskpass" not in xx:
	os.system("pip install maskpass")
clean_screen()



import mysql.connector
# ~ mycon = mysql.connector.connect(host="localhost", user="root",passwd="root")
try:
	u = input("User: ")
	p = maskpass.askpass("Password: ",mask='*')
	mycon = mysql.connector.connect(host="localhost", user=u,passwd=p)
# ~ _____________________________________________________________________________
except Exception :
	end()
	print("\n~~~~EROOR~~~~\nUser name or Password is wrong")
	enter_2coninue()
	clean_screen()
	try:
		u = input("User: ")
		p = maskpass.askpass("Password: ",mask='*')
		mycon = mysql.connector.connect(host="localhost", user=u,passwd=p)
	except:
		exit()
	# ~ continue
# ~ _____________________________________________________________________________
except Exception:
	print("USERNAME OR PASSWD IS WRONG")
	print(enter_2coninue())
	exit()
cur = mycon.cursor()

pr = ('''\n   MENU
1. Create database
2. Delete database
3. Show databases
4. Open database''')

# ~ Program starting
while True:
	os.system("cls")
	cur.execute("show databases")
	fdata = cur.fetchall()
	print(table("Databases"))
	print(table(fdata))
	print(pr)
	try:
		ip = int(input(">>>"))
	except ValueError:
		print("\n~~~~EROOR~~~~\nplease Enter only above mentioned integers\n")
		print(enter_2coninue())
		os.system("cls")
		continue
	except IndentationError:
		print("\n~~~~EROOR~~~~\nplease Enter only above mentioned integers\n")
		print(enter_2coninue())
		os.system("cls")
		continue
	
	if ip == 1:
		try:
			ipc1 = input("Database Name: ")
			if ipc1 == "//":
				ipc1_back = input("Press Enter to go Back or Press any other key(for no): ")
				if ipc1_back == "":
					print("BACK")
					enter_2coninue()
					continue
				else:
					pass
			cur.execute("create database if not exists "+ ipc1)
			print(end())
			os.system("cls")
		except mysql.connector.errors.DatabaseError:
			print(enter_2coninue())
			os.system("cls")
			continue
	elif ip == 2:
		try:
			ipc2 = input("Delete database: ")
			if ipc2 == "//":
				back = input("Press Enter to go Back or Press any other key(for no): ")
				if back == "":
					print("BACK")
					enter_2coninue()
					continue
				else:
					pass
			cur.execute("drop database "+ipc2)
			print("Database ",ipc2,"successfully Deleted")
			print(enter_2coninue())
			print(end())
			os.system("cls")
		except mysql.connector.errors.DatabaseError:
			print("\n~~~~EROOR~~~~\nNo such database exist :(\n Please try again")
			continue
	elif ip == 3:
		cur.execute("show databases")
		fdata = cur.fetchall()
		print(table(fdata))
		# ~ for i in fdata:
			# ~ print(i)
		print(enter_2coninue())
		print(end())
		os.system('cls')
	elif ip == 4:
		try:
			ipc4 = input("Enter the name of database to Open: ")
			if ipc4 == "//":
				print("BACK")
				print(enter_2coninue())
				continue
			mycon = mysql.connector.connect(host="localhost", user=u,passwd=p,database = ipc4)
			database = ipc4
			cur = mycon.cursor()
			print("database opened \n")
			cur.execute("show tables")
		except mysql.connector.errors.ProgrammingError:
			print(DB(ipc4))
			enter_2coninue()
			os.system("cls")
			continue
		except Exception as err:
			print("\n---- Error ----\n")
			print(err)
			print(enter_2coninue())
			continue
		try:
			fdata = cur.fetchall()
			print(table(fdata))
		except :
			print("~~~~_No Tables Found_~~~~\n")
		finally:
			print(enter_2coninue())
			print(end())
		os.system("cls")
		
		while True:
			os.system("cls")
			cur.execute("select database()")
			onDB_tup = cur.fetchall()
			for DB in onDB_tup:
				ipc4 = DB[0]
			print(table("Tables in "+ str(ipc4)))
			print(execution("show tables"))
			print('''	Options
		1. Create Table
		2. Open table
		3. delete table
		4. insert into table
		5. Share Table
		6. Copy Table
		0. Exit''')
			try:
				ip1 = int(input(ipc4+">>"))
				if ip1>6:
					print("please Enter only above mentioned integers\n")
					print(enter_2coninue())
					os.system("cls")
			except ValueError:
				print("please Enter only above mentioned integers\n")
				continue
			www=""
			if ip1 ==0:
				break
			elif ip1 ==1:
				table_creation_str =""
				clmn_list = []
				cnt = 1
				# ~ table_name = input("Enter Table Name: ")
				duplicate = True
				# ~ duplicate = check_duplicate_in_tables(table_name)
				while duplicate == True:
					table_name = input("Enter Table Name: ")
					if table_name == "//":
						duplicate = False
						www ="back"
						print(enter_2coninue())
						continue
						
					duplicate = check_duplicate_in_tables(table_name)
					if duplicate == True:
						print("\n----Error----\n Duplicate entry \n Table already exist\n")
						continue

					
				while www=="":
					dupluicate = False
					column_name = input("Enter Column "+str(cnt)+" Name: ")
					if column_name == "//":
						www="back"
						print(enter_2coninue())
						continue
					column_type = input("Enter Column "+column_name+" Type(int/char/varchar/date) : ")
					if column_type == "//":
						www="back"
						print(enter_2coninue())
						continue
					# ~ ch_limit = input("Enter Character Limit:")
					ch_limit = conditional_input("Enter Character Limit:","int")
					if ch_limit == "//":
						www="back"
						print(enter_2coninue())
						continue
					if ch_limit=="" or ch_limit.isspace():
						ch_limit=""
					else:
						ch_limit = ("("+ch_limit+")")
					null_ = input("data should Null or Not Null Enter y for YES or n for NO): ")
					if null_ == "//":
						www="back"
						print(enter_2coninue())
						continue
					else:
						pass
					if null_ in "yY":
						null = "null"
					elif null_ in "nN":
						null = "not null"
					# ~ else:
						# ~ print("you have Enterd ",null_)
						# ~ print("Please Enter y for yes or n for no")
						# ~ null = input("data can be Null or not(y/n): ")
					key = input("Enter SPECIAL key OR press Enter to skip : ")
					if key == "//":
						www="back"
						print(enter_2coninue())
						continue
					if key !="":
						key = key +" key"
					other = input("Enter other key press OR Enter to skip : ")
					if other == "//":
						www="back"
						print(enter_2coninue())
						continue
					column1=(column_name+" "+column_type+ch_limit+" "+null+" "+key+" "+other)
					column1=column1.strip()
					for l in range (len(clmn_list)):
						if column_name == clmn_list[l]:
							print("\n----Error----\n Duplicate entry \n Field Name can;t be duplicate\n")
							dupluicate=True
						else:
							pass
					if dupluicate == True:
						continue
					clmn_list.append(column_name)
					
					
					table_creation_str = table_creation_str + column1 + ","
					cnt = cnt + 1
					www = input("Press Enter to add another column or press 2 to Create Table: ")
					if www == "//":
						www="back"
						print(enter_2coninue())
						continue
					
					if www!= "":
						table_creation_str=table_creation_str+")"
						if table_creation_str.endswith(",)"):
							table_creation_str = table_creation_str.replace(",)",")")
							
						create_table = ("create table "+table_name+"("+table_creation_str)
						try:
							cur.execute(create_table)
							print("Table Sucessfully Created")
						except Exception as err:
							print("\n~~~~EROOR~~~~\n")
							print(err)
							print(enter_2coninue)
						os.system("cls")

			elif ip1 == 2:
				ip_execute = input("Enter Table Name to Open: ")
				if ip_execute == "//":
					continue
				try:
					cur.execute("select * from "+ip_execute)
					fdata = cur.fetchall()
				except mysql.connector.errors.ProgrammingError:
					print("\nError: There is no Tabled",ip_execute,"\nplease try again: ")
					print(enter_2coninue())
					continue
				os.system("cls")
				TableName = ip_execute
				while True:
					os.system("cls")
					print(open_table(TableName))
					print('''	Options
		1. Manipulate Data
		2. Share Data in python file
		3. ADD New Field/Column
		0. Exit''')
					
					try:
						ip4_open_table = int(input(ipc4+"\\"+ip_execute+">"))
					except Exception as err:
						print("\n----Error----\n",err,ip_execute,"\nplease try again: ")
						print(enter_2coninue())
						continue
					if ip4_open_table >3 or ip4_open_table<0:
						print("\n----:( Error :(----\n PLEASE ENTER ONLY ABOVE MENTIONED OPTION\nplease try again :): ")
					if ip4_open_table == 1:
						cur.execute("select * from "+TableName)
						result = cur.fetchall()
						cur.execute("desc "+TableName)
						fda = cur.fetchall()
						tb_name_lst =[]
						for i in fda:
							tb_name_lst.append(i[0])
						tb_name_lst = tuple(tb_name_lst)
						result.insert(0,tb_name_lst)
						manupulation_dict = {}
						tb00 = result
						tb_num = 0
						for i in tb00:
							chr_num = 65
							for i1 in i:
								keys_dic = chr(chr_num) + str(tb_num)
								manupulation_dict[keys_dic] = i1
								chr_num = chr_num + 1
							tb_num = tb_num + 1
						# ~ --------------------------
						input00 = input("Enter Block no. ")
						if input00 == "//":
							print(enter_2coninue())
							os.system("cls")
							break
							continue
						input00 = input00.title()
						print(input00)
						try:
							print(manupulation_dict[input00])
						except KeyError:
							print("\n~~~~EROOR~~~~\n Index No.",input00,"dose'nt exist")
							continue
						# ~ DISTRIBUTING THE FIELD NAMES AND TABLE DATA
						if input00 in manupulation_dict.keys():
							where_list = []
							clmns_list =[]
							edit_field_name = (manupulation_dict[input00])
							if input00[1]=="0":
								cur.execute("desc "+TableName)
								fdta = cur.fetchall()
								for i in fdta:
									if edit_field_name in i[0]:
										field_type0 =str(i[1])
										field_type0 = field_type0.replace("'","")
										field_type0 = field_type0[1:]
								update_field = input("Change FieldName "+ str(edit_field_name) + " to : ")
								if update_field == "//":
									print(enter_2coninue())
									os.system("cls")
									break
									continue
									
								exe = "ALTER TABLE "+str(TableName)+" CHANGE "+edit_field_name+" "+update_field+" "+field_type0
								cur.execute(exe)
								mycon.commit()
							else:
								string00 = "" 
								update_field = input("Change data "+ str(edit_field_name)+ " to : ")
								if update_field == "//":
									print(enter_2coninue())
									os.system("cls")
									break
									continue
									
								for i in manupulation_dict.keys():
									if input00[:1] in i:
										edit_in_clmn =manupulation_dict[(input00[:1]+"0")]
										pass
									elif "0" in i:
										if len(i)<=2:
											clmns_list.append(manupulation_dict[i])
									elif input00[1:] in i:
										where_list.append(manupulation_dict[i])
								for i in range (len(clmns_list)):
									if(str(where_list[i])=="None"):
										where_list[i] = "NULL";
										string00 = string00 +" "+clmns_list[i]+" is "+ where_list[i] +" and "
									else:
										string00 = string00 +" "+clmns_list[i]+" = "+"'"+str(where_list[i])+"'"+" and "
								if string00.endswith(" and "):
									string00 = string00[:-5]
								exe1 = "UPDATE "+str(TableName)+" SET "+edit_in_clmn+"='"+update_field +"' WHERE"+ string00
								print(exe1)
								cur.execute(exe1)
								mycon.commit()
						else:
							print("\n~~~~EROOR~~~~\n Index No.",input00,"dose'nt exist")
				
# ~ ---------------------------------------------------------------------------------------------------------------

					elif ip4_open_table == 2:
						
						share_file = open("file1.py","w+")
						cur.execute("desc "+ip_execute)
						fdata = cur.fetchall()
						cur.execute("select * from "+ip_execute)
						fields_data = cur.fetchall()
						share_text = 'share_table_name = "'+ip_execute+'"\n'+"fdata = "+str(fdata)+"\nfields_data="+str(fields_data)+share_py_txt()
						share_file.write(share_text)
						share_file.close()
					
					elif ip4_open_table == 3:
						'''add_column_name = input("Enter the Field Name you want to add : ")
						add_coulmn_type = input("Enter Field Type(int/char/varchar) : ")
						add_coulmn_null = input("Enter Field Null or not Null : ")
						add_coulmn_key = input("Enter Field key or press ENTER to skip : ")
						'''
						#---------------------------------------------
						#---------------------------------------------
						#---------------------------------------------
						#---------------------------------------------
						#---------------------------------------------
						#---------------------------------------------
					
						add_column_name = input("Enter Column Name to add: ")
						if add_column_name == "//":
							www="back"
							print(enter_2coninue())
							continue
						add_column_type = input("Enter Column "+add_column_name+" Type(int/char/varchar/) : ")
						if add_column_type == "//":
								www="back"
								print(enter_2coninue())
								continue
						add_ch_limit = conditional_input("Enter Character Limit:","int")
						if add_ch_limit == "//":
							www="back"
							print(enter_2coninue())
							continue
						if add_ch_limit=="" or add_ch_limit.isspace():
							add_ch_limit=""
						else:
							add_ch_limit = ("("+add_ch_limit+")")
						add_null_ = input("data should Null or Not Null Enter y for YES or n for NO): ")
						if add_null_ == "//":
							www="back"
							print(enter_2coninue())
							continue
						else:
							pass
						if add_null_ in "yY":
							add_null = "null"
						elif add_null_ in "nN":
							add_null = "not null"

						add_key = input("Enter SPECIAL key OR press Enter to skip : ")
						if add_key == "//":
							www="back"
							print(enter_2coninue())
							continue
						if add_key !="":
							add_key = add_key +" key"
						add_other = input("Enter other key press OR Enter to skip : ")
						if add_other == "//":
							www="back"
							print(enter_2coninue())
							continue
						add_field=(add_column_name+" "+add_column_type+add_ch_limit+" "+add_null+" "+add_key+" "+add_other)
						add_column1=add_field.strip()
						
						# ~ ---------------------------------------------------
						execute0 = "ALTER TABLE "+ ip_execute +" ADD "+ add_column1 
						print(execute0)
						cur.execute(execute0)
						mycon.commit()
					elif ip4_open_table == 0:
						os.system("cls")
						break
						continue

			elif ip1 == 3:
				try:
					ip_delete = input("Enter Table Name to Delete: ")
					if ip_delete == "//":
						print(enter_2coninue())
						os.system("cls")
						continue
					cur.execute("drop table "+ip_delete)
					print("Table",ip_delete,"sucessfully deleted")
				except mysql.connector.errors.ProgrammingError:
					print("table not found\n Please try again")
					continue
				except Exception as err:
					print("\n~~~~EROOR~~~~\n")
					print(err)
					print(enter_2coninue)
					continue
			elif ip1 == 4:
				ins_table_name = input("Enter Table Name :")
				if ins_table_name == "//":
					print(enter_2coninue())
					continue
				
				try:
					cur.execute("desc "+ins_table_name,)
				except Exception as err:
					print("\n~~~~EROOR~~~~\n")
					print(err)
					print(enter_2coninue)
					continue
				fdata = cur.fetchall()
				# ~ print(table(fdata))
				
				continue_inserting ="" 
				while continue_inserting == "":
					enterd_data_dict={}
					print(execution("select * from "+ ins_table_name,ins_table_name))
					for i in fdata:
						field_name = i[0]
						# ~ type
						i2str = str(i[1])
						i2str_split = i2str.split("'")
						f_type0 = i2str_split[1]
						if "(" in f_type0:
							find_start = f_type0.find("(")
							field_type = f_type0[:find_start]
							find_end =f_type0.find(")")
							field_len = eval(f_type0[find_start+1:find_end])
						else:
							field_len = 10
							field_type = f_type0
						field_null = i[2]
						field_key = i[3]
						field_default = i[4]
						field_extra = i[5]
						
						while True:
							enter_column = input("Enter in "+field_name+" : ")
							if enter_column == "//":
								print(enter_2coninue())
								continue_inserting = "back"
								break
								
							if field_type == "int":
								try:
									eval_ec = eval(enter_column)
								except NameError or SyntaxError:
									print("\n----Value Error----\n Enter only Numbers\n")
									continue
								if type(eval_ec) == int or float:
									enter_column = eval(enter_column)
									pass
								else:
									print("\n----Value Error----\n Enter only Numbers\n")
									continue
							else:
								pass
							if field_null == "NO":
								if enter_column !=""or None:
									pass
								else:
									print("\n----Value Error----\n input can't be NULL\n")
									continue
							elif field_null == "YES":
								pass
							if field_len<(len(str(enter_column))):
								print("\n----Error: Out of range----\n Max range is",field_len,"\n")
								continue
							else:
								pass
							break
						if enter_column == "//":
							continue_inserting = "back"
							break
						else:
							enterd_data_dict[field_name] = enter_column
							keys_of_table = str(tuple(enterd_data_dict.keys()))
					if enter_column == "//":
							continue_inserting = "back"
							break
					else:
						insert_into_table = ("insert into "+ ins_table_name+ keys_of_table.replace("'","")
						+" values"+str(tuple(enterd_data_dict.values())))
						try:
							cur.execute(insert_into_table)
							mycon.commit()
							print("Inserted Sucessfully")
						except Exception as err:
							print(err)
							print(enter_2coninue)
							break
						continue_inserting = input("press enter to add another column or enter any key : ")
						if continue_inserting == "//":
							back = input("Press Enter to go Back or Press N(for no): ")
							if back == "":
								print("BACK")
								print(enter_2coninue())
								continue_inserting = "back"
								break
							else:
								pass

			elif ip1 == 5:
				exp_name = True
				export_table_file0 =export_table_file= "Table exported"
				one_more = 0
				while exp_name == True:
					try:
						f1 = open(export_table_file+".py","r")
						f1.close()
						print(export_table_file)
						one_more = one_more + 1
						export_table_file = export_table_file0 + str(one_more)
					except Exception as err:
						exp_name =  False
						
				ip_execute = input("Enter Table Name to export as python file: ")
				share_file = open(export_table_file+".py","w+") 
				if ip_execute == "//":
					back = input("Press Enter to go Back or Press other key(for no): ")
					if back == "":
						print("BACK")
						continue
					else:
						pass
				cur.execute("desc "+ip_execute)
				fdata = cur.fetchall()
				cur.execute("select * from "+ip_execute)
				fields_data = cur.fetchall()
				share_text = 'share_table_name = "'+ip_execute+'"\n'+"fdata = "+str(fdata)+"\nfields_data="+str(fields_data)+share_py_txt()
				share_file.write(share_text)
				share_file.close()

			elif ip1 == 6:
				copy_table = input("Enter Table Name to Copy: ")
				if copy_table == "//":
					back = input("Press Enter to go Back or Press other key(for no): ")
					if back == "":
						print("BACK")
						continue
					else:
						pass
				
				
				try:
					cur.execute("select * from "+copy_table)
					fdata = cur.fetchall()
				except mysql.connector.errors.ProgrammingError:
					print("\nError: There is no Tabled",copy_table,"\nplease try again: ")
					print(enter_2coninue())
					os.system("cls")
					continue
				db_selected = False
				cd = database+"."+copy_table
				while db_selected == False:
					print("AGAIN")
					try:
						print(execution("show databases"))
						copy_table_in_database = input("Enter Database to Paste: ")
						if copy_table_in_database == "//":
							print(enter_2coninue())
							db_selected = True
							# ~ break
							# ~ break
							continue
							continue
						
						
						try:
							cur.execute("use "+copy_table_in_database)
						except mysql.connector.errors.ProgrammingError:
							print("\nError: There is no Database Named",copy_table_in_database,"\nplease try again: ")
							print(enter_2coninue())
							os.system("cls")
							continue
						mycon = mysql.connector.connect(host="localhost", user=u,passwd=p,database = copy_table_in_database)
						cur = mycon.cursor()
						if check_duplicate_in_tables(copy_table) == True:
							print("\n----Error: DUPLICATE TABLE----")
							copy_table00 = input("Press Enter to Paste Table as "+"duplicate_"+copy_table+" or Enter a New Name: ")
							if copy_table_in_database == "//":
								print(enter_2coninue())
								break
								continue
							
							
							if copy_table00 == "":
								while (check_duplicate_in_tables(copy_table)) == True:
									copy_table = "duplicate_"+copy_table
							if copy_table00 != "":
								copy_table = copy_table00
						print("done")
						db_selected = True
					except mysql.connector.errors.ProgrammingError:
						db_selected = False
						print(DB(ipc4))
						continue
					except TypeError:
						print("\n----Error----\nPlease Try Again"+"\n")
					continue
				if copy_table_in_database == "//":
					pass
				else:
					copy_table_query = "create table "+copy_table+" As"+" ("+"select * from "+cd+")"
					cur.execute(copy_table_query)
					print("Copied Sucessfully")
					print(enter_2coninue())
					os.system("cls")
					database = copy_table_in_database

	else:
		print("\n~~~~EROOR~~~~\nplease Enter only above mentioned integers\n")
		print(enter_2coninue())
