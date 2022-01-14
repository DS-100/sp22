---
layout: page
title: Home
nav_order: 1
description: A week-to-week description of the content covered in the course.
---

# Principles and Techniques of Data Science

## Note: This page is under construction. Everything on this website is subject to change.

{: .mb-2 }
UC Berkeley, Spring 2022
{: .mb-0 .fs-6 .text-grey-dk-000 }


<div>
<!-- {% assign instructors = site.staffers | where: 'role', 'Instructor' %}
<div class="role">
  {% for staffer in instructors %}
  {{ staffer }}
  {% endfor %} -->
</div>

+ **Frequently Asked Questions:** Before posting on the [class Ed](https://edstem.org/us/courses/15436/), please read the [class FAQ page](https://ds100.org/sp22faq).
+ The [Syllabus]({{site.baseurl}}/syllabus) page contains a detailed explanation of how each course component will work this semester, given the course will be taught in a hybrid format.
+ The scheduling of all weekly events is in the [Calendar]({{ site.baseurl }}/calendar)
+ Zoom links for any remote live events will be posted on EdStem once they are available.
+ **Note:** The schedule of lectures and assignments is subject to change.

<br><br>

{% for module in site.modules %}
{{ module }}
{% endfor %}
