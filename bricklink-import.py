import argparse
import re
import sys
import os

# Import selenium
try:
    import selenium
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
except ImportError:
    sys.exit("Python module 'selenium' not found.\nPlease install using: pip install selenium")



def main():
    def verbose(s):
        if args.verbose:
            print(s)

    def login():
        # Open the website
        verbose("Accessing login page")
        driver.get('https://www.bricklink.com/v2/wanted/upload.page?utm_content=subnav')

        # Select the id box
        verbose("\tfilling username") 
        id_box = driver.find_element_by_name('frmUsername')
        # Send id information
        id_box.send_keys(username)

        # Select the id box
        verbose("\tfilling password") 
        pass_box = driver.find_element_by_name('frmPassword')
        # Send id information
        pass_box.send_keys(password)

        # Find login button
        verbose("\tlogin")
        login_button = driver.find_element_by_id('blbtnLogin')
        # Click login
        login_button.click()

        
    def adding_list(list_name, list_file):
        # Wait till the page is loaded
        driver.implicitly_wait(10) 
        select = Select(driver.find_element_by_id('wantedlist_select'))

        # If the new name exist, then select the list. Else create a new list
        verbose("Finding list \"" + list_name + "\"") 
        list_item = "-1"
        for opt in select.options:
            if re.match(list_name + " \([0-9]+\)$", opt.text):
                verbose("\t" + list_name + " already exists")
                list_item = opt.get_attribute("value")
                #select.select_by_visible_text(opt.text) # Create New Wanted List
                break

        select.select_by_value(list_item) # Create New Wanted List

        add_in_list = False
        if list_item=="-1":
            verbose("\tlist not found, creating one")
            name_box = driver.find_element_by_name('newWantedMore')
            name_box.send_keys(list_name)
        else:
            if args.force:
                verbose("\tadding to list " + list_name)
                select.select_by_value(list_item) # Create New Wanted List
                add_in_list = True
            else:
                answer = input("Do you really want to add items to the list " + list_name + " ? (y)es or (n)o")
                print(answer)
                if answer=="y" or answer=="yes":
                    select.select_by_value(list_item) # Create New Wanted List
                    add_in_list = True
                else:
                    print("do not add")
                
        if add_in_list:
            driver.implicitly_wait(3) 
            send_box = driver.find_element_by_name('file')
            send_box.send_keys(list_file)

            send_box = driver.find_element_by_id('button-add-all')
            send_box.click()
            
            driver.implicitly_wait(3) 
            
            button = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/div/div/div/div[2]/span/button")
            button.click()

            # Button Upload More Items
            button = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/div/div/div/div/a[1]/button")
            button.click()

        
    # Command arguments
    parser = argparse.ArgumentParser(description='Import a BrickLink wanted list.')
    parser.add_argument('--version', action='version', version='bricklink-import 0.0')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False, help='be verbose')
    parser.add_argument('-u', '--username', dest='username', help='username on BrickLink')
    parser.add_argument('-p', '--password', dest='password', help='password on BrickLink')
    parser.add_argument('-f', '--file', dest='file', help='BrickStock (.bsx) file containing the list to import.')
    parser.add_argument('-n', '--name', dest='name', help="Name of the list in which you want to import your items. If the list doesn't exist, it will be created..")
    parser.add_argument('-g', '--gui', dest='gui', action='store_true', default=False, help='Enable graphic user interface (gui)')
    parser.add_argument('-a', '--all', dest='all', help='Import all .bsx files in the given directory. The list names correspond to the file names (without extension).')
    parser.add_argument('--force', dest='force', action='store_true', default=False, help='Do not ask confirmation if the list already exists.')
    
            
    args = parser.parse_args()
    username = args.username
    password = args.password
    if username==None or password==None:
        sys.exit("Please enter username and password using the -u and -p options")

    # Using Firefox to access web
    verbose("Opening firefox")
    options = webdriver.FirefoxOptions()
    if not args.gui:
        verbose("\twith no gui")
        options.add_argument('-headless')
    driver = webdriver.Firefox(firefox_options=options)

    login()

    if args.file:
        list_file = args.file
        if re.search(".bsx$", list_file)==None:
            sys.exit("Please provide a .bsx file")
        list_name = args.name
        adding_list(list_name, list_file)
        exit()
    
    if args.all:
        verbose("Importing all files in " + args.all)
        for f in os.listdir(args.all):
            if re.search(".bsx$", f):
                list_name_ = re.search("(^[^/]+).bsx", f).groups()[0]
                print(list_name_)
                adding_list(list_name_, args.all + "/" + f)
        exit()
  

if __name__ == '__main__':
	main()
        
