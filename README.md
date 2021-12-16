# Time Series Prediction for Individual Household Power
Dateset: https://archive.ics.uci.edu/ml/datasets/individual+household+electric+power+consumption

The data was collected with a one-minute sampling rate over a period between Dec 2006
and Nov 2010 (47 months) were measured. Six independent variables (electrical quantities and sub-metering values) a numerical dependent variable Global active power with 2,075,259 observations are available. Our goal is to predict the Global active power into the future.

Here, missing values are dropped for simplicity. Furthermore, we find that not all observations are ordered by the date time. Therefore we analyze the data with explicit time stamp as an index. In the preprocessing step, we perform a bucket-average of the raw data to reduce the noise from the one-minute sampling rate. For simplicity, we only focus on the last 18000 rows of raw dataset (the most recent data in Nov 2010).

### A list of python files:
+ *Gpower_Arima_Main.py* :  The **executable** python program of a univariate ARIMA model.
+ myArima.py : implements a class with some callable methods used for the ARIMA model.
+ *Gpower_Xgb_Main.py* : The **executable** python program of a tree based model (xgboost).
+ myXgb.py : implements some functions used for the xgboost model.
+ *lstm_Main.py* : The **executable** python program of a LSTM model.
+ lstm.py : implements a class of a time series model using an LSTMCell. The credit should go to https://github.com/hzy46/TensorFlow-Time-Series-Examples/blob/master/train_lstm.py
+ util.py : implements various functions for data preprocessing.
+ Exploratory_analysis.py : exploratory analysis and plots of data.
```diff
+ Environment : Python 3.6, TensorFlow1.4.
```
### Here, I used 3 different approaches to model the pattern of power consumption.
- **Univariate time series ARIMA**.(30-min average was applied on the data to reduce noise.)
![onestep](https://user-images.githubusercontent.com/25689659/34470019-001ea4e0-eef7-11e7-822a-5a5132e8ca75.png)
![dynamic](https://user-images.githubusercontent.com/25689659/34470018-0011600a-eef7-11e7-89df-79372c49a791.png)
![forecast](https://user-images.githubusercontent.com/25689659/34470017-0004e848-eef7-11e7-9148-abfb62f95dcc.png)
- **Regression tree-based xgboost**.(5-min average was performed.) 
![xgbManual](https://user-images.githubusercontent.com/25689659/34470022-00463b90-eef7-11e7-8a3c-d80df291f7d6.png)
- **Recurrent neural network univariate LSTM (long short-term memoery) model**. (15-min average was performed to reduce the noise.)
![predict_result](https://user-images.githubusercontent.com/25689659/34470791-a5047402-ef07-11e7-9111-ff1da558b6e1.png)

### Possible approaches to do in the future work:
#### (i) Dynamic Regression Time Series Model
Given the strong correlations between Sub metering 1, Sub metering 2 and Sub metering 3 and our target variable, 
these variables could be included into the dynamic regression model or regression time series model.

#### (ii) Dynamic Xgboost Model
Include the timestep-shifted Global active power columns as features. The target variable will be current Global active power. 
Recent history of Global active power up to this time stamp (say, from 100 timesteps before) should be included
as extra features.

#### (iii) Multivariate LSTM
Include the features per timestamp Sub metering 1, Sub metering 2 and Sub metering 3, date, time and our target variable into the RNNCell for the multivariate time-series LSTM model.
![multivariate](https://user-images.githubusercontent.com/25689659/35536009-86ac3612-0513-11e8-9ccd-4311dff198ee.png)


# Classification of Seismic Events Using Unsupervised Machine Learning
## Capstone Project, Master of Applied Data Science
### University of Michigan

In this project we apply unsupervised machine learning techniques to build a pipeline for automatically extracting and classifying seismic events from continuous seismograms.  Events are automatically identified using the [PhaseNet](https://arxiv.org/abs/1803.03211) phase-picking tool, and separated (e.g. classified) using both traditional machine learning and deep learning based clustering techniques.  In both cases, we validate our modeling choices on a labeled dataset before applying them to the unlabeled PhaseNet events.

This repository contains all the necessary materials to reproduce our machine learning analyses, except for the data files which can be downloaded from [Google Drive](https://drive.google.com/drive/folders/1-Eex84NC7S8D0qj-rliZ34Xw5-PKQuaS?usp=sharing).  All project code is contained in three Jupyter notebooks.

### Data Set
The data set available on Google Drive contains the following files and subfolders.
* Labeled EQ and Blasts
  * blasts.list.  The onset times of mining blasts in our labeled dataset.
  * inducedEQ.list.  The onset times of fracking-induced earthquakes in our labeled dataset.
  * Numpy files containing downloaded waveforms, event onset times (Unix timestamps), and STFT spectrograms computed from waveforms.  If missing or deleted, these files are created by the data preparation notebook using the two .list files.
* PhaseNet Picks
  * Four .tar.gz files containing the PhaseNet picks for the years 2013, 2014, 2015, and 2016.  These archives must be extracted before recreating the numpy files in the directory.
  * Numpy files containing downloaded waveforms, event onset times (Unix timestamps), and STFT spectrograms computed from waveforms.  If missing or deleted, these files are created by the data preparation notebook using the contents of the .tar.gz archives.
  * Numpy files containing some intermediate results from the DEC notebook.

*All of these files may be safely deleted and recreated except for the .list files and .tar.gz archives, which are the "starting point" of the project.*

### Jupyter Notebooks
1. `Capstone_Data_Preparation_(Final).ipynb`.  This notebook prepares the waveforms and spectrograms described above.  It's not necessary to run this notebook if nothing has been deleted from the downloaded data files.
2. `Capstone_Traditional_(Final).ipynb`.  Contains the traditional machine learning analyses.
3. `Capstone_DEC_(Final).ipynb`.  Contains the deep learning analyses.

*The traditional machine learning and deep learning notebooks are standalone and may be run in any order, assuming all data is present.*

Minimal setup should be required to run the notebooks in your environment.  First, point the ROOT_PATH variable found in each notebook to the data folder downloaded from Google Drive.  Second, unless you plan to upload the notebooks to Google Colab, remove the drive mounting cell.  Everything else should work out of the box.  All notebooks were developed using the Google Colab Pro environment, so a GPU is recommended.  Note that even with a GPU, the MNIST section of the DEC notebook can take about an hour to run on its own.

### Authors
Annette Han (hananh@umich.edu) \
Dongdong Yao (dongdony@umich.edu) \
Yihe Huang (yiheh@umich.edu)

