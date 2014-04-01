Data Mining a questionnaire
===========================
by Jens Dahl Mollerhoj

This project was made as a mandatory individual assignment for the 2013 Data Mining course at the IT-university.

The following is a 'Project report'. (I have to make one for my course, if you
want to keep your sanity, I would stop reading now.)

TODO:
Use cleaning and processing on kMeans and kNN.
Fix clean_int and clean_float to actually yield Nan
Normalize data in the two next methods
Put it all into folders: examples, lib etc.

Project report
==============
## Introduction, focus and learning goals
This is report documents a tiny data mining project in which I try to answer some basic questions based on the answers given in the questionnaire described below.
I have used this project to get a feeling for the basic concepts used in data mining. As this is the first python code I have ever written, I might not count as an exceptionally well coded project. After trying to be as object orientated as working in Ruby has made me used to, I ended up with a rather un-idiomatic solution. After quite a bit for refactoring (and after giving up on providing a decent amount of unit tests, I finally arrived with what I believe is at least readable python code. I have had a lot of focus on getting a understanding of the pandas library. The library is praised as a de facto standard for handling data in python, however, it has been a surprisingly difficult experience for me to grok the API. I feel like there is still at lot to be learned (especially in regards to the numpy library) in order to feel confident using python as a data mining / machine learning tool.

## The questions I try to answer
### What students have answered most alike, and how similar are their answers?
The results could be used to detect fraud. Also, it gives in insight into how similar 'minded' a small number of programmers can be.

Why is it interesting. What applications could it have for other types of data?
Apriori

### Is it possible to detect a students age based on their answers?
Since the dawn of time, the older generation have claimed to have a more mature than the youth. But in the world of programming, does age have anything to say?

### What types of students are taking this course? and what questions are causing a devision?
A quite loose question. But 

## The methods used
My general approach has been to focus a lot on the structure of the data. There is not a lot of data, so it is very important to throw as little away as possible. However, since the data is very dirty, most of it must be cleaned, and some is downright meaningless, and therefore has to be thrown away.

The small amount of data makes is possible to get a good overview, that yields insight into where it needs cleaning. This has proven to be extremely valuable. For a larger dataset, I would definitely use some random sampling to get a smaller chuck of data that I could use to guide my cleaning approach.

Since it has been so important to throw as little as possible away, I have chosen to preprocess the data with custom procedures before using the data mining techniques.

### Data Reduction: 
3 of the students was removed from the dataset, because their answers seemed to be fake, and seemed to be an attempt to be difficult.

The values of the attributes "SqRoot", "Georgios_middleName", "JulianHome" and "canteenFood" were too inconsistent to use.

The attribute "therbforttglag" simply didn't make any sense, thus is was also removed.

The random integers were not removed. Even though their values might seem useless, they says something about the psychology of the programmers.

### Data Cleaning:

The categorical data, (eg. the data of the attributes "OS", "progLangs", "EngSkill" and "FavAnimal".) was standardised as much as possible. Fore example, the values, "Win7", "WINDOWS", "Win" and "Windows" were all read as the same value.

The binary values, (eg. the data of the attributes "MoreMtns", "winter", "canteenFood", "FavColor", "neuralNetwork", "vectorMachine", "sql", "FavSQLServ" and "APriori") was also standardized.

The numerical values, (eg. the data of the attributes "age", "prog_skill", "uni_yrs", "OS", "progLangs", "EngSkill", "FavAnimal", "MoreMtns", "winter", "rand1-10", "rand0-1", "rand0-1_pt2" and "Planets")

was normalised using the following z-score formula:

  for_all_values(i - mean(i)) / standard_deviation(all).

### What two students have answered most alike?
The values of the numerical data was not normalised for for this question, Since outliers does not matter. The frequent pattern mining method Apriori was used.
The following values were found:

The output reads: 20 of 66 students has these values alike:

[frozenset(['sql: True', 'APriori: False', 'vectorMachine: False', 'FavAnimal: ELEPHANT']), frozenset(['sql: True', 'neuralNetwork: True', 'APriori: False', 'vectorMachine: False']), frozenset(['winter: True', 'sql: True', 'APriori: False', 'vectorMachine: False']), frozenset(['OS: windows', 'sql: True', 'APriori: False', 'vectorMachine: False']), frozenset(['MoreMtns: True', 'sql: True', 'APriori: False', 'vectorMachine: False'])]
As the results show, quite a lot of the students has given the same answers.

Conclusions?
A remarkable amount of students has answered the same in many of the questions. 

### Is it possible to detect a students age based on their answers?
The supervised learning method "k nearest neighbours" were used to answer this question.

As the results show...
### What types of students are taking this course?
Clustering method "k means" were used to answer this question.

As the results show...
### The implementation
The code (scripts) used to answer my questions can be found in the "examples" folder. If anyone would dare to use this tiny library, the scripts in this folder serves as good examples of use. The algorithms themselves are located in the "lib" folder. The somewhat abandoned set of unit tests are kept in the "spec" folder.

As mentioned, all my code is python. I heavily use the pandas library and also the numpy library. I chose python because I knew that it is one of the preferred languages for machine learning and data mining, and I knew that it would be an easy language to learn.

In order to run the example scripts, run the following commands
* python examples/kMeansTest.py
* python examples/???.py
* python examples/???.py

All examples loads data from the data/survey2014.csv file. The output is a print that describes the results

### The results I have reached
The conclusions that can be drawn from the above, formal results.
Two students seems to have answered almost the same to many of the problems. This could be a coincidence.
The age of a new student seems to be quite hard to detect.

### The problems I have had
(including the dirtiness of 
the dataset)

The pandas library has been very hard to grasp for some reason.

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE: www.wtfpl.net
