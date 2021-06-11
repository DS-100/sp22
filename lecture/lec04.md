---
layout: page
title: Lecture 4 – SQL
nav_exclude: true
---

# Lecture 4 - SQL

Presented by Anthony D. Joseph

Content by Anthony D. Joseph, Allen Shen, Josh Hug, John DeNero, Joseph Gonzalez

- [slides](https://docs.google.com/presentation/d/1iM8dv-LFEghSMQr4-sh6JnaAUGHV-3j4FLu-718YCzU/edit?usp=sharing)
- [video playlist](https://www.youtube.com/playlist?list=PLQCcNQgUcDfqNOs2WA_9ZXw5wE4-KVbkA)
- [code](https://github.com/DS-100/sp21/tree/main/lec/lec04) ([launch](https://data100.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/DS-100/sp21&subPath=lec/lec04/&branch=main))
- [code HTML](../../resources/assets/lectures/lec04/lec04.html)
- [code walkthrough by Josh Hug](https://youtu.be/QCrHZnLM0H4)
- [code walkthrough by Allen Shen](https://youtu.be/zetdBg61eaE)

A reminder – the right column of the table below contains _Quick Checks_. These are **not** required but suggested to help you check your understanding.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>Video</th>
<th>Quick Check</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>4.1</strong> <br> Databases and database management systems.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/SRoTXarDDk4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSdy8xeb-E5FEfrlIz4LJopIddUoFrJAAKY1Mg_GIqFymZuFZA/viewform" target="\_blank">4.1</a></td>
</tr>
<tr>
<td><strong>4.2</strong> <br> Relational database schemas.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/SJtoYIqGvEI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSeGCwtpFhXBq4RTg7ZebI8jdOM4yut3gwyF-tz-xNe44vMngg/viewform" target="\_blank">4.2</a></td>
</tr>
<tr>
<td><strong>4.3</strong> <br> SQL overview and the DISTINCT keyword.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/_WyqfDM1mN4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSeLuZWerXoDKqHIobG6B1vH0p35pZCz1qQc5ff5rT91cV-AKg/viewform" target="\_blank">4.3</a></td>
</tr>
<tr>
<td><strong>4.4</strong> <br> Types of joins in SQL.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/E5XPBV54MiQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfwvjklDzvLRroL26Gpe5_kcD9XEY59TfxAhYBeO2ROCOy0Vw/viewform" target="\_blank">4.4</a></td>
</tr>
<tr>
<td><strong>4.5</strong> <br> NULL values in SQL.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/K89kIINyjTM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfwKtSQFSA4yyp9JJ86VTr9sSHPp3SEI0t6VTOrh2GW05Xt6Q/viewform" target="\_blank">4.5</a></td>
</tr>
<tr>
<td><strong>4.6</strong> <br> SQL predicates and casting.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/af3vjZsz1BQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfdb-_737z6rUbC4WzQN_QUfgw54voslfzMHlvsO5Dx6lWu9A/viewform" target="\_blank">4.6</a></td>
</tr>
<tr>
<td><strong>4.7</strong> <br> SQL sampling, subqueries, and common table expressions.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/3TgY0zNbjoo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfLL2wU0Nk9h_Abk3zojYa3d96YEMpCOsQ-SoRF2tBAe-s2Rw/viewform" target="\_blank">4.7</a></td>
</tr>
<tr>
<td><strong>4.8</strong> <br> SQL CASE expressions and the SUBSTR function.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/MIE9NbCOyyQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfk0Dw-dgH_jx6OTg2KXUxTBtH7Napj-yBbZI1O04Bf6PauZA/viewform" target="\_blank">4.8</a></td>
</tr>
<tr>
<td><strong>4.9</strong> <br> SQL summary and conclusion.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/ch0LW6R1VrM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfJK4hk4Ue9jicRYEro0goTEyqz7EgbcaQ3WTDnWdnU9ehY8Q/viewform" target="\_blank">4.9</a></td>
</tr>
