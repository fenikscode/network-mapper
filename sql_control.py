import mysql.connector as mc
from os import getenv

HOST=getenv('HOST')
USERNAME=getenv('USERNAME')
PASSWORD=getenv('PASSWORD')
DATABASE=getenv('DATABASE')

class SQLQuery():
    def __init__(self, _dataset_name):
        self.dataset_name = _dataset_name
    # Network Layout Setup
    def create_dataset(self):
        setup_template = """
            CREATE TABLE `{}` (
	           `MACAddress` varchar(17) PRIMARY KEY NOT NULL,
	           `IPAddress`	varchar(15) NOT NULL,
	           `Hostname` text(50),
	           `FriendlyName` text(50),
	           `OSName` text(25),
	           `IsUp` bool NOT NULL
            ) ENGINE=InnoDB""".format(self.dataset_name)
        return setup_template
    # Network Layout Adding Entries
    def entry_add_dataset(self, _MAC_ADDRESS, _IP_ADDRESS, _HOSTNAME=None, _FRIENDLY_NAME=None, _OS_NAME=None, _IS_UP=False):
        entry_template = f"""
            INSERT INTO `{self.dataset_name}` (
                `MACAddress`,
                `IPAddress`,
                `Hostname`,
                `FriendlyName`,
                `OSName`,
                `IsUp`
            ) VALUES (
                {_MAC_ADDRESS},
                {_IP_ADDRESS},
                {_HOSTNAME},
                {_FRIENDLY_NAME},
                {_OS_NAME},
                {_IS_UP}
            )
        """
        return entry_template

# Queries are send to MySQL in STACK - a list containing many commands
# Send one by one to server to save on time

def sql_connection_stack(query_stack :list):
    
    connection, cursor = sql_connection_start()
    
    # This loop goes through all task store in STACK
    # And executes them on server
    for task in query_stack:
        cursor.execute(task)
        connection.commit()
    connection.close()

# This function is creating remote connection to MySQL Server
def sql_connection_start():
    try:
        # Creating connection & cursor for queries
        connection = mc.connect(
            host=HOST,
            user=USERNAME,
            password=PASSWORD,
            database=DATABASE
        )
        cursor = connection.cursor()

    # Sending any error to terminal
    except mc.Error as e:
        print(e.msg)
        print(HOST)
        exit()

    else:
        return connection, cursor