from django.shortcuts import render

# Create your views here.

def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=D41BE4B3-0084-489C-82D5-A481822F592A")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50)Air  Quality is considered as satisfactory and air pollution poses little"
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 - 100)Air Quality is acceptable;however for small pollutants there may be a moderate health concern for very small number of people who are unusually sensitive for air pollution"
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101 - 150) Altoughgeneralpeople is not likelytobeaffectedatthisAQIrange, peoplewith lung diseaseand olderadults and childrenaregreaterexposure"
            category_color = "USG"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151 - 200) Every one maybegan to experience health effects;members of sensitive groups may experience from serious healtheffects"
            category_color = "Unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201 - 250)HealthAlert: Everyone may experience some serious health effects"
            category_color = "Very Unhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(251 - 300)The entire population is more likely to be affected"
            category_color = "Hazardous"
        return render(request, 'home.html', {'api': api, 'category_description': category_description,
                                             'category_color': category_color})

        return render(request,'home.html', {'zipcode': zipcode})

        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ zipcode+"&distance=5&API_KEY=D41BE4B3-0084-489C-82D5-A481822F592A")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50)Air  Quality is considered as satisfactory and air pollution poses little"
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 - 100)Air Quality is acceptable;however for small pollutants there may be a moderate health concern for very small number of people who are unusually sensitive for air pollution"
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101 - 150) Altoughgeneralpeople is not likelytobeaffectedatthisAQIrange, peoplewith lung diseaseand olderadults and childrenaregreaterexposure"
            category_color = "USG"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151 - 200) Every one maybegan to experience health effects;members of sensitive groups may experience from serious healtheffects"
            category_color = "Unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201 - 250)HealthAlert: Everyone may experience some serious health effects"
            category_color = "Very Unhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(251 - 300)The entire population is more likely to be affected"
            category_color = "Hazardous"
        return render(request, 'home.html', {'api': api, 'category_description': category_description,
                                             'category_color': category_color})


    else:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=D41BE4B3-0084-489C-82D5-A481822F592A")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"

        if api[0]['Category']['Name'] == "Good":
            category_description="(0 - 50)Air  Quality is considered as satisfactory and air pollution poses little"
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description="(51 - 100)Air Quality is acceptable;however for small pollutants there may be a moderate health concern for very small number of people who are unusually sensitive for air pollution"
            category_color = "moderate"
        elif api[0]['Category']['Name']  == "Unhealthy for Sensitive Groups":
            category_description="(101 - 150) Altoughgeneralpeople is not likelytobeaffectedatthisAQIrange, peoplewith lung diseaseand olderadults and childrenaregreaterexposure"
            category_color = "USG"
        elif api[0]['Category']['Name']  == "Unhealthy":
            category_description="(151 - 200) Every one maybegan to experience health effects;members of sensitive groups may experience from serious healtheffects"
            category_color = "Unhealthy"
        elif api[0]['Category']['Name']  == "Very Unhealthy":
            category_description="(201 - 250)HealthAlert: Everyone may experience some serious health effects"
            category_color = "Very Unhealthy"
        elif api[0]['Category']['Name']  == "Hazardous":
            category_description="(251 - 300)The entire population is more likely to be affected"
            category_color = "Hazardous"
        return render(request, 'home.html', {'api': api, 'category_description': category_description,
                                             'category_color' : category_color })

def about(request):
    return render(request, 'about.html', {})
