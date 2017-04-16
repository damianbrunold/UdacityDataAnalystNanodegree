Summary
-------

The visualization shows the development of the number of refugees seeking
asylum in switzerland between the years 1986 and 2015. For peak years, the
total number of refugees is broken down by country of origin and this
information is brought in relation to regional and world events (wars). 
In addition, the time line is annotated with information 
about major changes to the laws regulating asylum in switzerland.

Design
------

First draft:

- Use a line diagram for visualizing the time series of refugee counts.
  The x axis spans from 1986 to 2016. The y axis spans from 0 to a little
  more than the maximum refugee count (i.e. 50'000). This diagram type
  communicates best the development of the data over time.

- Use a solid line as x axis with yearly tick marks and labels below it.
  This helps define the "bottom" of the graph and is needed to provide a solid
  visual grasp of the years.
  
- Use only tick marks and numbers every 10000 for the vertical axis, no axis line.
  The axis line is not needed and would only increase the ink to data ratio.
  
- Use dark blue and moderatly thick line for the time series. The blue color
  does not interfere with color blindness and is less hard that e.g. black.
  Making the line a little thicker than the axis lets the viewer focus on
  the data.

Second draft:

- Add a circle to the peak years. This increases the focus on the peaks.
  In addition, label the peak years with the actual values. This provides
  concreteness in the most important parts of the graph.

- On mouse over of these circles, show a bar chart containing the top 5
  counts per country of origin. This provides more information about these
  peaks without cluttering the basic design. Also, as the height of the bar
  chart matches the corresponding data point, it provides a very natural
  decomposition of the labeled value.

Final visualization:

- Add horizontal lines below chart to signify wars. Make these lines very thick 
  and red because they stand for wars. These lines are very helpful for 
  correlating wars with the peaks of the graph.
  
- Add paragraph symbol text for changes of the asylum law. This shows in an
  unobtrusive way the years when the asylum law was made more restrictive.

- Add mouse over for the symbols to show additional information about the
  event (what war, what change of law). This gives more context without cluttering
  the basic chart design.

- Add text explaining wars and changes of law below the chart. These explanations
  are not really part of the chart but help in interpreting it.


Feedback
--------

(Feedback was given orally by Nils, Jona and Rahel. Nils is a colleague
at work and Jona and Rahel are from my family.)

Feedback for first draft:

Nils: Add information about country of origin, at least for peak years ("crisis" years).

Feedback for second draft:

Nils: Add information about world and regional events (e.g. wars)
Rahel: Add information about changes to the asylum laws
Jona: Add legend for symbols used to depict wars and law changes

Feedback from Udacity/Ben:

- Improve code quality by adding comments and reusing code using functions
- Add explanatory text re law changes below chart
- Improve data loading by consolidating country data in one table and filtering by year


Resources
---------

- Course materials
- Knaflic, Storytelling with Data
- Staatssekretariat fuer Migration (SEM)
