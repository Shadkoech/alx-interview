# 0x03. Log Parsing

## Overview
This interview question focuses on parsing and processing data streams in real-time using Python programming. The task involves reading from standard input (stdin), handling data in a specific format, and performing calculations based on the input data. The main goal is to develop a script that computes metrics based on log entries.

## The Question
The main breakdown is a way of developing a Python script to parse and process log data in real-time. Some of the key aspects to handle include:

- Reading from standard input (stdin) line by line.
- Validating the format of each log entry using regular expressions.
- Computing metrics such as total file size and the number of lines by HTTP status code.
- Printing the computed metrics after every 10 lines of log data or upon keyboard interruption (CTRL + C).
- Handling possible exceptions during file reading and data processing to ensure the script's robustness.


## Task:

Files:

    - 0-stats.py, 0-generator.py
Write a script that reads stdin line by line and computes metrics:
- Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
- After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
    * Total file size: File size: <total size>
    * where <total size> is the sum of all previous <file size> (see input format above)
    * Number of lines by status code:
        - possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
        - if a status code doesn’t appear or is not an integer, don’t print anything for this status code
        - format: <status code>: <number>
        - status codes should be printed in ascending order
