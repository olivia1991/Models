# -*- encoding:utf-8 -*-

import re
import csv
import json
import time
import fileinput
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict


def analysis(filename):
	'''
		Analysis
		TBD: change any date to 'NA' if this date is larger than the first_trip_date.
	'''
	X, y = [], []; feature_set = {}; data_set = {}

	def get_category_feature(row, fieldname):
		field = row[fieldname] or 'NA'; feature_set[fieldname] = feature_set.get(fieldname,[])
		if not field in feature_set[fieldname]: feature_set[fieldname].append(field)
		return feature_set[fieldname].index(field)

	def get_time_year_feature(row, fieldname, thisyear=2016, defaultvalue=(0,-10**4)):
		get_feature = lambda t: (t, thisyear-t)
		return get_feature(int(row[fieldname])) if row[fieldname].isdigit() else defaultvalue

	get_time = lambda s: None if not re.match(u'/'.join([ur'[0-9]{,2}']*3),s) else time.strptime(s,'%m/%d/%y')

	def get_time_date_feature(row, fieldname, defaultvalue=(-10**4,-10**4)):
		get_feature = lambda t: (t.tm_yday, t.tm_wday)
		return get_feature(get_time(row[fieldname])) if get_time(row[fieldname]) else defaultvalue

	def get_time_date_delta_feature(row, fieldname1, fieldname2, defaultvalue=10**4):
		time1, time2 = map(lambda fieldname:get_time(row[fieldname]), (fieldname1,fieldname2))
		return time1.tm_yday-time2.tm_yday if time1 and time2 else defaultvalue

	with open(filename,'rU') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			city_name, signup_os, signup_channel, vehicle_model, vehicle_make = \
				[get_category_feature(row,fieldname) for fieldname in ('city_name','signup_os','signup_channel','vehicle_model','vehicle_make')]
			((vehicle_year, vehicle_year_delta),) = \
				[get_time_year_feature(row,fieldname) for fieldname in ('vehicle_year',)]
			((signup_date_yd, signup_date_wd), (bgc_date_yd, bgc_date_wd), (vehicle_added_date_yd, vehicle_added_date_wd),) = \
				[get_time_date_feature(row,fieldname) for fieldname in ('signup_date','bgc_date','vehicle_added_date')]
			signup_date_to_bgc_date, bgc_date_to_vehicle_added_date, signup_date_to_vehicle_added_date = \
				[get_time_date_delta_feature(row, t1, t2) for t1, t2 in [('bgc_date','signup_date'),('vehicle_added_date','bgc_date'),('vehicle_added_date','signup_date')]]
			label = bool(get_time(row['first_completed_date']))

			X.append([city_name, signup_os, signup_channel, vehicle_model, vehicle_make, vehicle_year, vehicle_year_delta, \
					  signup_date_yd, signup_date_wd, bgc_date_yd, bgc_date_wd, vehicle_added_date_yd, vehicle_added_date_wd, \
					  signup_date_to_bgc_date, bgc_date_to_vehicle_added_date, signup_date_to_vehicle_added_date])
			y.append(label)
	
	return np.array(X), np.array(y)


def prediction(filename, classifier='DecisionTree', get_feature_importance=False):
	'''
		Prediction
	'''
	from sklearn import svm
	from sklearn.tree import DecisionTreeClassifier
	from sklearn.ensemble import AdaBoostClassifier
	from sklearn.ensemble import RandomForestClassifier
	from sklearn.ensemble import GradientBoostingClassifier
	from sklearn.linear_model import SGDClassifier
	from sklearn.linear_model import LogisticRegression
	from sklearn.model_selection import KFold
	from sklearn.metrics import f1_score, confusion_matrix

	if classifier == 'SVM_rbf':
		clf = svm.SVC(kernel='rbf')
	elif classifier == 'SVM_linear':
		clf = svm.SVC(kernel='linear')
	elif classifier == 'DecisionTree':
		clf = DecisionTreeClassifier()
	elif classifier == 'AdaBoost':
		clf = AdaBoostClassifier()
	elif classifier == 'RandomForest':
		clf = RandomForestClassifier()
	elif classifier == 'GradientBoosting':
		clf = GradientBoostingClassifier()
	elif classifier == 'SGDClassifier_L1':
		clf = SGDClassifier(loss="hinge", penalty="l1")
	elif classifier == 'SGDClassifier_L2':
		clf = SGDClassifier(loss="hinge", penalty="l2")
	elif classifier == 'LogisticRegression_L1':
		clf = LogisticRegression(penalty="l1")
	elif classifier == 'LogisticRegression_L2':
		clf = LogisticRegression(penalty="l2")
	else:
		raise Exception('Classifer not supported.')

	X, y = analysis(filename)
	if get_feature_importance:
		clf.fit(X,y)
		print list(clf.feature_importances_)
	else:
		kf = KFold(n_splits=4); yp = []
		for train, test in kf.split(X):
			clf.fit(X[train],y[train])
			yp.extend(clf.predict(X[test]))
		print classifier, f1_score(y,yp)
		print classifier, confusion_matrix(y,yp)


if __name__ == '__main__':
	# prediction('../data/ds_challenge_v2_1_data.csv', classifier='SVM_rbf')
	# prediction('../data/ds_challenge_v2_1_data.csv', classifier='SVM_linear')
	# prediction('../data/ds_challenge_v2_1_data.csv', classifier='DecisionTree')
	# prediction('../data/ds_challenge_v2_1_data.csv', classifier='AdaBoost')
	# prediction('../data/ds_challenge_v2_1_data.csv', classifier='RandomForest')
	# prediction('../data/ds_challenge_v2_1_data.csv', classifier='GradientBoosting')
	# prediction('../data/ds_challenge_v2_1_data.csv', classifier='SGDClassifier_L1')
	# prediction('../data/ds_challenge_v2_1_data.csv', classifier='SGDClassifier_L2')
	# prediction('../data/ds_challenge_v2_1_data.csv', classifier='LogisticRegression_L1')
	# prediction('../data/ds_challenge_v2_1_data.csv', classifier='LogisticRegression_L2')

	prediction('../data/ds_challenge_v2_1_data.csv', classifier='GradientBoosting', get_feature_importance=True)

