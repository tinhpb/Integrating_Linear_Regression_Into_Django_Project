from django.shortcuts import render
from .models import Houses, Train
from .form import DemoForm, ContactForm
from .fusioncharts import FusionCharts
from collections import OrderedDict
from .linear_regression import main

### Home View
def home_page(request):
    count = Houses.objects.all().count()
    min = Houses.objects.all().order_by('askprice')[0]
    max = Houses.objects.all().order_by('-askprice')[0]

    chartObj = FusionCharts('logmsline','ex1','1100','400','chart-1','json',
        """{
            "chart": {
                "caption": "The relationship between House Prices and Year Build",
                "subcaption": "Source: United Nations Population Division",
                "xaxisname": "Year Build",
                "yaxisname": "Prices ($)",
                "theme": "fusion",
                "base": "2",
                "showlegend": "0",
                "drawcrossline": "1"
            },
            "categories": [{
                "category": [
                    {
                      "label": "1850"
                    },
                    {
                      "label": "1930"
                    },
                    {
                      "label": "1986"
                    },
                    {
                      "label": "2000"
                    },
                    {
                      "label": "2005"
                    },
                    {
                      "label": "2010"
                    },
                    {
                      "label": "2014"
                    },
                    {
                      "label": "2018<br>Projected"
                    },
                    {
                      "label": "2025<br>Projected"
                    },
                    {
                      "label": "2030<br>Projected"
                    },
                    {
                      "label": "2035<br>Projected"
                    }
                ]
            }],
            "dataset": [{
                "seriesname": "Prices",
                "data": [
                    {
                      "value": "599900",
                      "tooltext": "Prices in <b>$label</b> was <b>$dataValue $</b>"
                    },
                    {
                      "value": "478600",
                      "tooltext": "Prices in <b>$label</b> was <b>$dataValue $</b>"
                    },
                    {
                      "value": "273000",
                      "tooltext": "Prices in <b>$label</b> was <b>$dataValue $</b>"
                    },
                    {
                      "value": "385000",
                      "tooltext": "Prices in <b>$label</b> was <b>$dataValue $</b>"
                    },
                    {
                      "value": "308000",
                      "tooltext": "Prices in <b>$label</b> was <b>$dataValue $</b>"
                    },
                    {
                      "value": "278000",
                      "tooltext": "Population in <b>$label</b> was <b>$dataValue billion</b>"
                    },
                    {
                      "value": "599000",
                      "dashed": "1",
                      "tooltext": "Population in <b>$label</b> was <b>$dataValue billion</b>"
                    },
                    {
                      "value": "800000",
                      "dashed": "1",
                      "tooltext": "Population projected to reach <b>$dataValue billion</b> by <b>$label</b>"
                    },
                    {
                      "value": "1200000",
                      "dashed": "1",
                      "tooltext": "Population projected to reach <b>$dataValue billion</b> by <b>$label</b>"
                    },
                    {
                      "value": "1450000",
                      "dashed": "1",
                      "tooltext": "Population projected to reach <b>$dataValue billion</b> by <b>$label</b>"
                    },
                    {
                      "value": "2000000",
                      "tooltext": "Population projected to reach <b>$dataValue billion</b> by <b>$label</b>"
                    }
                ]}
            ]
        }"""
    )

    dataSource = {}
    dataSource['chart'] = {
        "caption": "Average Fastball Velocity",
        "xaxisname": "Year Build",
        "yaxisname": "Prices ($)",
        "subcaption": "[2005-2016]",
        "numbersuffix": " $",
        "rotatelabels": "1",
        "setadaptiveymin": "1",
        "theme": "fusion"
    }
    dataSource['categories'] = []
    for i in Houses.objects.all():
        data={}
        data['label'] = i.year_built
    dataSource['data'] = []
    for key in Houses.objects.all():
        data = {}
        data['value'] = key.askprice
        dataSource['data'].append(data)
        dataSource['data'].append(data)
    column2d = FusionCharts("scrollline2d", "ex2" , "100%", "500", "chart-2", "json",dataSource)

    charColumn2D = FusionCharts('column2d','ex2','400','300','chart-2','json',
    """{
        "chart": {
            "caption": "Market Share of Web Servers",
            "plottooltext": "<b>$percentValue</b> of web servers run on $label servers",
            "showlegend": "1",
            "showpercentvalues": "1",
            "legendposition": "bottom",
            "usedataplotcolorforlabels": "1",
            "theme": "fusion"
        },
        "data": [
            {
              "label": "Apache",
              "value": "12"
            },
            {
              "label": "Microsoft",
              "value": "23"
            },
            {
              "label": "Zeus",
              "value": "12"
            },
            {
              "label": "Other",
              "value": "23"
            }
        ]
    }"""
)

    char_numroom = FusionCharts('column2d','ex3','400','300','chart-3','json',
    """{
        "chart": {
            "caption": "Market Share of Web Servers",
            "plottooltext": "<b>$percentValue</b> of web servers run on $label servers",
            "showlegend": "1",
            "showpercentvalues": "1",
            "legendposition": "bottom",
            "usedataplotcolorforlabels": "1",
            "theme": "fusion"
        },
        "data": [
            {
              "label": "Apache",
              "value": "12"
            },
            {
              "label": "Microsoft",
              "value": "23"
            },
            {
              "label": "Zeus",
              "value": "12"
            },
            {
              "label": "Other",
              "value": "23"
            }
        ]
    }"""
)

    return render(request, 'home.html',{'count':count, 'min':min, 'max':max, 'output':chartObj.render(), 'output1':charColumn2D.render(),  'output2':char_numroom.render()})


