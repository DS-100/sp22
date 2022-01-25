---
layout: page
title: Home / Schedule
nav_order: 1
description: A week-to-week description of the content covered in the course.
course:
  edstem: https://edstem.org/us/courses/15436/
  edstem_join: https://edstem.org/us/join/TeKcwA
  faq: https://ds100.org/sp22faq
currWeekNumber: 2
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

+ **All discussions (Week 1), Lab Help Sections (Week 2), and office hours (Week 2) will be held online for the first two weeks (through 1/28)**. Zoom links, discussions sign up link is on Ed [here](https://edstem.org/us/courses/15436/discussion/1021263). In-person sections will go back to in-person starting the week of 1/31; lecture will stay hybrid (lecture in-person signup through Week 2: [here](https://www.signupgenius.com/go/805094ea8aa28a3fd0-inperson)).
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
