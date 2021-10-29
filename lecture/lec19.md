---
layout: page
title: Lecture 18 – Cross-Validation and Regularization
nav_exclude: true
---

# Lecture 18 – Cross-Validation and Regularization

Presented by Anthony D. Joseph, Joseph Gonzalez, Suraj Rampure, Paul Shao

Content by Joseph Gonzalez, Suraj Rampure, Paul Shao

- [slides](https://docs.google.com/presentation/d/1UL2ljxgvk8UQnBpkadPCS9-os7f6Iw_X4bXCERGp7HI/edit?usp=sharing)
- [video playlist](https://youtube.com/playlist?list=PLQCcNQgUcDfrhTm0sdDpyYbDhUiqr1vG5)
- [code](https://data100.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/DS-100/fa21&subPath=lec/lec18/&branch=main)

**Important**: Read this before proceeding with the lectures, as it details what materials you should focus on. (This is also largely recapped in Video 18.1.)

Sections 18.1 through 18.4 discuss train-test splits and cross-validation.

18.1, in addition to giving an overview of the lecture, walks through why we need to split our data into train and test in the first place, and how cross-validation works. It primarily consists of slides.
18.2 and 18.3 walk through the process of creating a basic train-test split, and evaluating models that we’ve fit on our training data using our testing data. Code is in “Part 1”.
18.4 walks through the process of implementing cross-validation. In this video there references to a `Pipeline` object in `scikit-learn`. This is **not** in scope for us, so do not worry about its details. Code is in “Part 1”.

Sections 18.5 and 18.6 discuss regularization.

18.5 discusses why we need to regularize, and how penalties on the norm of our parameter vector accomplish this goal.
18.6 explicitly lists the optimal model parameter when using the L2 penalty on our linear model (called “ridge regression”).

There are also three **supplementary** videos accompanying this lecture. They don’t introduce any new material, but may still be helpful for your understanding. They are listed as supplementary and not required since the runtime of this lecture is already quite long. They do not have accompanying Quick Checks for this reason.

18.7 and 18.8 walk through implementing ridge and LASSO regression in a notebook. These videos are helpful in explaining how regularization and cross-validation are used in practice. These videos again use `Pipeline`, which is not in scope. Code is in “Part 2”.
18.9 is another **supplementary** video, created by Paul Shao (a TA for Data 100 in Spring 2020). It gives a great high-level overview of both the bias-variance tradeoff and regularization.

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
<td><strong>18.1</strong> <br />Lecture overview. Training error vs. testing error. Why we need to split our data into train and test. How cross-validation works, and why it is useful.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/y6ZW4nZtlhI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/6CbWjfgNXeJzoDFK7" target="\_blank">18.1</a></td>
</tr>
<tr>
<td><strong>18.2</strong> <br />Using scikit-learn to construct a train-test split.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/_Bzfy7BTjz0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/jx7cQVVfyNh9Pzcy8" target="\_blank">18.2</a></td>
</tr>
<tr>
<td><strong>18.3</strong> <br />Building a linear model and determining its training and test error.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/2i7yj4JhIkw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/QMpoxmNpBhAKUQVn6" target="\_blank">18.3</a></td>
</tr>
<tr>
<td><strong>18.4</strong> <br />Implementing cross-validation, and using it to help select a model.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/m8580Et4pjY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/fA1MgxJomFAawsX87" target="\_blank">18.4</a></td>
</tr>
<tr>
<td><strong>18.5</strong> <br />An overview of regularization.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/NqKtsZpHmRY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/bB91QjoUpvRnBbJN6" target="\_blank">18.5</a></td>
</tr>
<tr>
<td><strong>18.6</strong> <br />Ridge regression and LASSO regression.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/B-labBbXj_c" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a href="https://forms.gle/JBcDvMhis1BzNg7fA" target="\_blank">18.6</a></td>
</tr>
<tr>
<td><strong>18.7</strong> <br />*Supplemental.* Using ridge regression and cross-validation in scikit-learn.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/frdGPG10dOA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a>N/A</a></td>
</tr>
<tr>
<td><strong>18.8</strong> <br />*Supplemental.* Using LASSO regression and cross-validation in scikit-learn.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/hqZNVrZ3flw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a>N/A</a></td>
</tr>
<tr>
<td><strong>18.9</strong> <br />*Supplemental.* An overview of the bias-variance tradeoff, and how it interfaces with regularization.</td>
<td><iframe width="300" height="" src="https://youtube.com/embed/U2J75Iq2nrk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></td>
<td><a>N/A</a></td>
</tr>
</tbody></table>
