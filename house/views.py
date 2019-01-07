from django.shortcuts import render
from .models import Houses
from .form import DemoForm, ContactForm
from .fusioncharts import FusionCharts
from collections import OrderedDict

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
        tongsp=form.cleaned_data['tongsophong']
        sopt=form.cleaned_data['sophongtam']
        sopn=form.cleaned_data['sophongngu']
        dt=form.cleaned_data['dientich']
        namxd=form.cleaned_data['namxaydung']
        num_parking=form.cleaned_data['num_parking']
        accessible_buildings=form.cleaned_data['accessible_buildings']
        family_quality=form.cleaned_data['family_quality']
        art_expos=form.cleaned_data['art_expos']
        emergency_shelters=form.cleaned_data['emergency_shelters']
        emergency_water=form.cleaned_data['emergency_water']
        Facilities=form.cleaned_data['Facilities']
        fire_stations=form.cleaned_data['fire_stations']
        Cultural=form.cleaned_data['Cultural']
        Monuments=form.cleaned_data['Monuments']
        police_stations=form.cleaned_data['police_stations']
        Vacant=form.cleaned_data['Vacant']
        Free_Parking=form.cleaned_data['Free_Parking']

        gia=int(tongsp)*13751.10116381+int(sopt)*89321.15969309+int(sopn)*6526.17965324+float(dt)*1035.54943042+int(namxd)*-144.05252464+int(num_parking)*1088.35985992+int(accessible_buildings)*-23292.72959269+int(family_quality)*-911.07133462+int(art_expos)*608.89750596+int(emergency_shelters)*-8713.4451033+int(emergency_water)*1953.67136794+int(Facilities)*597.20578898+int(fire_stations)*6222.19201123+int(Cultural)*-3639.5882536+int(Monuments)*3257.4615672+int(police_stations)*-9571.69925624+int(Vacant)*-2171.98986075+int(Free_Parking)*599.07022918 + 347150.604548

    context = {'form':form, 'tongsp':tongsp, 'sopt':sopt, 'sopn':sopn, 'dt':dt, 'namxd':namxd, 'num_parking':num_parking, 'accessible_buildings':accessible_buildings, 'family_quality':family_quality, 'art_expos':art_expos, 'emergency_shelters':emergency_shelters, 'emergency_water':emergency_water, 'Facilities':Facilities, 'fire_stations':fire_stations, 'Cultural':Cultural, 'Monuments':Monuments, 'police_stations':police_stations, 'Vacant':Vacant, 'Free_Parking':Free_Parking, 'gia':int(gia)}

    return render(request, 'predict.html', context)

### Load Data View
def load_house_data(request):
    house=Houses.objects.all()
    return render(request, 'others/load_house_data.html', {'house':house})
# Chart
def chart(request):
    dataSource = OrderedDict()
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Countries With Most Oil Reserves [2017-18]"
    chartConfig["subCaption"] = "In MMbbl = One Million barrels"
    chartConfig["xAxisName"] = "Room Number"
    chartConfig["yAxisName"] = "Count"
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
