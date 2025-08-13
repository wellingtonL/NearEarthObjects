NEAR EARTH OBJECTS README.md
Project: Explore Near Earth Objects Approaches
This is an Intermediate Python project requirement where all the course information is to write and develop a program for exploring close approaches of NEO’S Near Earth Objects. The Data is information gathered from NASA/Jet Propulsion Laboratories. 
The requirement is the python script to read data from (‘neos.csv’) has information of small bodies asteroids and comets in the solar system. CSV file and a (‘cad.json’) Jason file has information about NEO close approaches when the orbit body brings it close to earth. The data is made into Python Objects to construct classes and functions. And create filtering to query data, limiting the size of the result files and to write the result files into CSV and Jason files that are structured and readable information.

When task is complete you can run subcommands to inspect  and query the data. The dataset provides rows of field information:
•	Occurrence of date
•	Occurrence on or after a start date
•	Occurrence on or before end date
•	Distance to earth of at least to astronomical units
•	Relative Velocity of at least of Y kilometers per second
•	Object has a Diameter of at least as large or small as the Zkilometers
•	Labeled by NASA if or not the object is potentially hazardous 

Course Project Objectives:
•	Explore, understand and get familiar with the NASA DATASETS. To obtain understanding of the rows  of data. Each row represents a single NEO.
•	Create Python Objects to represent data. Learned how to construct instances of the classes created and write attributes from the dataset belonging to the objects.
•	Create and build a readable human representation of objects created. And create additional methods and objects or properties to be included. 
•	Plan how the objects will interact with other objects.
•	Python methods and function creation as Init methods, String formats, Datetime functions, None attribute, calendar date format are implemented.
•	Manual Testing is implemented at the interactive interpreter. And unit test is done to check functions and methods that are working. Bugs are encounter and gain debugging skills in stack traces, system errors. Check preconditions with ‘assert’ testing.

Near Earth Objects must have these attributes:
•	Designation The primary designation for this NearEarthObject.
•	name: The IAU name for this NearEarthObject.
•	diameter: The diameter, in kilometers, of this NearEarthObject.
•	hazardous: Whether or not this NearEarthObject is potentially hazardous.
•	approaches: A collection of this NearEarthObjects close approaches to Earth.

Close Approach Objects must have attributes (or retrievable  properties) for the following names:
•	time: The date and time, in UTC, at which the NEO passes closest to Earth.
•	distance: The nominal approach distance, in astronomical units, of the NEO to Earth at the closest point.
•	velocity: The velocity, in kilometers per second, of the NEO relative to Earth at the closest point.
•	neo: The NearEarthObject that is making a close approach to Earth.

Command Line Project Interface:
The project is run main.py at the command line to invoke the program code.
At a command line, you can run python3 main.py --help for an explanation of how to invoke the script.
usage: main.py [-h] [--neofile NEOFILE] [--cadfile CADFILE] {inspect,query,interactive} ...
Explore past and future close approaches of near-Earth objects.

positional arguments:
  {inspect,query,interactive}
optional arguments:
  -h, --help            show this help message and exit
  --neofile NEOFILE     Path to CSV file of near-Earth objects.
  --cadfile CADFILE     Path to JSON file of close approach data.

These are the three subcommands inspect, query, and interface. Below are each subcommands displayed.

Inspect command
The inspect subcommand is a single NEO prints details in a readable format. NEO  uses the –pdes option and the –name option. The –verbose flag  prints a human readable print-out .  The printout is of all known approaches to Earth made by the NearEarthObjects.
$ python3 main.py inspect

Query command 
This subcommand is more advance. It produces a collections of close approaches that match specific filters. Also displays a limited number of output or writs the structured results to a file.
The query command generates a collection of approaches that match specific filters and has a limited amount of row output and can be written to an output file as part of the query.
$ python3 main.py query

Interactive command
This command loads the database and starts a loop to repeatedly run inspect and query commands. This loop runs inspect and query without reloading data each time a command is run.

