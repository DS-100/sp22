---
layout: page
title: Lecture 13 – Gradient Descent, Feature Engineering
nav_exclude: true
---

# Lecture 13 – Gradient Descent, Feature Engineering

Presented by Josh Hug and Joseph Gonzalez

Content by Josh Hug and Joseph Gonzalez

- [slides](https://docs.google.com/presentation/d/1tfdoQR-iit3KnxA1SjNd7V70ErNBJTGMfvqxH4BfMik/edit#slide=id.g116a5f99ddb_0_11){:target="_blank"}
- [code](https://github.com/DS-100/sp22/blob/main/lec/lec13/lec13.ipynb){:target="_blank"} ([lauch](https://data100.datahub.berkeley.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FDS-100%2Fsp22&branch=main&urlpath=lab%2Ftree%2Fsp22%2Flec%2Flec13%2Flec13.ipynb){:target="_blank"})
- [code HTML](../../resources/assets/lectures/lec13/lec13.html){:target="_blank"}
- [code for video 6](https://github.com/DS-100/sp22/blob/main/lec/lec13/fitting-linear-models.ipynb){:target="_blank"} ([lauch](https://data100.datahub.berkeley.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FDS-100%2Fsp22&branch=main&urlpath=lab%2Ftree%2Fsp22%2Flec%2Flec13%2Ffitting-linear-models.ipynb){:target="_blank"})
- [code for video 6 HTML](../../resources/assets/lectures/lec13/fitting-linear-models.html){:target="_blank"}
- [video playlist](https://www.youtube.com/watch?v=3QDyVfe7Tks&list=PLQCcNQgUcDfqQOBZbRKTy4mwEtykpa9O9){:target="_blank"}

<!--A reminder – the right column of the table below contains _Quick Checks_. These are **not** required but suggested to help you check your understanding.

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
<td><strong>13.0</strong> <br />Introduction and recap of the modeling process.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/TXWx4v5MGm8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/Kd1tcSUC6v3pkggr8" target="\_blank">13.0</a></td>
</tr>
<tr>
<td><strong>13.1</strong> <br />The correlation coefficient and its properties.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/vo9ey0DL1nk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/xYLtaMuqCKeD2smh8" target="\_blank">13.1</a></td>
</tr>
<tr>
<td><strong>13.2</strong> <br />Defining the simple linear regression model, our first model with two parameters and an input variable. Motivating linear regression with the graph of averages.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/crDa6Y34r3A" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/KTA7Zf2HMAxMxif3A" target="\_blank">13.2</a></td>
</tr>
<tr>
<td><strong>13.3</strong> <br />Using calculus to derive the optimal model parameters for the simple linear regression model, when we choose squared loss as our loss function.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/7hVK78Ir618" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/41AcdfSYC3hD1eep6" target="\_blank">13.3</a></td>
</tr>
<tr>
<td><strong>13.4</strong> <br />Visualizing and interpreting loss surface of the SLR model.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/K3e19T_Z9JU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/awcr1eWvrdLHSp3AA" target="\_blank">13.4</a></td>
</tr>
<tr>
<td><strong>13.5</strong> <br />Interpreting the slope of the simple linear model. </td>
<td><iframe width="300" height="" src="https://youtube.com/embed/dKI_lDXDzvI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/MgVFCjvNfPS12Z4x5" target="\_blank">13.5</a></td>
</tr>
<tr>
<td><strong>13.6</strong> <br />Defining key terminology in the regression context. Expanding the simple linear model to include any number of features.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/LHbuY63Bh_0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/FeZTqtgxhba6dEZK7" target="\_blank">13.6</a></td>
</tr>
<tr>
<td><strong>13.7</strong> <br />RMSE as a metric of accuracy. Multiple R-squared as a metric of explained variation. Summary.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/1jLglngUYUM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/mpZz3JGZjWhTP7599" target="\_blank">13.7</a></td>
</tr>
</tbody>
</table>
-->