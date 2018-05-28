# Welcome to SAAVpedia 

## What's SAAVpedia
#### **SAAVpedia** is a platform for **identification, functional annotation, retrieval of single amino-acid variants from proteomic and genomic data**.
- **SAAVpedia provides** three user interfaces consisting of 

  - **Web User Interface (WUI)**
  - **Web Application Programming Interface (API)**
  - **Python package**.
  
- For Users with Python programming skills.
  - **This repository offers source codes of SAAVpedia Python package.**
- For Users without programming knowledge
  - Use WUI of SAAVpedia - <https://www.SAAVpedia.org>

## Getting Started

### [Unix/Linux]

#### Initial Python Setup for SAAVpedia.

Install SAAVpedia Python at the command prompt if you have not yet:   
To install SAAVpedia Python package,<br/> 
You **must have administrator privileges** or **write-access** on Python library folder.

##### Step One - Install SAAVpedia Python package via PyPI.
    $ pip install SAAVpedia   
    Collecting SAAVpedia
    Downloading https://files.pythonhosted.org/packages/...
    Installing collected packages: SAAVpedia
    Successfully installed SAAVpedia-x.x.x
   
##### Step Two - Upgrade SAAVpedia Python package via PyPI.     
    $ pip install --upgrade SAAVpedia

##### Download SAAVpedia DB in the local computer.
    $ python
    Python 2.7.12 (default, Dec  4 2017, 14:50:18)
    [GCC 5.4.0 20160609] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from SAAVpedia import SAAVpedia
    >>> SAAVpedia().init()
    ...
    Downloading SAAVpedia.sqlite.935.db - 91.23%
    Downloading SAAVpedia.sqlite.936.db - 91.33%
    Downloading SAAVpedia.sqlite.937.db - 91.42%
    ...
    Generating SAAVpedia DB... - 99.90%
    Generating SAAVpedia DB... - 100.00%
    Removing temporary files...
    SAAVpedia initilzation is completed.
    >>> quit()
    
##### Install SAAVpedia scripts in the current working directory.
    $ python
    Python 2.7.12 (default, Dec  4 2017, 14:50:18)
    [GCC 5.4.0 20160609] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from SAAVpedia import SAAVpedia
    >>> SAAVpedia().install()
    Copying SAAVinterpreter.py...
    Copying SNVretriever.py...
    Copying SAAVretriever-Online.py...
    Copying SAAVidentifier.py...
    Copying SAAVinterpreter-Online.py...
    Copying SAAVretriever.py...
    Copying SNVretriever-Online.py...
    Copying SAAVidentifier-Online.py...

    >>> quit()

##### The list of SAAVpedia command scripts
After installation of SAAVpedia in Python, You can see several SAAVpedia command scripts.

    $ ls -l
    -rw-r--r-- 1 user user 2333 May 10 09:10 SAAVidentifier-Online.py
    -rw-r--r-- 1 user user 2299 May 10 09:10 SAAVidentifier.py
    -rw-r--r-- 1 user user 6556 May 10 09:10 SAAVinterpreter-Online.py
    -rw-r--r-- 1 user user 6522 May 10 09:10 SAAVinterpreter.py
    -rw-r--r-- 1 user user 2328 May 10 09:10 SAAVretriever-Online.py
    -rw-r--r-- 1 user user 2294 May 10 09:10 SAAVretriever.py
    -rw-r--r-- 1 user user 2326 May 10 09:10 SNVretriever-Online.py
    -rw-r--r-- 1 user user 2292 May 10 09:10 SNVretriever.py

##### Example of Glioma data using SAAVidentifier
    $ python SAAVidentifier.py --input Glioma.input.txt 
    Reading the input file...
    Fetching output data...
    Estimated time for fetching data: 0.187811s
    Writing "SAAVidentifier-2018-05-10-09h-13m-52.362122s.scf" file...
    Total estimated time: 0.230s
    
    
##### Example of Glioma data using SAAVidentifier via online. 
    $ python SAAVidentifier-Online.py --input Glioma.input.txt 
    Reading the input file...
    Fetching output data...
    Estimated time for fetching data: 1.844199s
    Writing "SAAVidentifier-2018-05-10-09h-15m-17.405145s.scf" file...
    Total estimated time: 1.883s
    
