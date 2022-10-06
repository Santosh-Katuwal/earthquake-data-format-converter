*********INSTRUCTION******
(First, install obspy lybrary using "pip install obspy")
1. Prepare *.csv file with header E, N and Z. Where E is EW vibration, N represents NS vibration and Z represents UD vibration
2. Run "input format converter.py"
3. Enter:
    a.Event date as YYYY-MM-DD
    b. Event time as HH:MM:SS
    c. Sampling time step (dt)
    d. Network ID (Any text shorter than 11 letters)
    e. Location ID (Any text shorter than 11 letters)
    f. Station ID (Any text shorter than 11 letters)
    g. Output format: choose one from (MSEED, SAC, GSE2, SACXY, Q, SH_ASC, SLIST, TSPAIR, PICKLE, SEGY, SU, WAV, AH)
    h. File name: provide desired filename
It will create a file with provided filename with choosen format extension
