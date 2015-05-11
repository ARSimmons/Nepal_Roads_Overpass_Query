
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
    way ["highway"~"motorway|trunk|primary|motorway_link|trunk_link|primary_link|unclassified|tertiary|track|path"]({{bbox}});
    );

    out meta;
    >;
    out skel qt;


Red = "2 days after quake"
(for gorkha_roads, 720 ways)

Yellow = "1 week after quake"
(for gorkha_roads, 1957 ways)

Pink = "15 days after quake"
(for gorkha_roads, 1388 ways)

Gray = "Last edited before quake"
(in this query, none found)

*[Link to Gorkha query in Overpass](http://overpass-turbo.eu/s/9hl "Link to Gorkha query in Overpass")

*[Directions on how to create a url link to a OSM JSON file](http://www.mappa-mercia.org/2014/09/creating-an-always-up-to-date-map.html "URL-OSM JSOM")

*[Raw Gorkha JSON from Overpass](http://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3B%28way%5B%22highway%22~%22motorway%7Ctrunk%7Cprimary%7Cmotorway_link%7Ctrunk_link%7Cprimary_link%7Cunclassified%7Ctertiary%7Ctrack%7Cpath%22%5D%2827%2E892190893968916%2C84%2E50340270996094%2C28%2E07894754104761%2C84%2E76089477539062%29%3B%29%3Bout%20meta%3B%3E%3Bout%20skel%20qt%3B%0A
 "Raw Gorkha JSON from Overpass")

*NOTE: THIS PROJECT IS STILL in progress as of 5/10/2015*
 
</body>
</html>