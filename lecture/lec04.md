---
layout: page
title: Lecture 5 – Pandas, Part 1
nav_exclude: true
---

# Lecture 5 - Pandas, Part 1

Presented by Fernando Perez

Content by Fernando Perez, Josh Hug

- [slides](https://docs.google.com/presentation/d/1afDZnCeBrzdOlL3osFNb3hdb21Hrt0pJG02USEqIGPw/edit#slide=id.g8ae4121a16_0_1022)
- [video playlist](https://www.youtube.com/playlist?list=PLQCcNQgUcDfrlNxXQA6EHN_WYIstpeoq6)
- [code](https://github.com/DS-100/sp21/tree/main/lec/lec05) ([launch](https://data100.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/DS-100/sp21&subPath=lec/lec05/&branch=main))
- [code HTML](../../resources/assets/lectures/lec05/lec05.html)
- [Intro to Pandas if you’ve taken Data 8 (zip)](https://github.com/DS-100/sp21/raw/main/lec/lec05/pandas_for_data8_students.zip)

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
<td><strong>5.0</strong> <br> Announcements, SQL Review.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/PQJ_TD-tP7A" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td></td>
</tr>
<tr>
<td><strong>5.1.1</strong> <br> Pandas data frames, series, and indices.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/VWa5J1GDHgE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfjSg127wS2MMUXoTx2pLeYeh0Nm2kGXpolBq_TsITdbpsKNg/viewform" target="\_blank">5.1.1</a></td>
</tr>
<tr>
<td><strong>5.1.2</strong> <br> Pandas indices demo.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/ZhK5CRbJ9co" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSe7Z9itKw0lJu14tBf7mBJohyN5HV1iuvRdz3oHyBtjfPmT1g/viewform" target="\_blank">5.1.2</a></td>
</tr>
<tr>
<td><strong>5.2</strong> <br> Pandas indexing with the bracket operator.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/J5pN8YFacfU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSf8X6Cbi-UJQ-CmP0hNJ6ZBgAr76YAVsQXv_j2h2jucBHkOhg/viewform" target="\_blank">5.2</a></td>
</tr>
<tr>
<td><strong>5.3</strong> <br> Pandas boolean array selection, the isin function, and the query command.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/DaL2ekf-sls" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSe911sH56reSznqFbszYtZqjj1lMr794WDD4GI7Mqr1nvrkuw/viewform" target="\_blank">5.3</a></td>
</tr>
<tr>
<td><strong>5.4.1</strong> <br> Pandas indexing with .loc.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/_nvnW7I2N2g" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfM38F5u5pEZAcgY19HZT6RAhg0eumUei0pf7Pd7YOb_oFy5g/viewform" target="\_blank">5.4.1</a></td>
</tr>
<tr>
<td><strong>5.4.2</strong> <br> Pandas indexing with .iloc and Pandas sampling.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/SIl1oq_KXxU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSeYrZpPD3FLxp67-unm9qv7CZjA89gMBTvA4HaJo7l02zrDkQ/viewform" target="\_blank">5.4.2</a></td>
</tr>
<tr>
<td><strong>5.5.1</strong> <br> Pandas utility functions, properties, and the sort_values method.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/N1BTxLsYE30" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSeklaAVF4eFr8tdXTqFuKeQwSysW0bJxAQCCTyjC4lPmnH4BQ/viewform" target="\_blank">5.5.1</a></td>
</tr>
<tr>
<td><strong>5.5.2</strong> <br> The value_counts and unique methods in Pandas. An exploration of the baby names data set.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/TaUFFW3jB40" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLScK0axm1VZ2hu1gsdh74jfiAjufkFrnge-MNsU8h_rFdaJsRQ/viewform" target="\_blank">5.5.2</a></td>
</tr>
<tr>
