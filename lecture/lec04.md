---
layout: page
title: Lecture 4 – Pandas, Part 1
nav_exclude: true
---

# Lecture 4 - Pandas, Part 1

Presented by Fernando Perez

Content by Fernando Perez, Josh Hug

- [slides](https://docs.google.com/presentation/d/16ZeSryn94sL5u3PHQXveTGFvcVpu0qZcF73nbFFX59c/edit?usp=sharing)
- [video playlist](https://www.youtube.com/playlist?list=PLQCcNQgUcDfoD7vMjUf5r-VsDv5FyXqTj)
- [code](https://github.com/DS-100/su21/tree/main/lec/lec04) ([launch](https://data100.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/DS-100/su21&subPath=lec/lec04/&branch=main))
- [code HTML](../../resources/assets/lectures/lec04/lec04.html)
- [Intro to Pandas if you’ve taken Data 8 (zip)](https://github.com/DS-100/su21/raw/main/lec/lec04/pandas_for_data8_students.zip)
- [Prof. Hug's Pandas I Lecture Materials](https://ds100.org/su20/lecture/lec5/)

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
<td><strong>4.0</strong> <br>Introduction</td>
<td><iframe width="300" height="300" height src="https://www.youtube.com/embed/P14Pv_S4Bb0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td></td>
</tr>
<tr>
<td><strong>4.1.1</strong> <br> Pandas data frames, series, and indices.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/VWa5J1GDHgE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSedKbvsAE-Jz2NjnmgYle6_28Q7LDk50jub4hcVO76vY57rmw/viewform" target="\_blank">4.1.1</a></td>
</tr>
<tr>
<td><strong>4.1.2</strong> <br> Pandas indices demo.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/ZhK5CRbJ9co" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSc9GqQ6gpCTTR3k3Z8sXmjNPN9oAM-g0HnEAxEgT95jF96MDg/viewform" target="\_blank">4.1.2</a></td>
</tr>
<tr>
<td><strong>4.2</strong> <br> Pandas indexing with the bracket operator.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/J5pN8YFacfU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfE3LFgGsAxEfZymiUlE7L9vbFIuPFkfJHAinDVZ1HwAu_hPg/viewform" target="\_blank">4.2</a></td>
</tr>
<tr>
<td><strong>4.3</strong> <br> Pandas boolean array selection, the isin function, and the query command.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/DaL2ekf-sls" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfeBfLKDdzHHpACdCzLrYTmvpsR3uu2JOyb7N7AZFFFq7lhHw/viewform" target="\_blank">4.3</a></td>
</tr>
<tr>
<td><strong>4.4.1</strong> <br> Pandas indexing with .loc.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/_nvnW7I2N2g" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSccPdHccc1WHNnEQ4aeGN95-efhkDyD6dspdzGJmI0rvqvlkw/viewform" target="\_blank">4.4.1</a></td>
</tr>
<tr>
<td><strong>4.4.2</strong> <br> Pandas indexing with .iloc and Pandas sampling.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/SIl1oq_KXxU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSflTRJbrw4oIQBeUEhl92wUvx1tSPvyAPLbrVgH2Ap1TPDDEw/viewform" target="\_blank">4.4.2</a></td>
</tr>
<tr>
<td><strong>5.5.1</strong> <br> Pandas utility functions, properties, and the sort_values method.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/N1BTxLsYE30" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfwTgp95sAVQObZsXlJytA4RiWNqwUvdonhubn1RusDiaXQzw/viewform" target="\_blank">4.5.1</a></td>
</tr>
<tr>
<td><strong>4.5.2</strong> <br> The value_counts and unique methods in Pandas. An exploration of the baby names data set.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/TaUFFW3jB40" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLScMd9qIcT55y9RpkSHCcdbAJH57pdqY6YMwl_6MKLrTrjyIew/viewform" target="\_blank">4.5.2</a></td>
</tr>
<tr>
