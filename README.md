*********INSTRUCTION******
(First, install obspy lybrary using "pip install obspy")
1. Prepare *.csv file with header E, N and Z. Where E is EW vibration, N represents NS vibration and Z represents UD vibration
2. Run "input format converter.py"
3. Enter event date as YYYY-MM-DD
4. Enter event time as HH:MM:SS
5. Enter sampling time step (dt)
6. Enter network ID (Any text shorter than 11 letters)
7. Enter location ID (Any text shorter than 11 letters)
8. Enter station ID (Any text shorter than 11 letters)
9. Output format: choose one from (MSEED, SAC, GSE2, SACXY, Q, SH_ASC, SLIST, TSPAIR, PICKLE, SEGY, SU, WAV, AH)
10. File name: provide desired filename.
It will create a file with provided filename with choosen format extension
