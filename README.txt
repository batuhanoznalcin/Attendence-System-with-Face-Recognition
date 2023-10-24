The program is getting started from Main.py.

The screen that came from once the user opens there are two buttons. One of them is Login the other one is Register. According to the user purpose he/she clicks the button.

If the user clicks the Login button, the user is getting directed to the LoginPage.py. On that page, the user enters username and password information. 
    The information that the user entered, compared to the information that belongs to MySQL in the advisor database' Advisor table. If this information matches the user 
    provides an entrance. And the user directs to the DecidePage.py.

If the user clicks the Register button, the user is getting directed to the RegisterPage.py. On that page, there is an information line that says only authorized person(s) 
    can do this transaction. The authority only belongs to the Head of the Department. Then, asked from the user to enter username and password information. The information 
    that is entered by user, is compared to the advisor database' HeadOfDept table.  If this information matches the user provides an entrance. And the user directs to the 
    Registeration.py. On that page, there are 5 textfield that need to be filled. These are lastname, firstname, department, username, and password. information that entered 
    this page is getting inserted without allowing duplicate to the MySQL in the advisor database' Advisor table. After that the user is directed to the LoginPage.py.

On DecidePage.py page there is one button. Once this button is clicked the user is directed to the FaceRecognition.py which the attendence is taken.

On FacePageDataset.py I am taking 30 facial photos from students. These photos are creating my dataset. On this page I am asking user to enter id. In order the tkinter consider
    as 0 (default is 0) I determine it as string first and then with the help of isdigit() I made it integer.With the variable called id I store the photos in folder as dataset.
    Then, program starts training. Then the FaceRecognition page comes to screen.

In FaceRecognition.py I am doing emotion detection as well. The gathered information like name time day and emtotion is getting insterted to an .xlsx file named AttendenceList.
