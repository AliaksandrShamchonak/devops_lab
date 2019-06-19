#!/usr/bin/env bash

#Task 1: 
#Install pyenv using instructions from the lecture. In case of any problems use official documentation from pyenv github(https://github.com/yyuu/pyenv).

 sudo yum install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel libffi-devel findutils
 curl https://pyenv.run | bash
 echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> .bashrc
 echo 'eval "$(pyenv init -)"' >> .bashrc
 echo 'eval "$(pyenv virtualenv-init -)"' >> .bashrc
 curl https://pyenv.run | bash
 pyenv install 3.6.8


#Task 2:
#Write a script which Install python interpreters using pyenv:​ ­ 
#Python 2.7 ­
#Python 3.7 ­
#Create 2 virtualenv environments (1st for python2, 2nd for python3)

 pyenv install 2.7.16
 pyenv install 3.7.3

 pyenv virtualenv 2.7.16 python2716
 pyenv virtualenv 3.7.3 python373


#Task 3:
#Create a pull request. 


