---
layout: page
title: Lecture 9 – Visualization, Part 1
nav_exclude: true
---

# Lecture 9 – Visualization, Part 1

Presented by Fernando Perez

Content by Fernando Perez, Suraj Rampure, Ani Adhikari, Sam Lau, Yifan Wu

- [slides](https://docs.google.com/presentation/d/1r1zyItUSM7mmoF26-sPrVIg_m21BCx0TMVetdaSLtdQ/edit)
- [video playlist](https://www.youtube.com/playlist?list=PLQCcNQgUcDfpopjZVuLlvwriC_mABCfYi)
- [code](https://github.com/DS-100/su21/tree/main/lec/lec09) ([launch](https://data100.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/DS-100/su21&subPath=lec/lec09/&branch=main))
- [code HTML](../../resources/assets/lectures/lec09/lec09.html)

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
<td><strong>9.0</strong> <br>Announcements.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/YhXQMzZ5dpg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td></td>
</tr>
<tr>
<td><strong>9.1</strong> <br>Formal definition of visualization. The purpose of visualization in the data science lifecycle.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/jJEEYES-Drw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSepkekJbWvZuZ-aUCSR-dthFEWV8E37gbRUPWnwvvfk5WYLFQ/viewform?usp=sf_link" target="\_blank">9.1</a></td>
</tr>
<tr>
<td><strong>9.2</strong> <br>Different ways we can map from data to properties of a visualization.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/6cly3iD2B64" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSdWHGC4em0i_i_tL-3YCurymhEntQYPCFYe-5HMihnvR7SOiQ/viewform?usp=sf_link" target="\_blank">9.2</a></td>
</tr>
<tr>
<td><strong>9.3</strong> <br>Defining distributions, and determining whether or not given visualizations contain a distribution.</td>
<td><iframe width="300" height="500" height src="https://youtube.com/embed/7DaEWbSdBd4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSf-ARbF5oSVP6544DRUJQKclLCap9xcIx6cB_pJ0Po7e57jIA/viewform?usp=sf_link" target="\_blank">9.3</a></td>
</tr>
<tr>
<td><strong>9.4</strong> <br>Bar plots as a means of displaying the distribution of a qualitative variable, as well as for plotting a quantitative variable across several different categories.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/-uclH1gmwuE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSdxt72F5QDqvzVeC8IZ4IQjXFweZz8np6wgzoDBJJV6TS1Cag/viewform?usp=sf_link" target="\_blank">9.4</a></td>
</tr>
<tr>
<td><strong>9.5</strong> <br>Rug plots. Histograms, where areas are proportions. Reviewing histogram calculations from Data 8. Density curves as smoothed versions of histograms.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/j2cGxJTXask" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLScNFx_9Th9d1Ho3jxsOrJ16qQQ3DjxtLo4Agm21aEj8TKDZlw/viewform?usp=sf_link" target="\_blank">9.5</a></td>
</tr>
<tr>
<td><strong>9.6</strong> <br>Describing distributions of quantitative variables using terms such as modes, skew, tails, and outliers.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/XyVFj_ckvFg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfQN6qNCOHixf2U2B2qgYtw5orI05KraQ61eQlqoY2CsvVZ1A/viewform?usp=sf_link" target="\_blank">9.6</a></td>
</tr>
<tr>
<td><strong>9.7</strong> <br>Using box plots and violin plots to visualize quantitative distributions. Using overlaid histograms and density curves, and side by side box plots and violin plots, to compare multiple quantitative distributions.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/oGHNoTcJy6M" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSc24n1fpVNy6E6IzjWSnFzu6Cj9qhGyvZ6zPgYKUQNEOcEA4g/viewform?usp=sf_link" target="\_blank">9.7</a></td>
</tr>
<tr>
<td><strong>9.8</strong> <br>Using scatter plots, hex plots, and contour plots to visualize the relationship between pairs of quantitative variables. Summary of visualization thus far.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/s-dRmP_8zd0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLScbJ8CX6Bsot7mbhFVdRQ6hDhvQwfW-xNMHd2QapFX_w4y-8A/viewform?usp=sf_link" target="\_blank">9.8</a></td>
</tr>
