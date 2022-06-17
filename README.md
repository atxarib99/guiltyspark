# GuiltySpark

GuiltySpark is a simple daemon that allows applications to register themselves. The application will be a child instance of an abstract class that defines a simple get() method. This method returns either a value or list of values which the daemon then logs. GuiltySpark also implements asciiplot to allow in console viewing of logged data

# Note

Currently the application is just hard coded to listen to my computers cpu temp values. I am still building it out.

# Usage

A primary usage I want to use this for is logging parameters on my RaspberryPi such as CPU temp, CPU Throttling, etc. Once I get a database instacne running on it, I will register another monitor(s) to log some of those items.

```python
py viewer.py tempmonitor 30                                                                                                                                                                                             ✔ 
30
69.0┤              ╭╮           ╭───╮           ╭───╮              ╭╮
67.8┤              │╰╮          │   │           │   │              ││
66.5┤              │ │         ╭╯   ╰╮          │   ╰╮             │╰╮
65.2┤              │ │         │     │         ╭╯    │             │ │
64.0┤              │ ╰╮       ╭╯     ╰╮        │     │            ╭╯ │
62.8┤              │  │       │       │        │     ╰╮           │  ╰╮
61.5┤  ╭╮          │  │      ╭╯       │        │      │           │   │
60.2┤  ││         ╭╯  ╰╮     │        ╰╮       │      ╰╮          │   ╰╮
59.0┤ ╭╯│         │    │    ╭╯         │      ╭╯       │         ╭╯    │                ╭╮
57.8┤ │ ╰╮        │    ╰╮   │          ╰╮   ╭─╯        │         │     │                ││
56.5┤╭╯  │        │     │  ╭╯           │  ╭╯          ╰╮        │     ╰╮               │╰╮
55.2┤│   ╰╮       │     ╰╮╭╯            │╭─╯            │        │      │               │ │
54.0┼╯    │       │      ││             ╰╯              ╰╮       │      ╰╮              │ │
52.8┤     │       │      ╰╯                              │     ╭─╯       │             ╭╯ ╰╮
51.5┤     ╰╮      │                                      ╰╮  ╭─╯         │             │   │
50.2┤      │      │                                       │ ╭╯           ╰╮       ╭╮   │   ╰
49.0┤      │     ╭╯                                       │╭╯             │       ││   │
47.8┤      ╰╮    │                                        ╰╯              │      ╭╯│   │
46.5┤       │    │                                                        ╰╮    ╭╯ ╰╮ ╭╯
45.2┤       ╰╮   │                                                         │    │   │ │
44.0┤        │   │                                                         ╰╮  ╭╯   ╰╮│
42.8┤        │   │                                                          │ ╭╯     ││
41.5┤        ╰─╮ │                                                          ╰─╯      ││
40.2┤          ╰╮│                                                                   ╰╯
39.0┤──┬──┬──┬──├╯─┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬
    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29


```
