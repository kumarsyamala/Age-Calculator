def age_cal():
  import os
  import sys,time,random
  from colorama import Fore

  import calendar
  import datetime as dt
  from IPython.display import display,HTML

  black='\033[30m'
  red='\033[31m'
  green='\033[32m'
  orange='\033[33m'
  blue='\033[34m'
  purple='\033[35m'
  cyan='\033[36m'
  lightgrey='\033[37m'
  darkgrey='\033[90m'
  lightred='\033[91m'
  lightgreen='\033[92m'
  yellow='\033[93m'
  lightblue='\033[94m'
  pink='\033[95m'
  lightcyan='\033[96m'
  red1="\033[0;31m"
  redb="\033[1;31m"
  green1="\033[0;32m"
  greenb="\033[1;32m"
  yellow1="\033[0;33m"
  yellowb="\033[1;33m"
  blue1="\033[0;34m"
  blueb="\033[1;34m"
  purple1="\033[0;35m"
  purpleb="\033[1;35m"
  lightblue1="\033[0;36m"
  lightblueb="\033[1;36m"
  all_col = [red,green,orange,cyan,lightgrey,lightred,lightgreen,yellow,lightcyan,red1,redb,green1,greenb,yellow1,yellowb,blue1,blueb,purple1,purpleb,lightblue1,lightblueb]
  ran = random.choice(all_col)
  os.system("clear")


  def sprint(str):
    for c in str + '\n':
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(4./90)

  sprint(ran+"-"*30)




  ##hello terance##
  from datetime import datetime
  now = datetime.now()
  current_year = now.year
  current_month = now.month
  current_day = now.day


  dob = input("Enter your date of birth in dd/mm/yyyy format:")


  list_date_of_birth = dob.split("/")
  birth_date = int(list_date_of_birth[0])
  birth_month = int(list_date_of_birth[1])
  birth_year = int(list_date_of_birth[2])


  name = input("Enter you name: ")
  gender = input("\nEnter you gender \"M\" for male \"F\" for female: ")


  print('\n')
  sprint("We are setting up thingz for you")

  list_for_male = ['m','M','male','Male']
  list_for_female = ['f','F','Female','female']


  if gender in list_for_female:
      print(ran,"\nMrs.", name ,"you are born in" ,birth_date, birth_month, birth_year )
  elif gender in list_for_male:
      print(ran,"\nMr." , name , "you are born in",birth_date, birth_month, birth_year)
  else:
      if gender not in list_for_male or list_for_female:
          print(ran, name , "You are born in" ,birth_date, birth_month, birth_year )



  sprint(ran+"-"*50)
  sprint(ran+"\nLet me calculate some more intresting things about you")
  sprint(ran+"\ncalculating days...")
  sprint(ran+"\ncalculating seconds...")
  sprint(ran+"\ncalculating minutes...")
  sprint(ran+"\ncalulating hours...")
  sprint(ran+"\ncalculating......")

  if birth_month != 2 or birth_date != 29:
      if current_month == 1 or current_month == 2 or current_month == 4 or current_month == 6 or current_month == 8 or current_month == 9 or current_month == 11:
          var_date = 31
      elif current_month == 3:
          if current_year % 4 == 0 and (current_year % 100 != 0 and current_year % 400 == 0):
              var_date = 29
          else:
              var_date = 28
      else:
          var_date = 30
      if birth_year <= current_year:
          def date():
              if current_day > birth_date:
                  abs_date = current_day-birth_date
              elif current_day == birth_date:
                  abs_date = 0
              else:
                  n_days = birth_date-current_day
                  abs_date = var_date-n_days
              return abs_date
          if current_month > birth_month:
              if current_day > birth_date:
                  actual_month = current_month-birth_month
              else:
                  actual_month = current_month-birth_month-1
              actual_year = current_year-birth_year
              date()
          elif current_month == birth_month:
              date()
              if date() == 0:
                  print('\n')
                  print ("Happy Birthday" ,"\U0001F973","\U0001F382")
            
                  actual_month = 0
                  actual_year = current_year-birth_year
              else:
                  if birth_date < current_day:
                      actual_month = 0
                      actual_year = current_year-birth_year
                  else:
                      actual_month = 11
                      actual_year = current_year-birth_year-1
          else:
              date()
              diff_date = birth_month-current_month
              if birth_date < current_day:
                  actual_month = 12-diff_date
                  actual_year = current_year-birth_year
              else:
                  actual_month = 11-diff_date
                  actual_year = current_year-birth_year-1

          
          print ("\nYou are", actual_year, "years", actual_month, "months and", date(), "days old.")

          print('\n')

          # create HTML Calendar month
          cal = calendar.HTMLCalendar()
          s= cal.formatmonth (birth_year,birth_month)

          # display calendar without highlighting today 
          #display(HTML(s))    

          # add cell's backgroundcolor, bold and underling html tags 
          # around today's date
          ss = s.replace('>%i<'%birth_date, ' bgcolor="#FFFFE0"><b><u>%i</u></b><'%birth_date)
          display(HTML(ss))
          
          print('\n')

          # create HTML Calendar month
          cal = calendar.HTMLCalendar()
          s= cal.formatmonth (current_year,current_month)

          # display calendar without highlighting today 
          #display(HTML(s))    

          # add cell's backgroundcolor, bold and underling html tags 
          # around today's date
          ss = s.replace('>%i<'%current_day, ' bgcolor="#FFFFE0"><b><u>%i</u></b><'%current_day)
          display(HTML(ss))

          

      else:
          print ("Invalid Birth year")
  else:
      print( "So you are a leap year child ,Sorry I can't calculate your age , may be 1/4th of your present age,","\N{rolling on the floor laughing}")

  print('\n')

  sprint(ran+"-"*50)

  print('\n')

  sprint(ran+"Have a good day")
