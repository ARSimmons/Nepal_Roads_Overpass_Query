
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

Query of overpass 'ways' data in Nepal (5/10/2015). Query constructed using overpass-turbo.eu, processed using python.

'''
[out:json]
;
way
  ["highway"~"motorway|trunk|primary|motorway_link|trunk_link|primary_link|unclassified|tertiary|track|path"]
  (26.902476886279807,84.122314453125,28.294707428421205,86.1822509765625);

out meta center;
>;
out skel qt;
'''

Red = "2 days after quake"

Orange-Yellow = "1 week after quake"

Yellow = "15 days after quake"

Gray = "Last edited before quake"

*[Directions on how to create a url link to a OSM JSON file](http://www.mappa-mercia.org/2014/09/creating-an-always-up-to-date-map.html "URL-OSM JSOM")

*[Raw JSON from Overpass](http://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3Bway%5B%22highway%22~%22motorway%7Ctrunk%7Cprimary%7Cmotorway_link%7Ctrunk_link%7Cprimary_link%7Cunclassified%7Ctertiary%7Ctrack%7Cpath%22%5D%2826%2E902476886279807%2C84%2E122314453125%2C28%2E294707428421205%2C86%2E1822509765625%29%3Bout%20meta%20center%3B%3E%3Bout%20skel%20qt%3B%0A
 "Raw JSON from Overpass")

*NOTE: THIS PROJECT IS STILL in progress as of 5/10/2015*
 
</body>
</html>