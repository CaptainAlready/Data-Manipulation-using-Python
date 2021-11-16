# Data-Manipulationon-using-Python

This project is an optional project for the CEID-course **Principles of Programming Languages and Compilers**.

* <h2 style ="font-size: 0.5em"> getData.py</h2>
This script is responsible for :
* collecting four compressed files from the Eurostat databe 
* unzipping the compressed files to access the .csv files

* <h2 style ="font-size: 0.5em"> MainProgram.py</h2>
MainProgram.py is responsible for :
* Handling the information contained in the .csv files using the pandas framework.
* Creating plots that monitor the information and it's changes through a timespan of four years(selected by the user)
* Saving the desired information(selected by the user) to .csv files and uploading it to a local MySQL database
