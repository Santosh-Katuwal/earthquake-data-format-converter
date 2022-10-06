*********INSTRUCTION******
(First, install obspy lybrary using "pip install obspy")
1. Prepare *.csv file with header E, N and Z. Where E is EW vibration, N represents NS vibration and Z represents UD vibration
2. Run "input format converter.py"
3. Enter:
    Event date as YYYY-MM-DD
    Event time as HH:MM:SS
    Sampling time step (dt)
    Network ID (Any text shorter than 11 letters)
    Location ID (Any text shorter than 11 letters)
    Station ID (Any text shorter than 11 letters)
    Output format: choose one from (MSEED, SAC, GSE2, SACXY, Q, SH_ASC, SLIST, TSPAIR, PICKLE, SEGY, SU, WAV, AH)
    File name: provide desired filename\
It will create a file with provided filename with choosen format extension
