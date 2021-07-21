---
layout: page
title: Lecture 17 – Cross-Validation and Regularization
nav_exclude: true
---

# Lecture 17 – Cross-Validation and Regularization

Presented by Isaac Schmidt, Paul Shao

Content by Isaac Schmidt, Joseph Gonzalez, Suraj Rampure, Paul Shao

- [slides](https://docs.google.com/presentation/d/1i4XmSfcBALeeJ3LaQjCGYOUt_mYHRBdpMHQFsxUCskM/edit?usp=sharing)
- [video playlist](https://www.youtube.com/playlist?list=PLQCcNQgUcDfrIBZQ24xuw2741XBoUX58J)
- [code](https://data100.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/DS-100/su21&subPath=lec/lec17/&branch=main)
- [code HTML](../../resources/assets/lectures/lec17/lec17.html)

17.8 is a **supplementary** video, created by Paul Shao. It gives a great high-level overview of both the bias-variance tradeoff and regularization. **The instructors highly recommend this video.**

**Note:** The demos in this lecture were adapted from demos that Prof. Joeys Gonzalez recorded in Spring 2020. We decided to redo them as the originals significantly rely on sklearn's `Pipeline` object, which is not in scope this semester. However, these notebooks are still available to you, in case you wish to use this style of code for your own projects.
- code HTML: ([Part 1](../../resources/assets/lectures/lec17/lec17-alt-1.html), [Part 2](../../resources/assets/lectures/lec17/lec17-alt-2.html))

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
<td><strong>16.1</strong> <br>Lecture overview. Training error vs. testing error. Why we need to split our data into train and test. How cross-validation works, and why it is useful.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/y6ZW4nZtlhI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSeyzg8cTdWXADSk5Ki7EVaOm1h5R_V2iqTfg5Ozv481YRdt4Q/viewform" target="\_blank">16.1</a></td>
</tr>
<tr>
<td><strong>16.2</strong> <br>Using scikit-learn to construct a train-test split.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/_Bzfy7BTjz0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSeRph43oLp3hAmD5uH42BMquAoeGAQeey6XCaLsEbUsEZItzg/viewform" target="\_blank">16.2</a></td>
</tr>
<tr>
<td><strong>16.3</strong> <br>Building a linear model and determining its training and test error.</td>
<td><iframe width="300" height="500" height src="https://youtube.com/embed/2i7yj4JhIkw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSdRetxoBG08ztF3RUrodibq7N1DzOVkT9AHIkKVNflnkStFNA/viewform" target="\_blank">16.3</a></td>
</tr>
<tr>
<td><strong>16.4</strong> <br>Implementing cross-validation, and using it to help select a model.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/m8580Et4pjY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfi_PiJCgRsdzrI9vwyRKHUV5B37WZfaEh0u6HA-che0Ii3-w/viewform" target="\_blank">16.4</a></td>
</tr>
<tr>
<td><strong>16.5</strong> <br>An overview of regularization.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/NqKtsZpHmRY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfEckJSRCSCkVz_JxGhrf2MtcctLWcT9NBMQFtF3GGcRIRvVw/viewform" target="\_blank">16.5</a></td>
</tr>
<tr>
<td><strong>16.6</strong> <br>Ridge regression and LASSO regression.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/B-labBbXj_c" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfz0-SU11o_wgeIUmIoV7VKtCNgwm4WZVrXU-WWsBwPxekIlg/viewform" target="\_blank">16.6</a></td>
</tr>
<tr>
<td><strong>16.7</strong> <br>*Supplemental.* Using ridge regression and cross-validation in scikit-learn.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/frdGPG10dOA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a>N/A</a></td>
</tr>
<tr>
<td><strong>16.8</strong> <br>*Supplemental.* Using LASSO regression and cross-validation in scikit-learn.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/hqZNVrZ3flw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a>N/A</a></td>
</tr>
<tr>
<td><strong>16.9</strong> <br>*Supplemental.* An overview of the bias-variance tradeoff, and how it interfaces with regularization.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/U2J75Iq2nrk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a>N/A</a></td>
</tr>
