# InSight Wether API

![Insight Photo](https://hsto.org/webt/cw/gx/ad/cwgxadrbny22ynoldahmnnwqc8g.png)

#### InSight? What is it?

InSight (Interior Exploration using Seismic Investigations, Geodesy and Heat Transport) is a NASA Discovery Program mission that will place a single geophysical lander on Mars to study its deep interior. It've landed some years ago and already give to scinetific sosiety a lot of data to their researches. You can get more information about it [here](https://mars.nasa.gov/insight/)
![Photo](https://i0.wp.com/itc.ua/wp-content/uploads/2020/02/dims-3-3.jpg?fit=1920%2C1080&quality=100&strip=all&ssl=1)

#### What data is it measuring?
All of this information avalible with this API. 
 - Temperatue (averede per sol*, min, max)
 - Wind Speed (averede per sol*, min, max)
 - Atmosphere Pressure (averede per sol*, min, max)
 - Wind Direction

_\* Sol - mars's equivalent of Eath day. It is approximately 24 hours, 39 minutes, 35 seconds long. A Martian year is approximately 668 sols, equivalent to approximately 687 Earth days._

#### So what is the problem of usinf official NASA API?
Insight mission has official [API](https://api.nasa.gov/). But there are problems that you will face using it:
 - You can get data only for six last sols - it is the main problem
 - You have only 500 requests per hour per one API key for all nasa's services
 - Nasa returns data in very uncomfortable format
 
#### My solution of these problems
I am going to create my own API. It will get data from nasa server, save it to MySQL. Other people will be able to access this data through the API. 


![scheme](https://github.com/freQuensy23-coder/Insight_MarsWether_API/blob/master/photos/plan.png)

 #### What can I do?
 You can get data from my API using HTTP requests, or deploy your own server (I would recommend using Amazon ABC). You can also just download the data, they are automatically uploaded to the github.
 
 
![InSight](https://24gadget.ru/uploads/posts/2019-06/1560939536_mars_nasa__gov_insight-raw-images_surface_sol_0122_idc_d028r0122_607337988edr_f0103_0100m_.jpg)
 
#### HTTP request example
Sorry,  but API still unavaliblee

 #### How can I help?
 If you have your own server or VPS/VDS on which I can keep my script running, then I will be very grateful if you write to me about it. If you have access to old data from InSight (up to 650 sol), then let me know about it, I would like to add it to the API. Also y\ou can check TODO list [here](https://www.evernote.com/shard/s633/sh/e71dc5f1-c6f8-4e09-d59c-102c4c48fa24/f71d29918c9a2f09241e1004a3d842e5)