Samples of inspect and query output
C:\Users\lggoo\anaconda3\Udacity\IntermediatePython3Projects\NeoProject1\ProjectFiles> python3 main.py inspect --pdes 433
Welcome to the NEO close approach explorer!
433 is a near Earth object with a diameter of 16.840 and is not hazardous.
C:\Users\lggoo\anaconda3\Udacity\IntermediatePython3Projects\NeoProject1\ProjectFiles> python3 main.py inspect --name Halley  
Welcome to the NEO close approach explorer!
1P is a near Earth object with a diameter of 11.000 and is not hazardous.
 C:\Users\lggoo\anaconda3\Udacity\IntermediatePython3Projects\NeoProject1\ProjectFiles> python3 main.py inspect --verbose --name Eros
Welcome to the NEO close approach explorer!
433 is a near Earth object with a diameter of 16.840 and is not hazardous.
- A CloseApproach at 1900-12-27 01:30, '433' approaches Earth at a distance of 0.31 au and a velocity of 5.58 km/s
- A CloseApproach at 1907-11-05 03:31, '433' approaches Earth at a distance of 0.47 au and a velocity of 4.39 km/s
- A CloseApproach at 1917-04-20 21:19, '433' approaches Earth at a distance of 0.50 au and a velocity of 4.82 km/s
- A CloseApproach at 1924-03-05 22:13, '433' approaches Earth at a distance of 0.36 au and a velocity of 4.60 km/s
- A CloseApproach at 1931-01-30 04:07, '433' approaches Earth at a distance of 0.17 au and a velocity of 5.92 km/s
- A CloseApproach at 1938-01-13 22:04, '433' approaches Earth at a distance of 0.22 au and a velocity of 6.08 km/s
- A CloseApproach at 1944-11-27 01:41, '433' approaches Earth at a distance of 0.40 au and a velocity of 3.63 km/s
- A CloseApproach at 2025-11-30 02:18, '433' approaches Earth at a distance of 0.40 au and a velocity of 3.73 km/s
- A CloseApproach at 2042-04-06 19:02, '433' approaches Earth at a distance of 0.45 au and a velocity of 3.73 km/s
- A CloseApproach at 2049-02-12 05:38, '433' approaches Earth at a distance of 0.27 au and a velocity of 6.06 km/s
- A CloseApproach at 2056-01-24 11:03, '433' approaches Earth at a distance of 0.15 au and a velocity of 5.82 km/s
- A CloseApproach at 2062-12-31 08:25, '433' approaches Earth at a distance of 0.30 au and- A CloseApproach at 2025-11-30 02:18, '433' approaches Earth at a distance of 0.40 au and a velocity of 3.73 km/s
- A CloseApproach at 2042-04-06 19:02, '433' approaches Earth at a distance of 0.45 au and a velocity of 3.73 km/s
- A CloseApproach at 2049-02-12 05:38, '433' approaches Earth at a distance of 0.27 au and a velocity of 6.06 km/s
- A CloseApproach at 2056-01-24 11:03, '433' approaches Earth at a distance of 0.15 au and a velocity of 5.82 km/s
- A CloseApproach at 2062-12-31 08:25, '433' approaches Earth at a distance of 0.30 au and a velocity of 5.73 km/s
- A CloseApproach at 2069-11-08 21:29, '433' approaches Earth at a distance of 0.46 au and a velocity of 4.25 km/s
- A CloseApproach at 2086-03-11 22:55, '433' approaches Earth at a distance of 0.37 au and a velocity of 4.23 km/s
- A CloseApproach at 2093-01-31 15:47, '433' approaches Earth at a distance of 0.18 au and a velocity of 5.97 km/s
$ python3 main.py interactive

Project Files and folders
main.py
database.py
extract.py	
models.py
filters.py
write.py
helpers.py
test folder
workflows folder
README

