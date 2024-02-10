
!!! warning
	The numbers on this page **are made up** and should *not* be used for any real-world decision.

# The Linda Problem

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

# Genetic Markers

Suppose you are given the *per capita* breast cancer rate of your country to be the relative frequency:

$$f_{\text{Breast Cancer}} = \hat Pr[\text{Breast Cancer}] = \frac{1}{200}$$

Let us further suppose that breast cancer is more probable given that they have either of the BRCA1 or BRCA2 genes, which have probabilites of 

$$Pr[\text{BRCA1}] = \frac{1}{300}$$

and

$$Pr[\text{BRCA2}] = \frac{1}{400}$$

respectively.

Let us say that the thing we would like to know more about is probability of having cancer given that a person has either of the genetic markers, $Pr[\text{Breast Cancer} \mid \text{BRCA1} \cup \text{BRCA2}]$, but the requisite data is not available to estimate it directly. Instead, we only have those marginal probabilities to work with.
