from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.utils import timezone

import io
import json
from django.core.serializers.json import DjangoJSONEncoder

import dbarray
from .models import Controller, getDataModel
from .forms import NameForm
import datetime
import sys


# home page of the WebApp
#-------------------------
def index(request):
    request.session['link'] = 'TestLink'
    Controller_list = Controller.objects.all()
    template = loader.get_template('display/index.html')
    context = RequestContext(request, {
        'Controller_list': Controller_list,
    })
    return HttpResponse(template.render(context))


# page to show some details of an available controller
# on this page you can select any time to plot (not self updating)
#-----------------------------------------------------
def detail(request, controller_name):
    #check available controllers
    Controller_list = Controller.objects.all()

    # collect data for info table
    controller = get_object_or_404(Config, pk=config_controller)

    # initialize the datetime range (default is last day)
    time_start = datetime.datetime.now()-datetime.timedelta(hours=24)
    time_end = datetime.datetime.now()
    # this strings are needed for the input text field int he template
    time_start_str = time_start.strftime('%Y-%m-%d_%H:%M')
    time_end_str = time_end.strftime('%Y-%m-%d_%H:%M')

    DataNames = [x for x in controller.description]

    return render(request, 'display/detail.html',
            {'time_start_string': time_start_str,
                'time_end_string':time_end_str,
                'Controller_list': Controller_list,
                'controller': controller,
                'DataNames': DataNames})


#---------------------------------------------------------------
def getData(request, controller_name, desc, time_start_str, time_end_str):

    if request.method == 'GET':
        # get information about controller
        controller = get_object_or_404(Controller, pk=controller_name)
        data_i = list(controller.description).index(desc)

        #define DB table to look for the data
        DataClass = getDataModel(controller_name)

        time_start = datetime.datetime.strptime(time_start_str, '%Y-%m-%d_%H:%M')
        time_end = datetime.datetime.strptime(time_end_str, '%Y-%m-%d_%H:%M')

        # search for data using time range
        complete_list = DataClass.objects.filter(when__range=[time_start,time_end])
        # extract data points
        dates = map(lambda x : x.when.isoformat(sep=' '), complete_list)
        # extract time points
        datapoints = map(lambda x : x.data[data_i], complete_list)
        # extract status of datapoint
        status = map(lambda x : x.status[data_i], complete_list)

        # put data into list of the form [[data1, time1, status1], ...]
        data = list(zip(dates, datapoints, status))
        data.append([controller.warning_low[data_i], controller.warning_high[data_i], 0])
        data.append([controller.alarm_low[data_i], controller.alarm_high[data_i], 0])

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
    #print(PlotLinks)

    Controller_list = Controller.objects.all()
    return render(request, 'display/monitor.html', {'Controller_list': Controller_list, 'PlotLinks': PlotLinks })


# this function gets the required data for the monitor
#---------------------------------------------------------------
def scopedraw(request, controller_name, desc, timerange, plotnumber):

    if request.method == 'GET':

        # update PlotLinks in session
        PlotLinks = request.session['PlotLinks']
        PlotLinks[int(plotnumber)-1] = controller_name + '/' + desc
        request.session['PlotLinks'] = PlotLinks

        # get information about controller
        controller = get_object_or_404(Controller, pk=controller_name)
        #select data to plot
        data_i = list(controller.description).index(desc)

        #define DB table to look for the data
        DataClass = getDataModel(controller_name)
        # set the datetime range
        time_end = datetime.datetime.now()
        tr = {'1' : datetime.timedelta(hours=1),
              '2' : datetime.timedelta(hours=5),
              '3' : datetime.timedelta(hours=24),
              '4' : datetime.timedelta(weeks=1)}
        time_start = time_end - tr[timerange]

        # search for data using time range
        complete_list = DataClass.objects.filter(when__range=[time_start,time_end])
        # extract data points
        dates = map(lambda x : x.when.isoformat(sep=' '), complete_list)
        # extract time points
        datapoints = map(lambda x : x.data[data_i], complete_list)
        # extract status of datapoint
        status = map(lambda x : x.status[data_i], complete_list)

        # put data into list of the form [[data1, time1, status1], ...]
        data = list(zip(dates, datapoints, status))
        data.append([controller.warning_low[data_i], controller.warning_high[data_i], 0])
        data.append([controller.alarm_low[data_i], controller.alarm_high[data_i], 0])

    # Here the data is dumped as JSON to the frontend
    return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type='display/monitor/json')


