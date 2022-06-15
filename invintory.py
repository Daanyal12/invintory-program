

'''tabulate function allows the data to be displayed in a user friendly format'''
from tabulate import tabulate

'''shoe class is created with all the attributes related to a shoe business'''
class Shoe():
    '''all the attributes related to shoes is created'''
    '''once initialised the attributes is declared using self so that each one can be called individualy'''
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
'''shoes list is created to append all the objects to'''
shoes = []
'''function read data is created so that it can fetch all the data from the file and minipulate it later on'''
def read_data(shoes):
    '''trys to open the file'''
    try:
        file = open("inventory.txt", "r")
    #if file does not exist display file does not exist
    except FileNotFoundError:
        print("File does not exist.")
    #finally open the text file read all the data inside loop through the data and split it by the comma
    finally:
        file = open("inventory.txt", "r")
        lines = file.readlines()

        for line in lines:

            temp = line.split(",")
            #append that data to the shoes list
            if "Country" not in temp:
                shoes.append(Shoe(temp[0], temp[1], temp[2], temp[3], temp[4]))
        #run the loop for the length of the shoe list
        for i in range(len(shoes)):
            #print everything from the list in this order
            print(f'''
Country: {shoes[i].country}
code:    {shoes[i].code}
product: {shoes[i].product}
cost:    {shoes[i].cost}
quantity:{shoes[i].quantity}''')
        file.close()

#call the function
read_data(shoes)

#this function allows the user to search for the shoe codes
def searchForCode(shoes):
    print("Product codes:")
    '''display all the products and their codes so that the user can see what shoe they are looking for'''
    for i in range(len(shoes)):
        print(f'''{shoes[i].product} : {shoes[i].code} ...''')  # Complete
    '''user inputs a code'''
    codes = input("Enter the code to search for: ")
    '''loops through the list and looks for the product associated with that specific code'''
    for j in range(len(shoes)):
        if codes in shoes[j].code:
            print(shoes[j].product)

searchForCode(shoes)

'''this function finds the lowest quantity of shoes available and allows the user to restock it to their desired amount'''
def findLowest(shoes):
    '''list for the quantity'''
    quantities = []
    '''appends all the quantities to the list'''
    for i in range(len(shoes)):
        quantities.append(shoes[i].quantity)
    '''converts the quantities in the list to integers so that you can call math functions on them'''
    for i in range(len(quantities)):
        quantities[i] = int(quantities[i])
    '''gets the lowest quantity in the list'''
    lowest = min(quantities)
    print(lowest)
    '''displays the product and the quantity amount to the user so that they can see what product the are restocking'''
    for a in range(len(shoes)):
        if str(lowest) == shoes[a].quantity.strip():
            print(shoes[a].product)
            print(shoes[a].quantity)
            #prompts the user howmuch they would like to restock
            restock = input("How much of the item would you like to restock? ")
            #changes the associated quantity amount to the restock value
            shoes[a].quantity = restock
            #display the updated quantity
            print(shoes[a].product)
            print(shoes[a].quantity)

findLowest(shoes)

'''this function finds the highest amount of products and allows you to set a sale amount'''
def findHighest(shoes):
    highList = []
    '''does the same as the previous function and appends all the quantities to a list'''
    for i in range(len(shoes)):
        highList.append(shoes[i].quantity)
    '''converts every instance to a integer'''
    for i in range(len(highList)):
        highList[i] = int(highList[i])
    '''gets the highest value in the list'''
    highest = max(highList)
    print()
    print(highest)
    '''loops through the length of the list and displays the product with the highest quantity'''
    for a in range(len(shoes)):
        if str(highest) == shoes[a].quantity.strip():
            print(shoes[a].product)
            print(shoes[a].quantity)
            #prompt user to input if they would like to mark the item as sale
            YN = input("would you like to mark this as sale? Y/N: ")
            #if they select yes they will be prompted to input a new discount price
            if YN == "Y":
                discount = input("what is the new discount price: ")
                shoes[a].cost = discount
                #show updated product and cost
                print(shoes[a].product)
                print(shoes[a].cost)
            else:
                pass
findHighest(shoes)

'''this function works out the total value per item by multiplying the cost by the quantity'''
def valuePerItem(shoes):
    '''open the text file with the data in it'''
    file = open("inventory.txt", "r+")
    lines = file.readlines()
    '''list to put data in two D form'''
    empty = []
    '''opens it again for append purpose will be explained later'''
    file2 = open('inventory.txt', 'a+')
    '''appends all the data to the empty list so that you can easily add the Value item to it'''
    for i in lines:
        #comma = i.split(",")
        empty.append(i)
    print(empty)
    '''removes the heading from the list'''
    empty.pop(0)
    print(empty)
    print()

    newList = []
    '''open invintory with a write function'''
    file3 = open("inventory.txt", "w")
    '''clear old data in text file with write function and add new data being the headings'''
    file2.write("country, code, product, cost, quantity, value \n")
    '''close file'''
    file3.close()
    '''run loop through the shoes list'''
    '''multiplys the quantity by the cost to get the value per item'''
    for i in range(len(shoes)):
        value1 = int(shoes[i].cost)
        value2 = int(shoes[i].quantity)
        value3 = value1 * value2

        '''this was to see what data got aappended and in what form'''
        data = (f"{shoes[i].country} {shoes[i].code} {shoes[i].product} {shoes[i].cost} {shoes[i].quantity.strip()} {value3}")
        newList.append(data)
        #print(newList)
        '''once form was correct that data is appended to the file under each specific heading'''
        file2.write(f"{shoes[i].country}, {shoes[i].code}, {shoes[i].product}, {shoes[i].cost}, {shoes[i].quantity.strip()}, {value3}\n")

        '''close the files'''
        file.close()
    file2.close()

valuePerItem(shoes)

'''this functions puts the data in table form so that the user can easily see what they are reading'''
def TabData():
    '''opens the file with read only'''
    file = open("inventory.txt", "r")
    '''gets each line in the file'''
    lines = file.readlines()
    '''adds the data to a list so that it can be in 2D form as tabulate needs to use a 2D list'''
    twoD = []
    '''loop appends the data with a comma so that it can be splitted by comma in the table'''
    for line in lines:
        stripped = line.strip()
        line_list = stripped.split(",")
        twoD.append(line_list)
    file.close()
    '''loops through the list and prints each line'''
    for i in twoD:
        print(i)
    '''prints the list using tabulate function which puts it in the easy to read function'''
    print(tabulate(twoD, headers='firstrow', tablefmt='fancy_grid'))
TabData()