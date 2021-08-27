---
layout: page
title: Lecture 10 – Visualization, Part 2
nav_exclude: true
---

# Lecture 10 – Visualization, Part 2

Presented by Fernando Pérez

Content by Fernando Pérez, Suraj Rampure, Ani Adhikari, Sam Lau, Yifan Wu, Deborah Nolan

- [slides](https://docs.google.com/presentation/d/16l3XLseFMJIhoPZXuQSXogCpob9htZ9TEEEgAXlHDtw/edit?usp=sharing)
- [video playlist](https://www.youtube.com/playlist?list=PLQCcNQgUcDfrmwSHwEnaHuDC88OzQ3s0g)
- [code](https://github.com/DS-100/su21/tree/main/lec/lec10) ([launch](https://data100.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/DS-100/su21&subPath=lec/lec10/&branch=main))
- [code HTML](../../resources/assets/lectures/lec10/lec10.html)

Extra reading on colormaps:

- [matplotlib colormaps (BIDS)](https://bids.github.io/colormap/)
- [How the Rainbow Color Map Misleads](https://eagereyes.org/basics/rainbow-color-map)
- [When to use Sequential and Diverging Palettes](https://everydayanalytics.ca/2017/03/when-to-use-sequential-and-diverging-palettes.html)
- [Color Use Guidelines](https://web.natur.cuni.cz/~langhamr/lectures/vtfg1/mapinfo_2/barvy/colors.html)

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
<td><strong>10.0</strong> <br>Introduction.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/lPjgccaoG7I" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td></td>
</tr>
<tr>
<tr>
<td><strong>10.1</strong> <br>Ensuring that the axes in our visualizations aren't misleading.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/WKcm52yif6s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSeby6pIjBbTvpep8Ix9IA7qKrZtkS392_i0gNJqzinbnedQzw/viewform?usp=sf_link" target="\_blank">10.1</a></td>
</tr>
<tr>
<td><strong>10.2</strong> <br>Designing visualizations that are well-suited for making comparisons.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/giFxDyTFUfg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSd6rgf5na9Crs2smuMQsCQIFO4HLKhdK8rDfn8YkxKCEB5utw/viewform?usp=sf_link" target="\_blank">10.2</a></td>
</tr>
<tr>
<td><strong>10.3</strong> <br>How to use color to create effective visualizations. How to choose color schemes that are clear and accessible.</td>
<td><iframe width="300" height="500" height src="https://youtube.com/embed/TgQZ3NrfKEY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSchasXZG2jm3-CVCQLQo3wXY7OTPa9-g9ISvpQoT8m6l6mmkg/viewform?usp=sf_link" target="\_blank">10.3</a></td>
</tr>
<tr>
<td><strong>10.4</strong> <br>How to choose markings that the human eye can easily interpret. Issues to avoid, such as jiggling baselines and overplotting.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/0kpwp4AXLM8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSdy7Zx8ecIjNqeMqodfy_x5mRzq_u1PoNdU49TfIwlddaa5lw/viewform?usp=sf_link" target="\_blank">10.4</a></td>
</tr>
<tr>
<td><strong>10.5</strong> <br>Discussing the supplemental text that publication-ready plots need.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/dcQuKORSfyQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSeEX8XbuxDIi0YZI1ZdOc4k86cQEUw7LYpmdyUR-dpcWo9BMA/viewform?usp=sf_link" target="\_blank">10.5</a></td>
</tr>
<tr>
<td><strong>10.6</strong> <br>When to use smoothing. How kernel density estimates are created. Looking at various kernels. Understanding the impact of the bandwidth hyperparameter.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/sZxvb4LvcLU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSei3y8XCJ_v1QM8Dww-npW4EXwLnVF8CNRUMI4RSMfDv7NWqw/viewform?usp=sf_link" target="\_blank">10.6</a></td>
</tr>
<tr>
<td><strong>10.7</strong> <br>Discussing why we prefer linear relationships. Understanding how to "reverse-engineer" a linearized relationship to determine the true relationship. Identifying which transformations to use in order to linearize a relationship.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/zA-Cy887CXM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSdQzRY7c2GWnUViTQjYy-YnUOgVd9O3lahHcwhX6N8gIT3OOw/viewform?usp=sf_link" target="\_blank">10.7</a></td>
</tr>
