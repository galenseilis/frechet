
!!! warning
	The numbers on this page **are made up** and should *not* be used for any real-world decision.

## The Linda Problem

A [conjunction fallacy](https://en.wikipedia.org/wiki/Conjunction_fallacy) is an inference that the intersection of two or more events are more probable than any event alone.

Amos Tversky and Daniel Kahneman raised awareness of this fallacy in the form of the Linda Problem:

!!! quote
	Linda is 31 years old, single, outspoken, and very bright. She majored in philosophy. As a student, she was deeply concerned with issues of discrimintion and social justice, and also participated in anti-nuclear demonstrations.
	
	Which is more probable?
	
	1. Linda is a bank teller.
	
	2. Linda is a bank teller and is active in the feminist movement.

Purportedly, a non-trivial fraction of study participants asked this question answered `2.` even though it is logically impossible. The Fréchet inequalities guarantee that 

$$Pr\left[ A \cap B \right] \leq Pr[A] Pr[B]$$

for any events $A$ and $B$. This includes the choice of events:

$$A := \text{Linda is a bank teller}$$

and

$$B := \text{Linda is active in the feminist movement}.$$

Suppose that $Pr[A] = \frac{1}{2}$ and $Pr[B] = \frac{19}{20}$ then

$$Pr[A \cap B] \leq \min \left( \frac{1}{2}, \frac{19}{20} \right) = \frac{1}{2}$$

Thus we have shown using a Fréchet inequality that the probability that Linda is a bank teller **and** active in the feminist movement is less-than-or-equal-to the probability of Linda being a bank teller.

That's only the upper bound. We can also surmise using the Frechet inequality for intersections that

$$\max \left(0, Pr[A] + Pr[B] - 1 \right) = \frac{9}{20}  \leq Pr[A \cap B].$$

Taking that $Pr[A \cap B] \in \left[ \frac{9}{20}, \frac{1}{2} \right]$ tells us that the probability of Linda being both a bank teller and being active in the feminist movement is roughly half, whatever it actually is.

## Bad Weather at the Picnic

Suppose you're considering having a picnic next year and you want to consider the probabiliy of "bad weather". Knowing that is pretty vague, you define "bad weather" as being any combination of precipitation (PPT), high winds (HW), or temperatures outside of the interval of [20,30] Celcius (ET). So you would like to know

$$Pr[\text{PPT} \cup \text{HW} \cup \text{ET}]$$

but let's say you are only able to look find the marginal probabilities:

$$Pr[\text{PPT}] = \frac{1}{10}$$

$$Pr[\text{HW}] = \frac{1}{20}$$

$$Pr[\text{ET}] = \frac{1}{30}$$

With the Frechet inequality for unions we can assume

$$\max \left\{ Pr[\text{PPT}], Pr[\text{HW}], Pr[\text{ET}] \right\} = \frac{1}{10} \leq Pr[\text{PPT} \cup \text{HW} \cup \text{ET}]$$

as the lower bound. We can similarly obtain the upper bound to be

$$Pr[\text{PPT} \cup \text{HW} \cup \text{ET}] \leq \min \left(1, Pr[\text{PPT}] +  Pr[\text{HW}] + Pr[\text{ET}]  \right) = \frac{11}{60}.$$

So, with $Pr[\text{PPT} \cup \text{HW} \cup \text{ET}] \in \left[\frac{1}{10}, \frac{11}{60} \right]$, we can roughly say that the percent probability of bad weather on your picnic is 10-20%.

## Genetic Markers Indicating Breast Cancer

Suppose you are given the *per capita* breast cancer rate of your country to be the relative frequency:

$$Pr[\text{Breast Cancer}] = \frac{1}{200}$$

Let us further suppose that breast cancer is more probable given that they have either of the BRCA1 or BRCA2 genes, which have probabilites of 

$$Pr[\text{BRCA1}] = \frac{1}{300}$$

and

$$Pr[\text{BRCA2}] = \frac{1}{400}$$

respectively.

Let us say that the thing we would like to know more about is probability of having cancer given that a person has either of the genetic markers, $Pr[\text{Breast Cancer} \mid \text{BRCA1} \cup \text{BRCA2}]$, but the requisite data is not available to estimate it directly. Instead, we only have those marginal probabilities to work with.

We can compute the bounds on

$$Pr[ \text{BRCA1} \cup \text{BRCA2}]$$ 

as an intermediate step using the Frechet inequalities for the union:


$$\max \left\{ Pr[\text{BRCA1}], Pr[\text{BRCA2}]\right\} = \frac{1}{300} \leq Pr[ \text{BRCA1} \cup \text{BRCA2}]$$

$$ Pr[ \text{BRCA1} \cup \text{BRCA2}] \leq \min \left(1, Pr[\text{BRCA1}] + Pr[\text{BRCA2}]  \right) = \frac{7}{1200}$$

Next we consider the following definition of conditional probability:

$$Pr[A \mid B] = \frac{Pr[A \cap B]}{Pr[B]}$$

## Independence Gap

## Almost-Disjoint Gap
