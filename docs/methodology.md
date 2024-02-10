## Background

There are two such inequalities. One for the intersection of events, and the other for the union of events.

$$ \begin{align} \max \left( 0, \sum_{k=1}^n Pr[A_k] - (n-1) \right) \leq &  Pr \left[ \bigcap_{k=1}^n A_k \right] \leq &  \min_k \left\{ Pr[A_k] \right\}  \\
\max \left\{ Pr(A_k) \right\} \leq &  Pr \left[ \bigcup_{k=1}^n A_k \right] \leq &  \min \left( 1, \sum_{k=1}^n Pr[A_k] \right) \end{align} $$

??? info "To Conjoin, or to Intersect, That is the Operator"
	
	You may have noticed that we use the symbols $\cap$ and $\cup$ instead of $\land$ and $\lor$. In many cases they can be used interchangeably without incident, however we prefer the set-theoretic notation. However, formal [probability theory](https://en.wikipedia.org/wiki/Probability_space) does not directly have a conjunction operator on sets.

Here is a public domain image of Maurice Frechet.

![](assets/Frechet.jpeg) 

## Intersections & Unions

## Independence Gap

??? abstract
	The independence gap quantifies statistical dependence. The Fréchet inequalities allow us to put lower and upper bounds on how much statistical independence there could be given only the marginal probabilities. Those bounds can also be used to normalize the independence gap onto the interval $[-1,1]$.

The independence gap was conceived of sometime between asking [*A formal definition of a "measure of association"*](https://stats.stackexchange.com/q/534454/69508) and posting [this answer](https://stats.stackexchange.com/a/589235/69508) to that question. The independence gap was originally conceived of in terms of cumulative distribution functions, but fortunately [Sextus Empiricus](https://stats.stackexchange.com/users/164061/sextus-empiricus) readily generalized it to events from any probability space in [their answer](https://stats.stackexchange.com/a/623001/69508) to the question: [*Is the pairwise independence gap bounded to $\left[-\frac{1}{4},\frac{1}{4}\right]$? What about for n variables?*](https://stats.stackexchange.com/q/622983/69508)

We can take the independence gap for a collection of events $E_1, \ldots, E_n$ from a suitable probability space $(\Omega, \mathcal{F}, P)$ to be

$$\phi[E_1, \ldots, E_k] \triangleq Pr\left[ \bigcap_{k=1}^n E_{k}  \right] - \prod_{k=1}^n Pr[E_k].$$

Regarding the [definition of statistical independence on a collection of events](https://en.wikipedia.org/wiki/Independence_(probability_theory)#More_than_two_events) for such a probability space is when the equality

$$Pr\left[ \bigcap_{k=1}^n E_{k}  \right] = \prod_{k=1}^n Pr[E_k]$$

holds, it should be clear that the independence gap quantifies statistical independence directly from its definition. 

When the independence gap is zero then events are statistically independent. When the independence gap is positive it means that the joint probability is greater than what would be expected had the events been independent. When the independence gap is negative is means that the joint probability is less than what would have been expected had the events been statistically independent.

??? failure "Ruling Out Independence"
	One might naïvely hope or expect that the bounds bounds could be used to rule out statistical independence, but that is not possible. The bounds will always cover zero.

## Almost-Disjoint Gap

??? abstract
	The almost-disjoint gap quantifies how close a collection of events are to being disjoint (i.e. mutually exclusive). The Fréchet inequalities provide bounds which can be used to produce a normalize score.

In [*Can we obtain a probability interpretation on these bounds obtained from the ADG and Frechet inequalities?*](https://stats.stackexchange.com/q/623136/69508) I defined and discussed the almost-disjoint gap (ADG) as follows:

!!! quote
	The **almost-disjoint gap** (ADG) is given by

	$$\mathcal{D}_{\mu} \left( E_1, \ldots, E_n \right) \triangleq \mu \left( \bigcup_{k=1}^{n} E_k \right) - \sum_{k=1}^n \mu \left( E_k \right)$$

	where $\mu$ is a measure and $\{ E_k \}_{k=1}^n$ are elements of a suitable $\sigma$-algebra. When the ADG equals zero we know that the events are [almost everywhere](https://en.wikipedia.org/wiki/Almost_everywhere) [pairwise disjoint](https://en.wikipedia.org/wiki/Disjoint_sets). 

	The [IE principle](https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle) (for probabilities, just to skip general measure) states that 

	$$P\left( \bigcup_{k=1}^n E_k \right) = \underbrace{\sum_{k=1}^n P(E_k)}_{\text{Marginal Terms}} +  \underbrace{\sum_{k=2}^n \left((-1)^{k-1} \sum_{\substack{I \subseteq \{1, \ldots, n \} \\ |I| = k}} P\left(\bigcap_{i \in I} E_i \right) \right)}_{\text{Joint Terms}}$$

	where I have labelled what I call the *marginal terms* and *joint terms* in under braces. This tells us directly what the meaning of the ADG is: the joint terms.

	$$\mathcal{D}_{P} \left( E_1, \ldots, E_n \right) = \underbrace{\sum_{k=2}^n \left((-1)^{k-1} \sum_{\substack{I \subseteq \{1, \ldots, n \} \\ |I| = k}} P\left(\bigcap_{i \in I} E_i \right) \right)}_{\text{Joint Terms}}$$


	The Frechet bounds for the probability of a union given the marginal probabilities is given by

	$$\max \{ P(E_k) \} \leq P\left( \bigcup_{k=1}^{n} E_k \right) \leq \min \left(1, \sum_{k=1}^n P(E_k) \right).$$

	The ADG and Frechet bound together can be used to create bounds on the ADG when the marginal probabilities are given.

	$$\max \{ P(E_k) \} - \sum_{k=1}^n P \left( E_k \right) \leq \mathcal{D}_{P} \left( E_1, \ldots, E_n \right) \leq \min \left(1, \sum_{k=1}^n P(E_k) \right) - \sum_{k=1}^n P \left( E_k \right)$$

	Even not knowing the marginal probabilities we know the most extreme bounds for the ADG can be written in terms of the number of events.

	$$1 - n \leq \mathcal{D}_{P} \left( E_1, \ldots, E_n \right) \leq 0$$

I further commented on the bounds implying a normalization:

!!! quote
	Noting that $1-n \leq 0$, we can flip the bounds by multiplying by negative one:

	$$0 \leq -\mathcal{D}_{P} \left( E_1, \ldots, E_n \right) \leq n-1.$$

	And since $n-1$ will sometimes be greater than 1 we can divide through by $n-1$ to normalize:

	$$0 \leq \frac{-\mathcal{D}_{P} \left( E_1, \ldots, E_n \right)}{n-1} \leq 1$$

## Applications

The primary applications for data analysis are when the appropriate summary statistics are available but the raw data is not available.

## Design 

Frechet is designed to work with minimal dependencies. Because the primary use case is to work with summary statistics, dealing with truly "big data" is not part of the design scope. Therefore there are no special packages or language extensions used in Frechet.

??? question "Is Fréchet Compatible With PyPy?"
	Fréchet seems to work with PyPy, but this is not a supported compatibility.
