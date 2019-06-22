# Overall system data

## Description

Python app which can monitor your system. Output write to the plain text file or json file. For monitoring purposes use ​psutil​ module.

App create snapshots of the systems parameters: 

● Overall CPU load 

● Overall memory usage 

● Overall virtual memory usage 

● IO information 

● Network information 

## Installation

`pip install overallsystemdata-1.0-py3-none-any.whl`

## Settings

Settings located in `config.ini` file.
Configure time interval `Interval` of snapshots in seconds.
Configure format `Output` file `json` or `txt`.  

## Running

`../site-packages]$ python overallsystemdata`

or

`$ python  ../site-packages/overallsystemdata`

## Output examples

Example of the structure for output data is about as follows: 

`output.txt`:

SNAPSHOT 1: 2019-06-22 14:22:22.937735: CPU load %: 8.5 Memory usage MB: 8780.484375 Virtual memory usage MB: 5927.24609375 IO information sdiskio(read_count=203903, write_count=1456771, read_bytes=4261850624, write_bytes=19769283072, read_time=2444835, write_time=17097233, read_merged_count=2766, write_merged_count=448697, busy_time=5123983) Network information snetio(bytes_sent=156600102, bytes_recv=317831869, packets_sent=359617, packets_recv=975823, errin=0, errout=0, dropin=1, dropout=0)

`output.json`:
{
    "SNAPSHOT": 1,
    "Time": "2019-06-22 14:04:58.834675",
    "CPU load %:": "18.8",
    "Memory usage MB:": "8366.3125",
    "Virtual memory usage MB:": "6297.2421875",
    "IO information": "sdiskio(read_count=203887, write_count=1436097, read_bytes=4261637632, write_bytes=19461640704, read_time=2444697, write_time=16874145, read_merged_count=2766, write_merged_count=442274, busy_time=5060657)",
    "Network information": "snetio(bytes_sent=154627243, bytes_recv=313055427, packets_sent=353893, packets_recv=964888, errin=0, errout=0, dropin=1, dropout=0)"
}
 
