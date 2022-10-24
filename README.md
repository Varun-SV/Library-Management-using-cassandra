## Ever Stuck on a library desk to know what books are present???
```
  _    _               _        ____
 | |  | |             ( )      / __ \            
 | |__| | ___ _ __ ___|/ ___  | |  | |_   _ _ __ 
 |  __  |/ _ \ '__/ _ \ / __| | |  | | | | | '__|
 | |  | |  __/ | |  __/ \__ \ | |__| | |_| | |   
 |_|__|_|\___|_|  \___|_|___/  \____/ \__,_|_|   
  / ____|     | |     | | (_)                    
 | (___   ___ | |_   _| |_ _  ___  _ __          
  \___ \ / _ \| | | | | __| |/ _ \| '_ \         
  ____) | (_) | | |_| | |_| | (_) | | | |        
 |_____/ \___/|_|\__,_|\__|_|\___/|_| |_|        

```
| **Most Common Answer is to ask the librarian!!! Right???**
```
                ._.
  ____   ____   | |
 /    \ /  _ \  | |
|   |  (  <_> )  \|
|___|  /\____/   __
     \/          \/
```
# *Why ask librarian when you can get information about the books by yourself...*
This project uses cassandra as the database provider and then uses it to manage database.<br>

# How to run this project?
1. Run the following command in terminal in the same folder ...
    >`pip install -r /requirements.txt`
2. Go through the following link to install cassandra ...
    >Cassandra Installation for [Windows](https://www.google.com/search?q=cassandra+installation+in+windows&oq=cassandra+install&aqs=chrome.0.0i512j69i57j0i512l8.4198j0j7&sourceid=chrome&ie=UTF-8),[mac](https://www.google.com/search?q=cassandra+installation+in+mac&sxsrf=ALiCzsYsY_cZ09qttdbKOgiuBBFmsqKe_g%3A1666639713332&ei=YedWY__1E_es3LUP-6al-AM&ved=0ahUKEwi_qtPgzPn6AhV3FrcAHXtTCT8Q4dUDCA8&uact=5&oq=cassandra+installation+in+mac&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEBYQHjIFCAAQhgMyBQgAEIYDMgUIABCGAzoKCAAQRxDWBBCwAzoNCAAQ5AIQ1gQQsAMYAUoECE0YAUoECEEYAEoECEYYAVC3BVilCGDdC2gCcAF4AIABmAGIAbgDkgEDMC4zmAEAoAEByAENwAEB2gEGCAEQARgJ&sclient=gws-wiz) and [linux](https://www.google.com/search?q=cassandra+installation+in+linux&sxsrf=ALiCzsb_H5YqpCJLhPwbVbIHlMuxiIzsYw%3A1666639779609&ei=o-dWY_HZJKehz7sPyK6yuAM&ved=0ahUKEwixt6CAzfn6AhWn0HMBHUiXDDcQ4dUDCA8&uact=5&oq=cassandra+installation+in+linux&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIFCAAQhgMyBQgAEIYDOgoIABBHENYEELADOg0IABDkAhDWBBCwAxgBSgQITRgBSgQIQRgASgQIRhgBUNUEWKQMYLoOaAJwAXgAgAGOAYgBuAWSAQMwLjWYAQCgAQHIAQ3AAQHaAQYIARABGAk&sclient=gws-wiz)
3. Run the program by first setting up the virtual environment by using the following command in your command prompt...
    >`python3 -m venv lms` 
    1.  This will create a virtual environment with name ***lms*** inside wherever your cmd is pointed to....
    2. If you want it to specific then open cmd in your required directory and then run the above code...
    3. Then write the following code...<br>
        >`pip install -r requirements.txt`
4. Now Start the cassandra server if not started by typing the following command in your cmd opened in cassandra's bin folder...
    >`cassandra`
5. Now run this python program by writing the following program...
    >`python Library_Management_merge_sort.py`

# AND 
```
d888888b  .d8b.  d8888b.  .d8b.       db      db    db  .d88b.  db    db d8888b.                                              
`~~88~~' d8' `8b 88  `8D d8' `8b      88      `8b  d8' .8P  Y8. 88    88 88  `8D                                              
   88    88ooo88 88   88 88ooo88      YP       `8bd8'  88    88 88    88 88oobY'                                              
   88    88~~~88 88   88 88~~~88                 88    88    88 88    88 88`8b                                                
   88    88   88 88  .8D 88   88      db         88    `8b  d8' 88b  d88 88 `88.                                              
   YP    YP   YP Y8888D' YP   YP      YP         YP     `Y88P'  ~Y8888P' 88   YD                                              
                                                                                                                              
                                                                                                                              
d8888b. d8888b.  .d88b.     d88b d88888b  .o88b. d888888b      d888888b .d8888.      d8888b. d88888b  .d8b.  d8888b. db    db 
88  `8D 88  `8D .8P  Y8.    `8P' 88'     d8P  Y8 `~~88~~'        `88'   88'  YP      88  `8D 88'     d8' `8b 88  `8D `8b  d8' 
88oodD' 88oobY' 88    88     88  88ooooo 8P         88            88    `8bo.        88oobY' 88ooooo 88ooo88 88   88  `8bd8'  
88~~~   88`8b   88    88     88  88~~~~~ 8b         88            88      `Y8b.      88`8b   88~~~~~ 88~~~88 88   88    88    
88      88 `88. `8b  d8' db. 88  88.     Y8b  d8    88           .88.   db   8D      88 `88. 88.     88   88 88  .8D    88    
88      88   YD  `Y88P'  Y8888P  Y88888P  `Y88P'    YP         Y888888P `8888Y'      88   YD Y88888P YP   YP Y8888D'    YP    

```
