There are two such inequalities. One for the intersection of events, and the other for the union of events.

$$ \begin{align} \max \left( 0, \sum_{k=1}^n Pr[A_k] - (n-1) \right) \leq &  Pr \left[ \bigcap_{k=1}^n A_k \right] \leq &  \min_k \left\{ Pr[A_k] \right\}  \\
\max \left\{ Pr(A_k) \right\} \leq &  Pr \left[ \bigcup_{k=1}^n A_k \right] \leq &  \min \left( 1, \sum_{k=1}^n Pr[A_k] \right) \end{align} $$

??? info "To Conjoin, or to Intersect, That is the Operator"
	
	You may have noticed that we use the symbols $\cap$ and $\cup$ instead of $\land$ and $\lor$. In many cases they can be used interchangeably without incident, however we prefer the set-theoretic notation. However, formal [probability theory](https://en.wikipedia.org/wiki/Probability_space) does not directly have a conjunction operator on sets.

Here is a public domain image of Maurice Frechet.

![](assets/Frechet.jpeg) 