Python3 Environment
Requires 3.6 plus. Run python3 -v in the command line.
Development and Testing files.
Clone the project to laptop or desktop. Go to main.py file and run test to check files are in correct form. Below is the command line information to test the files.

$ python3 -m unittest
This runs 73 tests and returns an OK acknowledg PS C:\Users\lggoo\anaconda3\Udacity\IntermediatePython3Projects\NeoProject1\ProjectFiles> python3 main.py 

Reports Generated:
inspect --pdes 433
Welcome to the NEO close approach explorer!
433 is a near Earth object with a diameter of 16.840 and is not hazardous.
(venv) PS C:\Users\lggoo\anaconda3\Udacity\IntermediatePython3Projects\NeoProject1\ProjectFiles> python3 main.py inspect --name Halley  
Welcome to the NEO close approach explorer!
1P is a near Earth object with a diameter of 11.000 and is not hazardous.
(venv) PS C:\Users\lggoo\anaconda3\Udacity\IntermediatePython3Projects\NeoProject1\ProjectFiles> python3 main.py inspect --verbose --name Eros
Welcome to the NEO close approach explorer!
433 is a near Earth object with a diameter of 16.840 and is not hazardous.
- A CloseApproach at 1900-12-27 01:30, '433' approaches Earth at a distance of 0.31 au and a velocity of 5.58 km/s
- A CloseApproach at 1907-11-05 03:31, '433' approaches Earth at a distance of 0.47 au and a velocity of 4.39 km/s
- A CloseApproach at 1917-04-20 21:19, '433' approaches Earth at a distance of 0.50 au and a velocity of 4.82 km/s
- A CloseApproach at 1924-03-05 22:13, '433' approaches Earth at a distance of 0.36 au and a velocity of 4.60 km/s
- A CloseApproach at 1931-01-30 04:07, '433' approaches Earth at a distance of 0.17 au and a velocity of 5.92 km/s
- A CloseApproach at 1938-01-13 22:04, '433' approaches Earth at a distance of 0.22 au and a velocity of 6.08 km/s
- A CloseApproach at 1944-11-27 01:41, '433' approaches Earth at a distance of 0.40 au and a velocity of 3.63 km/s
- A CloseApproach at 2025-11-30 02:18, '433' approaches Earth at a distance of 0.40 au and a velocity of 3.73 km/s
- A CloseApproach at 2042-04-06 19:02, '433' approaches Earth at a distance of 0.45 au and a velocity of 3.73 km/s
- A CloseApproach at 2049-02-12 05:38, '433' approaches Earth at a distance of 0.27 au and a velocity of 6.06 km/s
- A CloseApproach at 2056-01-24 11:03, '433' approaches Earth at a distance of 0.15 au and a velocity of 5.82 km/s
- A CloseApproach at 2062-12-31 08:25, '433' approaches Earth at a distance of 0.30 au and- A CloseApproach at 2025-11-30 02:18, '433' approaches Earth at a distance of 0.40 au and a velocity of 3.73 km/s
- A CloseApproach at 2042-04-06 19:02, '433' approaches Earth at a distance of 0.45 au and a velocity of 3.73 km/s
- A CloseApproach at 2049-02-12 05:38, '433' approaches Earth at a distance of 0.27 au and a velocity of 6.06 km/s
- A CloseApproach at 2056-01-24 11:03, '433' approaches Earth at a distance of 0.15 au and a velocity of 5.82 km/s
- A CloseApproach at 2062-12-31 08:25, '433' approaches Earth at a distance of 0.30 au and a velocity of 5.73 km/s
- A CloseApproach at 2069-11-08 21:29, '433' approaches Earth at a distance of 0.46 au and a velocity of 4.25 km/s
- A CloseApproach at 2086-03-11 22:55, '433' approaches Earth at a distance of 0.37 au and a velocity of 4.23 km/s
- A CloseApproach at 2093-01-31 15:47, '433' approaches Earth at a distance of 0.18 au and a velocity of 5.97 km/s



