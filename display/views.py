from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.utils import timezone

import io
import json
from django.core.serializers.json import DjangoJSONEncoder

import dbarray
from .models import Config, DataPressurecontroller, getModel
from .forms import NameForm
import datetime
import sys


# home page of the WebApp
#-------------------------
def index(request):
    request.session['link'] = 'TestLink'
    Config_list = Config.objects.all()
    template = loader.get_template('display/index.html')
    context = RequestContext(request, {
        'Config_list': Config_list,
    })
    return HttpResponse(template.render(context))


# page to show some details of an available controller
# on this page you can select any time to plot (not self updating)
#-----------------------------------------------------
def detail(request, config_controller):
    #check available controllers
    Config_list = Config.objects.all()

    # collect data for info table
    config = get_object_or_404(Config, pk=config_controller)

    # initialize the datetime range (default is last day)
    time_start = datetime.datetime.now()+datetime.timedelta(seconds=7200)-datetime.timedelta(seconds=86400)
    time_end = datetime.datetime.now()+datetime.timedelta(seconds=7200)
    # this strings are needed for the input text field int he template
    time_start_string = time_start.strftime('%m/%d/%Y %I:%M %p')
    time_end_string = time_end.strftime('%m/%d/%Y %I:%M %p')

    DataNames = ["" for x in range(0, config.number_of_data)] #list containing the name of data in the data array
    for x in range(0, config.number_of_data):
        DataNames[x] = config.description[x]


    return render(request, 'display/detail.html', {'time_start_string': time_start_string, 'time_end_string':time_end_string, 'Config_list': Config_list,'config': config, 'DataNames': DataNames})


#---------------------------------------------------------------
def getCVSdata(request, controller, select, t1, t2, t3, t4, t5): 

    if request.method == 'GET':
        data = controller+'/'+select+'/'+t1+'/'+t2+'/'+t3+'/'+t4+'/'+t5
        
        # get information about controller
        config = get_object_or_404(Config, pk=controller)
        counter = 0
        #select data to plot
        for data in config.description:
            if data == select:
                data_select = counter
            counter = counter+1
            
    	#define DB table to look for the data
        db_table = 'data_' + controller
        DataClass = getModel(db_table.lower()) #use lower case of 'db_table'

        time_start_string = t1+'/'+t2+'/'+t3[:13]
        time_start = datetime.datetime.strptime(time_start_string, "%m/%d/%Y %I:%M %p")
        time_end_string = t3[16:]+'/'+t4+'/'+t5
        time_end = datetime.datetime.strptime(time_end_string, "%m/%d/%Y %I:%M %p")

	# search for data using time range
        complete_list = DataClass.objects.filter(datetime__range=[time_start,time_end])
	# extract data points
        datepoint = [datetime.datetime.strftime(DataClass.datetime,"%Y/%m/%d %H:%M:%S") for DataClass in complete_list] #format datetime
	# extract time points
        datapoint = [DataClass.data[data_select] for DataClass in complete_list]
        # extract status of datapoint
        status = [DataClass.status[data_select] for DataClass in complete_list]
	# put data into list of the form [[data1, time1], [data2, time2], ...]
        data = []
        for i in range(0, len(datepoint)): #len(datepoint)
            data.append([datepoint[i], datapoint[i] ])

    return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type='display/detail/json')


# call monitor page of WebApp: 
#contains 4 scopes to monitor any data available (self updating)
#---------------------------------------------------------------
def monitor(request):

    #if links for monitor plots do not exist => create them
    if 'PlotLinks' not in request.session:
        request.session['PlotLinks'] = ['','','','','','']

    #request.session['PlotLinks'] = ['','','','','','']
    PlotLinks = request.session['PlotLinks']
    print(PlotLinks)

    Config_list = Config.objects.all()
    return render(request, 'display/monitor.html', {'Config_list': Config_list, 'PlotLinks': PlotLinks })


# this function gets the required data for the monitor
#---------------------------------------------------------------
def scopedraw(request, controller, select, timerange, plotnumber): 

    if request.method == 'GET':

        # update PlotLinks in session
        PlotLinks = request.session['PlotLinks']
        PlotLinks[int(plotnumber)-1] = controller + '/' + select
        request.session['PlotLinks'] = PlotLinks

        

        # get information about controller
        config = get_object_or_404(Config, pk=controller)
        counter = 0
        #select data to plot
        for data in config.description:
            if data == select:
                data_select = counter
            counter = counter+1

	#define DB table to look for the data
        db_table = 'data_' + controller
        DataClass = getModel(db_table.lower()) #use lower case of 'db_table'
        # set the datetime range
	# last hour
        if timerange == '1':
            time_start = datetime.datetime.now()-datetime.timedelta(seconds=3600)
	# last 5 hours
        if timerange == '2':
            time_start = datetime.datetime.now()-datetime.timedelta(seconds=18000)
	# last day
        if timerange == '3':
            time_start = datetime.datetime.now()-datetime.timedelta(seconds=86400)
	# last week
        if timerange == '4':
            time_start = datetime.datetime.now()-datetime.timedelta(seconds=604800)
        time_end = datetime.datetime.now()

	# search for data using time range
        complete_list = DataClass.objects.filter(datetime__range=[time_start,time_end])
	# extract data points
        datepoint = [datetime.datetime.strftime(DataClass.datetime,"%Y/%m/%d %H:%M:%S") for DataClass in complete_list] #format datetime
	# extract time points
        datapoint = [DataClass.data[data_select] for DataClass in complete_list]
        # extract status of datapoint
        status = [DataClass.status[data_select] for DataClass in complete_list]
	# put data into list of the form [[data1, time1], [data2, time2], ...]
        data = []
        print(len(datepoint))
        for i in range(0, len(datepoint)): #len(datepoint)
            data.append([datepoint[i], datapoint[i], status[i] ])
            #print(datepoint[i])
        data.append([config.warning_low[data_select], config.warning_high[data_select], 0])

        

    # Here the data is dumped as JSON to the frontend
    return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type='display/monitor/json')


