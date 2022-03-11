# Classeek


## Project Overview
In this project, we create a pilot recommender system that reminds [The University of Michigan LSA Computer Science](https://cse.engin.umich.edu/academics/undergraduate/computer-science-lsa/) undergraduate students of the courses they should take to meet the college-specific requirements and connect students with courses they would not have otherwise selected. We provide a survey to a student user at the beginning of each section of the system, which asks the student about their course schedule, personal and academic interests, and aspirations. We then use this information to:

+ Remind the students of the course to take next based on their previous and pending completion, and the CS degree requirements
+ Recommend elective courses to students that are similar to the student’s input courses and meet the degree requirements
+ Recommend elective courses or Michigan Online courses to students that match the student’s interests
+ Recommend courses to students based on the similarity of the student’s schedule and other students

## Overall Flow
This flowchart presents the overall steps of our project including the data used and algorithms utilized for each recommender system

![Flowchart Final](https://user-images.githubusercontent.com/76750938/146664485-8da2270d-7b4e-4eee-91e5-430a67598cdd.jpg)


## Data Used
The majority of our data were supplied by [Office of the Registrar](https://ro.umich.edu) and [Center for Academic Innovation](https://ai.umich.edu) with one portion of the data used was scraped from the [LSA Course Guide](https://www.lsa.umich.edu/cg/)

![tables](https://user-images.githubusercontent.com/76750938/146664540-545997fb-f5e5-4f70-9e0d-d50fbe69352b.jpg)

The folder contains comprehensive data files used for the project can be found [here](https://drive.google.com/drive/folders/1rtkShHZcbzqS4RqxT83VuSgF9zS1xSVb?usp=sharing) (need UMID to access)

## Folder Explanation
The following flowchart explains the significances of the folders included in this repository

![folder flow readme](https://user-images.githubusercontent.com/76750938/146603856-11abc460-4586-4719-aa63-23d42c8ccc54.jpg)


### Exploration Folder Details
+ *collab_filtering_exploration.ipynb* : Model selection and evaluation for collaborative recommender system. Exploration of memory-based and Matrix based (SVD and NMF) approaches. 
+ *collab_filtering_final.ipynb* : Final version of the memory-based model for collaborative recommender system. 
+ *content_based_exploration.ipynb* : Model selection and evaluation for course-based recommender system. Exploration of count vectorization with cosine similarity and tf-idf vectorization with sigmoid kernel. 
+ *deep_learning_content_based_exploration.ipynb* : Exploration of deep learning approach for course-based and survey answer-based recommender system and the final version for course-based and survey answer-based recommender system.

## Access to Project Files in Exploration Folder
The `Exploration` Folder contains our recommender systems' most comprehensive and final results. We recommend exploring this folder for efficiency. Of course, you are free to view draft files in other folders as well.
To navigate this folder, follow these steps for an effortless experience:

+ Clone the project GitHub repository:
```
git clone https://github.com/annettehan/classeek.git
```
+ Create and activate a virtual environment:
```
virtualenv env --no-site-packages
source env/bin/activate
```
+ Navigate to the `Exploration` directory:
```
cd Exploration
````
+ Download our data folder [here](https://drive.google.com/drive/folders/1rtkShHZcbzqS4RqxT83VuSgF9zS1xSVb?usp=sharing) (need UMID to access)
+ Ensure this data folder is `Exploration/assets/` and all data files are in this folder
+ Still in `Exploration` directory, install required dependencies:
```
pip3 install -r requirements.txt
```
+ Congratulation! You should be able to view and run our .ipynb and .py files now!

## Deployment

The recommender systems were deployed to a pilot webapp. The webapp is developed using [Flask](https://flask.palletsprojects.com/en/2.0.x/) backend API and [ReactJS](https://reactjs.org) frontend. The development files of the webapp are contained in the `Deploy` folder. Since the final webapp is forthcoming, the `Deploy` folder is currently hidden. 

## Authors
**Annette Han**: hananh@umich.edu \
**Beilei He**: beileihe@umich.edu \
**Yeseul Kim**: yeseulk@umich.edu
