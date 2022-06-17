# GuiltySpark

GuiltySpark is a simple daemon that allows applications to register themselves. The application will be a child instance of an abstract class that defines a simple get() method. This method returns either a value or list of values which the daemon then logs. GuiltySpark also implements asciiplot to allow in console viewing of logged data

# Note

Currently the application is just hard coded to listen to my computers cpu temp values. I am still building it out.

# Usage

A primary usage I want to use this for is logging parameters on my RaspberryPi such as CPU temp, CPU Throttling, etc. Once I get a database instacne running on it, I will register another monitor(s) to log some of those items.
