---
layout: page
title: Lecture 23 – Principal Components Analysis
nav_exclude: true
---

# Lecture 23 – Principal Components Analysis

Presented by Anthony D. Joseph

Content by Josh Hug, John DeNero, Sam Lau, and Suraj Rampure

- [slides](https://docs.google.com/presentation/d/1mk9g45VZP8U-9cLCke72aPB1Ve1D8LvpKsPX2Ix-VX4/edit?usp=sharing)
- [video playlist](https://www.youtube.com/playlist?list=PLQCcNQgUcDfqbh1ZwcC11OXL3eYklOeSk)
- [code](https://data100.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/DS-100/fa20&subPath=lecture/lec22/)
- [code HTML](../../resources/assets/lectures/lec22/lec22.html)
- [Summer 2020 notes on PCA](http://www.ds100.org/su20/resources/assets/lectures/live07/live7.pdf)
- [(Optional) PCA tutorial](https://arxiv.org/pdf/1404.1100.pdf)

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
<td><strong>23.0</strong> <br>Announcements.</td>
<td><iframe width="300" height="300" height src="https://www.youtube.com/embed/9Ta6KBGNoIk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td></td>
</tr>
<tr>
<td><strong>23.1</strong> <br>Dimensionality. Visualizing high-dimensional data.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/cRKHiaYAH8w" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSc-cMTc05Jv9cvU2EnCa13iaSJ-Vc57j6hA0K5EMxunyGEwZA/viewform" target="\_blank">23.1</a></td>
</tr>
<tr>
<td><strong>23.2</strong> <br>More visualizations of high-dimensional data.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/joE5rVir8uc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSdkR56J3KPQZqh5qBfYbOK_ca2Iy9Klr-3D6n33zyBDWQrL-Q/viewform" target="\_blank">23.2</a></td>
</tr>
<tr>
<td><strong>23.3</strong> <br>Matrix decomposition, redundancy, and rank. Introduction to the singular value decomposition (SVD).</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/rFuyMgD6Z5Y" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfOrnulBMvI042vrwUh5n9mzHrMKfnd9imWVBWE8HOcHCkzNw/viewform" target="\_blank">23.3</a></td>
</tr>
<tr>
<td><strong>23.4</strong> <br>The theory behind the singular value decomposition. Orthogonality and orthonormality.</td>
<td><iframe width="300" height="500" height src="https://youtube.com/embed/e9QDPdWa9NI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfyjk9RqFaBdqayZBKQKJ2P1h58L01toYZce0_RSbAoa3fRUw/viewform" target="\_blank">23.4</a></td>
</tr>
<tr>
<td><strong>23.5</strong> <br>Definition and computation of principal components. Geometric interpretation of principal components and low rank approximations. Data centering.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/UuPBTEnd4GU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLScw_fww3v5Fows5sIU7uMfpXz4IM-m74NoOzYbvcBScKg7qZA/viewform" target="\_blank">23.5</a></td>
</tr>
<tr>
<td><strong>23.6</strong> <br>Interpretation of singular values. The relationship between singular values and variance. Analyzing scree plots.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/TsaIkauTsuM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSc9hzkBYU3bxppA59vClSct91iS53cp7fONsWo0vXGoJ4qChg/viewform" target="\_blank">23.6</a></td>
</tr>
<tr>
<td><strong>23.7</strong> <br>Introduction to principal Component analysis (PCA). PCA for exploratory data analysis.</td>
<td><iframe width="300" height="500" height src="https://youtube.com/embed/0JHaGBT0hmY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfl_hhXt33Ao7kG6yBx_u3eJoh8SJAY8eOpSu5RkLwvbJvT3Q/viewform" target="\_blank">23.7</a></td>
</tr>
