#Python for evveryone exercise 5.1
#Set starting variables
# start(int) set to 1 to keep while loop running
start = 1
#count(int) total count of numbers entered, goes up by 1 each time number is entered
count = 0
#total(int) sum of all numbers entered
total = 0
#usernumber is the user input, set to none to start the loop
usernumber = None

while start >= 0:
    usernumber = (input("Enter a number"))
    #if user enters 'done' as the input breaks the lopps
    if usernumber == "done":
        break
    else:
        #tries to convert input into a float, if successful adds 1 to count of number and add numbers to total sum
        try:
            enterednumber = float(usernumber)
            print(enterednumber)
            count = count + 1
            total = total + enterednumber
        #if input cannot be converted to float, prints error message
        except:
            print('Please enter a numeric value')
#once loop is broken by inputting done, prints out total of all numbers, the count, and the average numbers entered
print("Total is ", total, "Count of numbers entered  is", count, "Average of numbers entered is ", (total/count))