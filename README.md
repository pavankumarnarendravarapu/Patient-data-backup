<p align="right">
By-: N.Pavan Kumar
</p>

# Patient data backup

### Brief explaination-:
> Our Web Application main agenda is to carrying the patients data, if they are already admitted in our hospital or not. The entire patient data is stored like diseases, patient information and payment slips. We give treatment based on his health condition. We check previous health checkup details, by these we finalised his health  condition.
 
### Install Libraries
 - pip install Flask 
 - pip install SQLalchemy
 - pip install requests
 - pip install psycopg2
 
### Softwares for item-catalog
 - `python3` - It is a general-purpose interpreted, interactive, object-oriented, and high-level programming language.
 - `Git-Bash` - Git is a distributed version-control system for tracking changes in source code.
 - `Virtual-Box` - Oracle VM VirtualBox is a free and open-source hosted hypervisor.
 - `Vagrant` - It is an open-source softwarw product for building and maintaining portable virtual software development environmeants.
 - `DB browser` - Unlike client–server database management systems, the SQLite engine has no standalone processes with which the application program communicates. 
 - `Any Editor` - Like (Sublime text, Notepad, Notepad++, Visual Studio) I'm using Sublime text.

### Download Links

 | Softwares | Links |
 | ------------ | ----- |
 | Python3 | [https://www.python.org/downloads/] |
 | Git-Bash | [https://git-scm.com/downloads] |
 | Virtual-Box | [https://www.virtualbox.org/wiki/Downloads] |
 | Vagrant | [https://www.vagrantup.com/downloads.html] |
 | DB browser | [https://sqlitebrowser.org/dl/] |
 | Sublime text | [https://www.sublimetext.com/3] |

### Requirements for item-catalog
 - `python3` - It is a general-purpose interpreted, interactive, object-oriented, and high-level programming language.
 - `HTML` - Hypertext Markup Language is the standard markup language for creating web pages and web applications. (we save files with `.html`).
 - `CSS` - Cascading Style Sheets (it is used for styling the web pages).
 - `BOOTSTRAP` - It contains HTML and CSS-based design templates for typography, forms, buttons, navigation and other interface components, as well as optional JavaScript extensions.(It is FRONT-END-FRAMEWORK)
 - `JavaScript(JS)` - is a lightweight, interpreted or JIT compiled programming language with first-class functions. Most well-known as the scripting language for Web pages, many non-browser environments also use it, such as node.js and Apache CouchDB.
 - `Flask` - Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries (except for some basics standard libraries such as bottom.
 - `SQLalchemy` -  SQLAlchemy's philosophy is that relational databases behave less like object collections as the scale gets larger and performance starts being a concern, while object collections behave less like tables and rows as more abstraction is designed into them.

### Python files-:
 - I have one main file - `flaskblog.py` 
 - One database file - `hospital_database.py`
 - One hospital information file - `hospital_info.py` 

### How to run python files
 - pyhon flaskblog.py
 - python hospital_database.py
 - python hospital_info.py

## How to run Patient data backup

> * First place the all files in `vagrant` folrder
> * Click on right button.
> * Open `gitbash` here.

###### Launch the vagrant. 

```sh
vagrant up
```
###### Run the vagrant.

```sh
vagrant ssh
```
###### Change the directory into vagrant folder.

```sh
cd /vagrant
```

###### Check the files.

```sh
ll or ls
```
###### Write your folder name.

```sh
cd folder name
```

###### Check the files.

```sh
ll or ls
```

###### Run python main file.

```sh
python flaskblog.py
```
