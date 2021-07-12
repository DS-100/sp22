---
layout: page
title: Lecture 16 – Bias and Variance
nav_exclude: true
---

# Lecture 16 – Bias and Variance

Presented by Joey Gonzalez, Andrew Bray, Fernando Perez, and Ani Adhikari


- [slides](https://docs.google.com/presentation/d/15LDeDKNxpIa9j0_dHZr1F5AzrbVEUoM5OWOxgqYUKM0/edit?usp=sharing)
- 15.5 slides ([1](../../resources/assets/lectures/lec15/decomposing-mse-wide.html), [2](../../resources/assets/lectures/lec15/decomposing-mse-square.html))
- [video playlist](https://www.youtube.com/playlist?list=PLQCcNQgUcDfpsM-s0xEnuVScBP3i_9bMs)
- [Introduction to Overfitting](../../resources/assets/lectures/lec15/IntroductionToOverfitting.html)
- [Bias-Variance decomposition derivation](../../resources/assets/lectures/lec15/lec15-bias-variance-derivation.html) ([raw](https://data100.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/DS-100/sp21&subPath=lecture/lec15/))

**Important:** The algebra behind the decomposition of model risk into observational variance, model variance, and bias, is not in the slides or video but is in the link above. You should read it **after** watching this lecture. Also, you may want to review [Lecture 3](http://ds100.org/fa20/lecture/lec03) for a refresher on random variables.


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
<td><strong>15.0</strong> <br> Weekly Overview. </td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/YYKP33-fcNo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td></td>
</tr>
<tr>
<td><strong>15.1</strong> <br> A quick Introduction to Overfitting and Generalization. </td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/14YGCOq37yg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td>Coming soon</td>
</tr>
<tr>
<td><strong>15.2</strong> <br> Variance of random variables. Walking through an alternate calculation of variance. Variance of a linear transformation. </td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/3W_TtAHxlXQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSeU8a1bVqVtvu82Opw4n3dNlvLpP5JPx6gy6JH1tPFHCAFCJg/viewform" target="\_blank">15.2</a></td>
</tr>


<!-- <tr>
<td><strong>15.2</strong> <br> Deriving the variance of a sum. Understanding covariance, correlation, and independence. </td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/8ovh_lGuMdQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSewRWkZ5vOLbO7zoQbPkiSlkcHJk9s3BW-aBJUpMPyPH9v2Xg/viewform" target="\_blank">15.2</a></td>
</tr>


<tr>
<td><strong>15.3</strong> <br> Variance of an i.i.d. sum. Variance of the Bernoulli and binomial distributions. </td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/t4gPC6LDS1c" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfvnzx2LeTC4EKK72KEf9LHVhQkuSKsUJuUyCrMbWl9WZ7bRg/viewform" target="\_blank">15.3</a></td>
</tr>
<tr>
<td><strong>15.4</strong> <br> Variability of the sample mean. Reviewing inferential concepts from Data 8, but with the framework of random variables. </td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/CwXhjoBt25I" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSce8iejVjmHjlJGUjbw7mbskFVvqDzS6XFe9VZ_c6_DsL_BRw/viewform" target="\_blank">15.4</a></td>
</tr>
 -->

<tr>
<td><strong>15.3</strong> <br>Introducing the data generating process and prediction error. Model risk.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/mPz-jIl9H7s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSewQ5vHKA30nkeESdbiCKISmafTtOCurxw1fmpNvd0a3jCi5A/viewform" target="\_blank">15.3</a></td>
</tr>

<!-- <tr>
<td><strong>15.6</strong> <br>Looking at different sources of error in our model – observation variance, model variance, and bias – and discussing how to mitigate them.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/mmjYEOeOEM4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSegBG0lw56mX_iiJBLGe7VfT5Hz3b0aVppPuSgcWzDsXliMCQ/viewform" target="\_blank">15.6</a></td>
</tr>
 -->
<tr>
<td><strong>15.4</strong> <br>Components of the Prediction Error.</td>
<td><iframe width="300" height="500" height src="https://youtube.com/embed/sktUKDB4Zfc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSesORFx-WhNSODExsb5k_32E0AOYEVqxiOcrarQjyKE75Xyrg/viewform" target="\_blank">15.4</a></td>
</tr>

<tr>
<td><strong>15.5</strong> <br>Visualizing Bias and Variance.</td>
<td><iframe width="300" height="500" height src="https://youtube.com/embed/lKMjFxdMhTQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td>Coming Soon</td>
</tr>


<tr>
<td><strong>15.6</strong> <br>Model Complexity and the Bias Variance Tradeoff.</td>
<td><iframe width="300" height="500" height src="https://youtube.com/embed/a1zMueoMVpw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td>Coming Soon</td>
</tr>
