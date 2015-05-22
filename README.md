
<html>
<head>
</head>
<body>
# Table of Contents
[Team Members](#team-members)

[Project Summary](#project-summary)

# <a name="team-members"></a>Team Members
* "Arielle Simmons" <ari.ucb.fire@gmail.com>
	- Data Engineer 
	
# <a name="project-summary"></a>Project Summary

Query of overpass 'ways' data in Nepal (5/13/2015). Query constructed using overpass-turbo.eu, processed using python. Below 
is the query used for all of Nepal. The enclosed geojson files are subsets of this query (mostly because it was too big to 
render at github). 

The full dataset (of all of Nepal) was queried out using the below query, and exported as a shapefile. 
The shapefile was converted into a Tableau format using MSolbrig's [TabShapeR](https://github.com/msolbrig/TabShapeR "TabShapeR") tool.
The final viz [here](https://public.tableau.com/profile/arielle.ari.simmons6630#!/vizhome/NepalEarthquakeAstudyofOSMvolunteerimpacts/StoryThelongtailofOSMvolunteering "here").


    /*
    This shows the roads in nepal.
    */

    [out:json];

    area[name="नेपाल"];
    (way["highway"~"motorway|trunk|primary|motorway_link|trunk_link|primary_link|unclassified|tertiary|secondary|track|path|residential|service|services|secondary_link|tertiary_link"](area);
    );

    out meta;
    >;
    out skel qt;

Key for the 'sample' geojson files:

Neon Green = "2 days after quake"

Yellow = "1 week after quake"

Orange = "over a week to 16 days after quake"

Red = "17 days after quake - day of 7.3 magnitude aftershock"

Gray = "Last edited before quake"


*[Link to Gorkha query in Overpass](http://overpass-turbo.eu/s/9wx "Link to Gorkha query in Overpass")

*[Link to Nepal shake zone query in Overpass](http://overpass-turbo.eu/s/9jX "Link to Nepal shake zone query in Overpass")

*[Link to Nepal roads query in Overpass](http://overpass-turbo.eu/s/9li "Link to Nepal query in Overpass")

*[Directions on how to create a url link to a OSM JSON file](http://www.mappa-mercia.org/2014/09/creating-an-always-up-to-date-map.html "URL-OSM JSOM")

*[Raw Gorkha JSON from Overpass](http://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3B%28way%5B%22highway%22~%22motorway%7Ctrunk%7Cprimary%7Cmotorway_link%7Ctrunk_link%7Cprimary_link%7Cunclassified%7Ctertiary%7Csecondary%7Ctrack%7Cpath%22%5D%2827%2E892190893968916%2C84%2E50340270996094%2C28%2E07894754104761%2C84%2E76089477539062%29%3B%29%3Bout%20meta%3B%3E%3Bout%20skel%20qt%3B%0A
 "Raw Gorkha JSON from Overpass")
 
*[Raw Nepal JSON from Overpass - very large, may not load in browser](http://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3B%28way%5B%22highway%22~%22motorway%7Ctrunk%7Cprimary%7Cmotorway_link%7Ctrunk_link%7Cprimary_link%7Cunclassified%7Ctertiary%7Csecondary%7Ctrack%7Cpath%22%5D%2827%2E610538528074823%2C84%2E38873291015625%2C28%2E357567857801694%2C85%2E418701171875%29%3B%29%3Bout%20meta%3B%3E%3Bout%20skel%20qt%3B%0A "Raw Nepal shake zone JSON from Overpass - very large, may not load in browser")

*[Raw ALL of NEPAL JSON from Overpass - very large, may not load in browser](http://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3Barea%5B%22name%22%3D%22%E0%A4%A8%E0%A5%87%E0%A4%AA%E0%A4%BE%E0%A4%B2%22%5D%3B%28way%5B%22highway%22~%22motorway%7Ctrunk%7Cprimary%7Cmotorway_link%7Ctrunk_link%7Cprimary_link%7Cunclassified%7Ctertiary%7Csecondary%7Ctrack%7Cpath%7Cresidential%7Cservice%7Csecondary_link%7Ctertiary_link%22%5D%28area%29%3B%29%3Bout%20meta%3B%3E%3Bout%20skel%20qt%3B%0A "Raw Nepal JSON from Overpass - very large, may not load in browser")


*NOTE: THIS PROJECT IS FINISHED AS OF 5/21/2015*
 
</body>
</html>