---
layout: page
title: Lecture 21 – Classification and Logistic Regression I
nav_exclude: true
---

# Lecture 21 – Classification and Logistic Regression I

Presented by Lisa Yan

<!-- Content by Lisa Yan, Josh Hug, John DeNero, Sam Lau, and Suraj Rampure -->

- [slides](https://docs.google.com/presentation/d/1p1XQ6q57uJ46QjkUGA8N6RgmynSJFzxWw2tUR5j_ceo/edit#slide=id.g10ed28599e7_0_0){:target="_blank"}
- [code](https://github.com/DS-100/sp22/blob/main/lec/lec21/lec21.ipynb){:target="_blank"} ([launch](https://data100.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/DS-100/sp22&subPath=lec/lec21/){:target="_blank"})
- [code HTML](../../resources/assets/lectures/lec21/lec21.html){:target="_blank"}
- [recording](https://youtu.be/ZeWQRESmxV8){:target="_blank"}
- [supplemental video on MLE Derivation](https://youtu.be/jwXbZ6QnQmA){:target="_blank"}

<!--
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
<td><strong>22.1</strong> <br />Dimensionality. Visualizing high-dimensional data.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/cRKHiaYAH8w" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/kbP5dMQZsUVr7Bhq6" target="\_blank">22.1</a></td>
</tr>
<tr>
<td><strong>22.2</strong> <br />More visualizations of high-dimensional data.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/joE5rVir8uc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/1kDnLCvbgoBgvJxQ6" target="\_blank">22.2</a></td>
</tr>
<tr>
<td><strong>22.3</strong> <br />Matrix decomposition, redundancy, and rank. Introduction to the singular value decomposition (SVD).</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/rFuyMgD6Z5Y" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/gqU3J7mta5fpavP87" target="\_blank">22.3</a></td>
</tr>
<tr>
<td><strong>22.4</strong> <br />The theory behind the singular value decomposition. Orthogonality and orthonormality.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/e9QDPdWa9NI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/vFfz9PYN5pPdqvVH6" target="\_blank">22.4</a></td>
</tr>
<tr>
<td><strong>22.5</strong> <br />Definition and computation of principal components. Geometric interpretation of principal components and low rank approximations. Data centering.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/UuPBTEnd4GU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/pDoQ7sTjQ81ZWhdK6" target="\_blank">22.5</a></td>
</tr>
<tr>
<td><strong>22.6</strong> <br />Interpretation of singular values. The relationship between singular values and variance. Analyzing scree plots.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/TsaIkauTsuM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/gVGctERYp6CCG3aU8" target="\_blank">22.6</a></td>
</tr>
<tr>
<td><strong>22.7</strong> <br />Introduction to principal Component analysis (PCA). PCA for exploratory data analysis.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/0JHaGBT0hmY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/LNKVEmBVd63TFpWT9" target="\_blank">22.7</a></td>
</tr>
</tbody></table>
-->
