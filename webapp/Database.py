import sqlite3

NOT_FOUND = -1

class POSITION():
    DISTANCE = 1
    TIME = 2
    MASS_TO_BURN = 3

class database_instance():
    '''
    This class in singleton because there is no need for more than 1 db instance
    '''
    db = 0 #init db
    cursor = 0 #init cursor

    def create_table(self):
        '''
        Create the database table if not exists
        Input: none
        Output: none
        '''
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS DATA (
                    total_cargo_mass INTEGER NOT NULL PRIMARY KEY,
                    minimal_taking_off_distance INTEGER,
                    time_for_take_off INTEGER,
                    mass_of_cargo_to_burn INTEGER
                );
            """)

    def insert_data(self ,total_cargo_mass, minimal_taking_off_distance, time_for_take_off, mass_of_cargo_to_burn):
        '''
        Insert data to the database
        Input: total_cargo_mass, minimal_taking_off_distance, time_for_take_off, mass_of_cargo_to_burn - the calculation results
        Output: none
        '''
        try:
            sql = 'INSERT INTO DATA (total_cargo_mass, minimal_taking_off_distance, time_for_take_off, mass_of_cargo_to_burn) values({}, {}, {}, {})'
            sql = sql.format(total_cargo_mass, minimal_taking_off_distance, time_for_take_off, mass_of_cargo_to_burn) #Add the variables to the string
            
            self.db.execute(sql)
            self.db.commit()


        except sqlite3.Error as e:
            print(e)

    def get_data_of_a_specific_cargo_mass(self, total_cargo_mass):
        '''
        Get the data that fits the cargo mass entered
        Input: total_cargo_mass - the ID of the database
        Output: A list containning the minimal_taking_off_distance, time_for_take_off and mass_of_cargo_to_burns that is saved at the database for the mass entered. -1 if not found
        '''
        try:
            minimal_taking_off_distance, time_for_take_off, mass_of_cargo_to_burns = NOT_FOUND,NOT_FOUND,NOT_FOUND
            rows = self.cursor.execute("SELECT * FROM DATA WHERE total_cargo_mass == " + str(total_cargo_mass)).fetchall()
            
            for data in rows: #Read the data to the variables
                minimal_taking_off_distance = data[POSITION.DISTANCE]
                time_for_take_off = data[POSITION.TIME]
                mass_of_cargo_to_burns = data[POSITION.MASS_TO_BURN]

            return [minimal_taking_off_distance, time_for_take_off, mass_of_cargo_to_burns]
        
        except(...):
            return [NOT_FOUND,NOT_FOUND,NOT_FOUND]


    def __init__(self):
        '''
        Iniating the database. Creating one if non exist
        Input: none
        Output: none
        '''
        self.db = sqlite3.connect("/db/aircraft_data_db.db") #Creates the database if it does not exists

        self.cursor = self.db.cursor()
    
        self.create_table() #Create table if not exists


       
    def __new__(cls):
        '''
        Creating only one instance of the class, singleton design pattern.
        Input: none
        Output: the class instance
        '''
        if not hasattr(cls, 'instance'):
            cls.instance = super(database_instance, cls).__new__(cls)
        return cls.instance
    
    def __del__(self):
        '''
        Deconstructor, close connection to the database
        Input: none
        Output: none
        '''
        self.db.commit()
        self.db.close()