### About View
def about_page(request):
    return render(request, 'about.html', {})

### Contact view
def contact_page(request):
    return render(request, 'contact.html', {})

### Demo View
def demo_page(request):
    form=DemoForm()
    return render(request, 'demo.html', {'form':form})

### Predict View
def predict(request):
    form=DemoForm(request.POST)
    if form.is_valid():
      obj = Train.objects.all().order_by('-score')[0]
      sopk=form.cleaned_data['sophongkhach']
      sopt=form.cleaned_data['sophongtam']
      sopn=form.cleaned_data['sophongngu']
      dt=form.cleaned_data['dientich']
      namxd=form.cleaned_data['namxaydung']
      kc_trungtam=form.cleaned_data['kc_trungtam']
      kc_sanbay=form.cleaned_data['kc_sanbay']
      kc_taudienngam=form.cleaned_data['kc_taudienngam']
      gia=int(sopk)*obj.coef_num_room+int(sopt)*obj.coef_num_bath+int(sopn)*obj.coef_num_bed
      +float(dt)*obj.coef_living_area+int(namxd)*obj.coef_year_built+float(kc_trungtam)*obj.coef_distance_to_citycenter
      +float(kc_sanbay)*obj.coef_distance_to_airport+float(kc_taudienngam)*obj.coef_distance_to_station

    context = {'form':form, 'sopk':sopk, 'sopt':sopt, 'sopn':sopn, 'dt':dt, 'namxd':namxd, 'kc_trungtam':kc_trungtam, 'kc_sanbay':kc_sanbay, 'kc_taudienngam':kc_taudienngam, 'gia':int(gia)}

    return render(request, 'predict.html', context)

### Load Data View
def load_house_data(request):
    house=Houses.objects.all()
    return render(request, 'others/load_house_data.html', {'house':house})

def train(request):
    train=Train(coef_distance_to_citycenter=main()[0][0],
      coef_distance_to_airport=main()[0][1],
      coef_distance_to_station=main()[0][2],
      coef_year_built=main()[0][3],
      coef_num_room=main()[0][4],
      coef_num_bed=main()[0][5],
      coef_num_bath=main()[0][6],
      coef_living_area=main()[0][7],
      score=main()[1]
      )
    train.save()
    obj=Train.objects.all().order_by('-score')
    return render(request, 'others/train.html', {'obj':obj})

