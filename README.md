
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

Query of overpass 'ways' data around Gorkha, Nepal (5/10/2015). Query constructed using overpass-turbo.eu, processed using python.


    /*
    This shows the roads in gorkha,nepal.
    */

    [out:json];

    (
    way ["highway"~"motorway|trunk|primary|motorway_link|trunk_link|primary_link|unclassified|tertiary|secondary|track|path"]({{bbox}});
    );

    out meta;
    >;
    out skel qt;


Neon Green = "2 days after quake"
(for gorkha_roads, 551 LineStrings)
(for nepal_roads, 5330 LineStrings)

Yellow = "1 week after quake"
(for gorkha_roads, 1,824 LineStrings)
(for nepal_roads, 15,863 LineStrings)

Orange = "over a week to 16 days after quake"
(for gorkha_roads, 1/530 LineStrings)
(for nepal_roads, 10,440 LineStrings)

Red = "17 days after quake - day of 7.3 magnitude aftershock"
(for gorkha_roads, 248 LineStrings)
(for nepal_roads, 1,184 LineStrings)

Gray = "Last edited before quake"
(for gorkha_roads, 114 LineStrings)
(for nepal_roads, 3,673 LineStrings)

*[Link to Gorkha query in Overpass](http://overpass-turbo.eu/s/9jS "Link to Gorkha query in Overpass")

*[Link to Nepal query in Overpass](http://overpass-turbo.eu/s/9jX "Link to Nepal query in Overpass")

*[Directions on how to create a url link to a OSM JSON file](http://www.mappa-mercia.org/2014/09/creating-an-always-up-to-date-map.html "URL-OSM JSOM")

*[Raw Gorkha JSON from Overpass](http://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3B%28way%5B%22highway%22~%22motorway%7Ctrunk%7Cprimary%7Cmotorway_link%7Ctrunk_link%7Cprimary_link%7Cunclassified%7Ctertiary%7Csecondary%7Ctrack%7Cpath%22%5D%2827%2E892190893968916%2C84%2E50340270996094%2C28%2E07894754104761%2C84%2E76089477539062%29%3B%29%3Bout%20meta%3B%3E%3Bout%20skel%20qt%3B%0A
 "Raw Gorkha JSON from Overpass")
 
*[Raw Nepal JSON from Overpass - very large, may not load in browser](http://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3B%28way%5B%22highway%22~%22motorway%7Ctrunk%7Cprimary%7Cmotorway_link%7Ctrunk_link%7Cprimary_link%7Cunclassified%7Ctertiary%7Csecondary%7Ctrack%7Cpath%22%5D%2827%2E610538528074823%2C84%2E38873291015625%2C28%2E357567857801694%2C85%2E418701171875%29%3B%29%3Bout%20meta%3B%3E%3Bout%20skel%20qt%3B%0A "Raw Nepal JSON from Overpass - very large, may not load in browser")

*NOTE: THIS PROJECT IS STILL in progress as of 5/10/2015*
 
</body>
</html>