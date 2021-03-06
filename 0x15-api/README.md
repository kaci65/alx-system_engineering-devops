## **0x15-api**
One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures using Python.

### **Resorces**

    Friends don’t let friends program in shell script<https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script>
    What is an API<https://www.webopedia.com/definitions/api/>
    What is a REST API<https://www.sitepoint.com/rest-api/>
    What are microservices<https://smartbear.com/solutions/microservices/>
    PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry<https://www.python.org/dev/peps/pep-0008/>

### **Learning Outcomes**

    What Bash scripting should not be used for
    What is an API
    What is a REST API
    What are microservices
    What is the CSV format
    What is the JSON format
    Pythonic Package and module name style
    Pythonic Class name style
    Pythonic Variable name style
    Pythonic Function name style
    Pythonic Constant name style
    Significance of CapWords or CamelCase in Python

### **Tasks**
### **0-gather_data_from_an_API.py**
Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

Requirements:

    You must use urllib or requests module
    The script must accept an integer as a parameter, which is the employee ID
    The script must display on the standard output the employee TODO list progress in this exact format:
        First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
            EMPLOYEE_NAME: name of the employee
            NUMBER_OF_DONE_TASKS: number of completed tasks
            TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
        Second and N next lines display the title of completed tasks: Tab TASK_TITLE (with 1 tabulation + 1 space before)

### **1-export_to_CSV.py**
Using what you did in the task #0, extend your Python script to export data in the CSV format.

Requirements:

    Records all tasks that are owned by this employee
    Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv

### **2-export_to_JSON.py**
Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

    Records all tasks that are owned by this employee
    Format must be: { "USER_ID": [ {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, ... ]}
    File name must be: USER_ID.json

### **3-dictionary_of_list_of_dictionaries.py**
Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

    Records all tasks from all employees
    Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
    File name must be: todo_all_employees.json
