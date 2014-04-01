Data Mining a questionnaire
===========================
by Jens Dahl Mollerhoj

This project was made as a mandatory individual assignment for the 2013 Data Mining course at the IT-university.

The following is a 'Project report'. (I have to make one for my course, if you
want to keep your sanity, I would stop reading now.)

Project report
==============
## Introduction, focus and learning goals
This is report documents a tiny data mining project in which I try to answer some basic questions based on the answers given in the questionnaire described below.
I have used this project to get a feeling for the basic concepts used in data mining. As this is the first python code I have ever written, I might not count as an exceptionally well coded project. After trying to be as object orientated as working in Ruby has made me used to, I ended up with a rather un-idiomatic solution. After quite a bit for refactoring (and after giving up on providing a decent amount of unit tests, I finally arrived with what I believe is at least readable python code. I have had a lot of focus on getting a understanding of the pandas library. The library is praised as a de facto standard for handling data in python, however, it has been a surprisingly difficult experience for me to grok the API. I feel like there is still at lot to be learned (especially in regards to the numpy library) in order to feel confident using python as a data mining / machine learning tool.

## The questions I try to answer
### Is it possible to detect fraud by looking at frequent patterns?
It is always interesting to detect fraud. Also, it gives in insight into how similar 'minded' a small number of programmers can be.

### Is it possible to detect weather or not a student is bored with winter based on their answers?
Since the dawn of time, the older generation have claimed to have a more mature than the youth. But in the world of programming, does age have anything to say?

### What types of students are taking this course?
A quite loose question. I will to use the data to detect certain types of students.

## The methods used
My general approach has been to focus a lot on the structure of the data. There is not a lot of data, so it is very important to throw as little away as possible. However, since the data is very dirty, most of it must be cleaned, and some is downright meaningless, and therefore has to be thrown away.

The small amount of data makes is possible to get a good overview, that yields insight into where it needs cleaning. This has proven to be extremely valuable. For a larger dataset, I would definitely use some random sampling to get a smaller chuck of data that I could use to guide my cleaning approach.

Since it has been so important to throw as little as possible away, I have chosen to preprocess the data with custom procedures before using the data mining techniques.

### Data Reduction: 
3 of the students was removed from the dataset, because their answers seemed to be fake, and seemed to be an attempt to be difficult.

The values of the attributes "SqRoot", "Georgios_middleName", "JulianHome" and "canteenFood" were too inconsistent to use.

The attribute "therbforttglag" simply didn't make any sense, thus is was also removed.

The random integers were not removed. Even though their values might seem useless, they say something about the psychology of the programmers.

### Data Cleaning:

The categorical data, (eg. the data of the attributes "OS", "progLangs", "EngSkill" and "FavAnimal".) was standardised as much as possible. Fore example, the values, "Win7", "WINDOWS", "Win" and "Windows" were all read as the same value.

The binary values, (eg. the data of the attributes "MoreMtns", "winter", "canteenFood", "FavColor", "neuralNetwork", "vectorMachine", "sql", "FavSQLServ" and "APriori") was also standardized.

The numerical values, (eg. the data of the attributes "age", "prog_skill", "uni_yrs", "OS", "progLangs", "EngSkill", "FavAnimal", "MoreMtns", "winter", "rand1-10", "rand0-1", "rand0-1_pt2" and "Planets")

was normalised using the following z-score formula:

  for_all_values(i - mean(i)) / standard_deviation(all).

### Is it possible to detect fraud by looking at frequent patterns?
The frequent pattern mining method Apriori was used. The values of the numerical data was not normalised for for this question, since outliers aren't a problem for Apriori. 

Looking at the output (can be seen by running python Apriori_Test.py), one can see that there at 4 pairs of students that share 9 answers. Since the values are categorial, they are quite likely to be the same. Noone of the testruns reveals any patterns that surgest fraud. It is however, quite interesting to see how many of the answers are the same. On the question of favorite animal, the answers given are almost exclusively "elephant" or "zebra".

5 of 56 students has answered the same to all these questions:
'winter: True', 'FavAnimal: ELEPHANT', 'FavSQLServ: mysql', 'sql: True', 'neuralNetwork: True', 'APriori: False', 'vectorMachine: False'

### Is it possible to detect weather or not a student is bored with winter based on their answers?
The supervised learning method "k nearest neighbours" were used to answer this question.

by sampling random from the data, 50 of the tuples were used of training and 6 tuples were used for testing. After 10 runs, the results ranged from 66.7% to 100% percent accuracy.

As this might be due to overfitting, I ran the algoritm with 36 training tuples and 30 test tuples. The accuracy was not affected. This indicates (strange as it may sound) that there is actually some kind of relationship between the answers of the students and whether or not they are bored with winter.

### What types of students are taking this course?
I tried using the clustering method "k means" to answer this question. After trying to split the students into 2,3,4,5,6,7 and 8 clusters based on their answers, I have found no meaningful way to devide the students based on all the data.
If one does clustering on 2 features, such as age and programmingskill,university years or english skills, the data reveals one cluster, but only one:

https://github.com/mollerhoj/Data-Mining-a-questionnaire/blob/master/images/engSkill.png)
https://github.com/mollerhoj/Data-Mining-a-questionnaire/blob/master/images/progSkill.png)
https://github.com/mollerhoj/Data-Mining-a-questionnaire/blob/master/images/uni_yrs.png)

### The implementation
The code (scripts) used to answer my questions can be found in the file appended with the '_Test' ending. If anyone would dare to use this tiny library, the scripts in these files as good examples of use. The algorithms themselves are in files called the name of the algorithm. The somewhat abandoned set of unit tests are kept in files appended with the "spec" ending.

As mentioned, all my code is python. I heavily use the pandas library and also the numpy library. I chose python because I knew that it is one of the preferred languages for machine learning and data mining, and I knew that it would be an easy language to learn.

In order to run the example scripts, run the following commands

* python kMeans_Test.py
* python kNN_Test.py
* python Apriori_Test.py

All examples loads data from the data/survey2014.csv file. The output is a print that describes the results

### The problems I have had
The dataset was very small, and quite dirty. A lot of the data had to be removed because of meaningless questions and fake answers. Of the remaining data, none of the features have obvious relations. Since many of the features are based very subjective there is not a lot of obvious patterns. It is very interesting to see how questions such as faviorte animal leads to a lot of similar answers.

### License
DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE: www.wtfpl.net
