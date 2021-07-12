---
layout: page
title: Lecture 13 – Ordinary Least Squares
nav_exclude: true
---

# Lecture 13 – Ordinary Least Squares

Presented by Suraj Rampure, Andrew Bray

Content by Joey Gonzalez, Suraj Rampure, Ani Adhikari, Deb Nolan

- [slides](https://docs.google.com/presentation/d/165f1_eaalRAsZZI79IGgSdpRdEuV8u9bPrzDQGv5R-k/edit?usp=sharing)
- [video playlist](https://www.youtube.com/playlist?list=PLQCcNQgUcDforMNM7CkHqgrMAfuau3BIA)
- [code](https://data100.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/DS-100/su21&subPath=lec/lec13/)
- [code HTML](../../resources/assets/lectures/lec13/lec13.html)

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
<td><strong>13.0</strong> <br>Introduction.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/lQ9ZK72zkzg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td></td>
</tr>
<tr>
<td><strong>13.1</strong> <br>A quick recap of the modeling process, and a roadmap for lecture.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/qL_enPmtwk8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLScMPMjPelv72qZ0M_mJ6h_T2kUWZbWF16a6L-YuBS-qp5TGug/viewform?usp=sf_link" target="\_blank">13.1</a></td>
</tr>
<tr>
<td><strong>13.2</strong> <br>Defining the multiple linear regression model using linear algebra (dot products and matrix multiplication). Introducing the idea of a design matrix.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/oGIPhLtVb6k" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLScyvNS0odURTvCobEpYveEyUwhaw0t4A9UggGW7p64T_PUWKg/viewform?usp=sf_link" target="\_blank">13.2</a></td>
</tr>
<tr>
<td><strong>13.3</strong> <br>Defining the mean squared error of the multiple linear regression model as the (scaled) norm of the residual vector.</td>
<td><iframe width="300" height="500" height src="https://youtube.com/embed/odY5eSwJ02w" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSftKQMn3hHIvGDAaT72wLdFTm9x81t2ZrrAKU_aIRJzHc5x4w/viewform?usp=sf_link" target="\_blank">13.3</a></td>
</tr>
<tr>
<td><strong>13.4</strong> <br>Using a geometric argument to determine the optimal model parameter.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/nkLUTatnK0s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSf4lyCJJ1fXoWFqSU6UwZ8yQGN-isTH8GWqq4dI1iO9uXt3xg/viewform?usp=sf_link" target="\_blank">13.4</a></td>
</tr>
<tr>
<td><strong>13.5</strong> <br>Residual plots. Properties of residuals, with and without an intercept term in our model.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/lT_gzva-dKg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSd78OrksVXNM6rYmFeMyES77o-aLuAsOlVzYVoAFZiTepns4Q/viewform?usp=sf_link" target="\_blank">13.5</a></td>
</tr>
<tr>
<td><strong>13.6</strong> <br>Discussing the conditions in which there isn't a unique solution for the optimal model parameter. A summary, and outline of what is to come.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/9e_w8up-8Yc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSe1cZ8t1TFyM3zCHlLQl1R0y7rHNtqiLqgSvt8uw_bRzOK2Ew/viewform?usp=sf_link" target="\_blank">13.6</a></td>
</tr>
<tr>
<td><strong>13.7 [EXTRA]</strong> <br>A case study demonstrating the descriptive capacity of a MLR model.</td>
<td><iframe width="300" height="300" height src="https://www.youtube.com/embed/fvdgLgAl4_k" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td></td>
</tr>
</tbody>
</table>
