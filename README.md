# Calendar_Puller
Recreates a case database from disjointed pdf files online by automating a web browser, downloading pdfs, converting to text, and regex analysis on strings.

Local court did not grant practitioners access to the court case database backend.  Rather, what could be accessed publicly was a site that had various .pdfs of the calendars.

Practitioners need to pull all cases, note changes to court calendars, and compare 

Step 1 is to recreate the court's database of cases so that those entries can be compared to practitioners' internal databases.

These two programs get *most* of the way through Step 1.

GUIandDatePicker automates a web browser to select today, tomorrow, or another day.  (GUI for user-friendliness.)

PdfToTextAndSplit changes the pdf files to text, finds judge and department, and breaks case entries into strings in a list.  (From there, the goal would be to process the strings into database entries for comparison, see future plan 5, below.)

(Site: http://www.imperial.courts.ca.gov/CourtCalendars/Public/MCalendars.aspx
A copy of a random day of the site is in the "samplecalpage" folder.
Copies of a random day of calendars are in the "calendars" folder.)

Known issues / future plans:

1.  "Tomorrow" date picker does not work on Friday (because of weekend), need to tweak to only pick work (court) days.
2.  Goal would be to extend the os.makedir to make folders for each day picked and sub-folders for each time calendars were pulled (for comparison).
3.  Also regexes that get data (judge, department, case data) should return that data as functions so that data can then be passed elsewhere.
4.  Realistically my office is probably going to synch with the court system in the near future so most of this will be rendered obsolete/useless.  Just putting it out there because it actually works (thus far).  See also 6.
5.  Need to choose a database/case management approach on the client end.  Then the lists of case strings can be broken down into database / dictionary entries so that, each time the calendar is pulled, changes are highlighted (and/or conflicts with the client's internal client/calendar management database can be noted).
6.  See 4 if this never gets finished/updated.

