# redump_dat_copy

If, like me, you want to host a local copy of Redump’s .dat files, this program is for you.  

It downloads the .dat files hosted on the  http://redump.org/downloads page, following the systems.json file.  

After downloading each file, it calculates the SHA256 checksum and writes the result to a separate file.  

If you want to build your own systems.json file, you can use the extract_from_table.py script located in the tools folder. 


## How to run

* Copy the sample-params.json and edit the content
* If you want the private dat file, don't forget to specify your username / password
* run redump_dat_copy.py


## HAQ (Heavily anticipated questions)

**Q: Why did you rewrite sabretool fonctionnaly?**

**A:** Beceause I don't want runs exe program on my Linux server


Please note:
* I am not an experienced developer.
* I am still in the learning phase.
* I am doing this to improve my skills daily.

## TODO
