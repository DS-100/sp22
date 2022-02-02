---
layout: page
title: Home / Schedule
nav_order: 1
description: A week-to-week description of the content covered in the course.
course:
  edstem: https://edstem.org/us/courses/15436/
  edstem_join: https://edstem.org/us/join/TeKcwA
  faq: https://ds100.org/sp22faq
currWeekNumber: 3
---

# Principles and Techniques of Data Science

{: .mb-2 }
UC Berkeley, Spring 2022
{: .mb-0 .fs-6 .text-grey-dk-000 }

<p>
<a href="https://edstem.org/us/courses/15436/discussion/1004495" class="btn btn-blue">Lecture Zoom</a>
<a href="https://edstem.org/us/courses/15436/discussion/1021263" class="btn btn-purple">Discussion Sign-Up/Zoom</a>
<a href="{{site.baseurl}}/calendar" class="btn btn-green">Office Hour/Lab Help</a>
</p>

<div>
{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
<div class="role">
  {% for staffer in instructors %}
  {{ staffer }}
  {% endfor %}
</div>
</div>

Jump to current week: [here](#week-{{page.currWeekNumber}}).

+ Lecture is hybrid: in-person in Li Ka Shing 245 and online via Zoom (see link above). Recordings will be posted within 12 hours of live lecture.
+ For discussion recordings, see this Jupyter [notebook](https://data100.datahub.berkeley.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FDS-100%2Fsp22&urlpath=tree%2Fsp22%2Fdisc%2Fdisc_recording_links.ipynb&branch=main). 
+ **Frequently Asked Questions:** Before posting on the [class Ed]({{page.course.edstem}}), please read the [class FAQ page]({{page.course.faq}}).
+ Join Ed: [here]({{page.course.edstem_join}}).
+ Textbook readings are optional and actively in development. See the [Resources]({{site.baseurl}}/resources/#textbook) for more details.
+ **Note:** The schedule of lectures and assignments is subject to change.

<br><br>

<a name="schedule"></a>
## Schedule

{% for module in site.modules %}
<a name="week-{{module.weekNumber}}"></a>
{{ module }}
{% endfor %}