def chart(request):
    dataSource = OrderedDict()
    chartConfig = OrderedDict()
    # chartConfig["caption"] = "Countries With Most Oil Reserves [2017-18]"
    # chartConfig["subCaption"] = "In MMbbl = One Million barrels"
    chartConfig["xAxisName"] = "Room Number"
    chartConfig["yAxisName"] = "Prices"
    chartConfig["numberSuffix"] = "K"
    chartConfig["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs of data
    chartData = OrderedDict()
    chartData["1"] = 290
    chartData["2"] = 260
    chartData["3"] = 180
    chartData["4"] = 140
    chartData["5"] = 115
    chartData["6"] = 100
    chartData["7"] = 30
    chartData["8"] = 30

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # Convert the data in the `chartData`array into a format that can be consumed by FusionCharts.
    #The data for the chart should be in an array wherein each element of the array
    #is a JSON object# having the `label` and `value` as keys.

    #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
    for key, value in chartData.items():
        data = {}
    data["label"] = key
    data["value"] = value
    dataSource["data"].append(data)


    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D = FusionCharts("column2d", "myFirstChart", "500", "300", "myFirstchart-container", "json", dataSource)

    chartObj = FusionCharts('area2d','ex1','600','400','chart-1','json',
        """{
            "chart": {
                "caption": "Yearly sales of iPhone",
                "yaxisname": "Number of units sold",
                "subcaption": "2007-2016",
                "legendposition": "Right",
                "drawanchors": "0",
                "showvalues": "0",
                "plottooltext": "<b>$dataValue</b> iPhones sold in $label",
                "theme": "ocean"
            },
            "data": [
              {
                "label": "2007",
                "value": "1380000"
              },
              {
                "label": "2008",
                "value": "1450000"
              },
              {
                "label": "2009",
                "value": "1610000"
              },
              {
                "label": "2010",
                "value": "1540000"
              },
              {
                "label": "2011",
                "value": "1480000"
              },
              {
                "label": "2012",
                "value": "1573000"
              },
              {
                "label": "2013",
                "value": "2232000"
              },
              {
                "label": "2014",
                "value": "2476000"
              },
              {
                "label": "2015",
                "value": "2832000"
              },
              {
                "label": "2016",
                "value": "3808000"
              }
            ]
        }"""
    )

    chartObj2 = FusionCharts('column2d','ex2','600','400','chart-2','json',
        """{
            "chart": {
                "caption": "Countries With Most Oil Reserves [2017-18]",
                "subcaption": "In MMbbl = One Million barrels",
                "xaxisname": "Country",
                "yaxisname": "Reserves (MMbbl)",
                "numbersuffix": "K",
                "theme": "fusion"
            },
            "data": [
                {
                  "label": "Venezuela",
                  "value": "290"
                },
                {
                  "label": "Saudi",
                  "value": "260"
                },
                {
                  "label": "Canada",
                  "value": "180"
                },
                {
                  "label": "Iran",
                  "value": "140"
                },
                {
                  "label": "Russia",
                  "value": "115"
                },
                {
                  "label": "UAE",
                  "value": "100"
                },
                {
                  "label": "US",
                  "value": "30"
                },
                {
                  "label": "China",
                  "value": "30"
                }
            ]
        }"""
    )

    chartObj3 = FusionCharts('pie2d','ex3','600','400','chart-3','json',
        """{
            "chart": {
                "caption": "Market Share of Web Servers",
                "plottooltext": "<b>$percentValue</b> of web servers run on $label servers",
                "showlegend": "1",
                "showpercentvalues": "1",
                "legendposition": "bottom",
                "usedataplotcolorforlabels": "1",
                "theme": "fusion"
            },
            "data": [
                {
                  "label": "Apache",
                  "value": "32647479"
                },
                {
                  "label": "Microsoft",
                  "value": "22100932"
                },
                {
                  "label": "Zeus",
                  "value": "14376"
                },
                {
                  "label": "Other",
                  "value": "18674221"
                }
            ]
        }"""
    )

    return render(request, 'others/chart.html', {'output': column2D.render(), 'output1':chartObj.render(), 'output2':chartObj2.render(), 'output3':chartObj3.render()})

def chart_2(request):


    return render(request, 'home.html', {'output1': chartColumn2D.render()})
