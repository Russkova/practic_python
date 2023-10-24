# 1.  Basic concepts of the theory of dynamical systems

Dynamical system - is a mathematical object that represents some real system. System evolutes starting from some initial state

Dynamical system describes real system using system of differential equations
$$\frac{dx_i}{dt} = F(x_i, \lambda)$$
where $\lambda$ are operational parameters
$x_i \in P$; P - __phase space__

Changing state of the system over time is a point movement along trajectory which is called __phase trajectory__

a set $C$ is invariant (w.r.t. system) if for every trajectory $x$, $$x(t) \in C \rightarrow x(\tau) \in C, \forall \tau ≥ t$$
__Attractor__ is a set of states, invariant under dynamics,  towards which neighboring states asymptotically approach in the evolution of dynamic system

__Repeller__ is opposite of an attractor. It is a set of states from which initial states are moving away from it

__Strange attractors__ is a special form of the attractor where initially close points may be exponentially separated after some time.

# 2. Chaotic time series. Fingerprints of chaos
## Definition. Horizon of predictability
Time series (TS) is sequence
$$y_0, y_1, ..., y_t , ..., y_j \in R^n$$
There are two large classes of time series
- _regular_ - simple (unconnected to real world problems)
- _chaotic_ - complicated (real world problems)

How to distinguish?
- using the horizon of predictability

__Def__: Horizon of predictibility - is the number of observation that one is able to predict after one stopped observation

For regular time series the horizon of predictability is theoretically infinite

For chaotic time series the horizon of predictability is finite. Moreover it is possible to calculate it using the time series itself.
## Lyapunov stability and instability
__Lyapunov stability__
The trajectory is called Lyapunov stable if for any $\delta > 0$ there exists $\epsilon(\delta) > 0$ s.t. 
$|X(0) - \tilde{X}(0)| < \delta$ =>
$|X(t) - \tilde{X}(t)| < \epsilon, \forall t > t_0$

__Lyapunov instability__
For any $\delta > 0$ (as small as possible) and for any $E > 0$ (as large as possible) one can find $t=T$ s.t.
$|X(0) - \tilde{X}(0)| < \delta$ =>
$|X(t) - \hat{X}(t)| > E, \forall t > T$

All chaotic time series are Lyapunov Instable
# 3.  Invariant Measure  of a dynamical system. Basic theorems.
## Measures
A measure is $\mu: A \rightarrow R^1$
1) $\mu(A) \geq 0$
2) $\mu(A \cup B) = \mu(A) + \mu(B)$ if $A \cap B = \varnothing$
3) $\mu(0) = 0$

A continious measure:
$\mu(A) = \int_A f(x)dx$

A singular measure is the measure that is neither pointwise, nor continious, nor the combination of them
## Invariant measure intro
Invariant measure is measure that does not change when time shifting trajectory. 

We can divide the phase space into grid and map each grid cell to the portion of time the trajectory is in this cell.
Such portion can be considered as probability

Probability distribution is invariant measure
### The Perron-Frobenius equation
We have
- probability distribution $P(x)$
- transformation $x_{n+1} = f(x_n)$
Then probability distribution (discuissed above) can be represented as
$$P_{n+1}(y) = \int_{R^n} \delta(f(x) - y)P_n(x) dx$$
It is invariant measure because it is not changed by the system (also it is PFE)
## Invariant measure final
Each repeller or attractor produces its own __invariant measure__ (IM)

Any linear combinations of IM is also IM because PFE is linear

__Def__: IM is called ergodic or irreducible if one is unable to represent it as a sum of other IM
Def: IM (ergodic) is called physical if it correspond to attractor.

### Th. Krylov-Bogolubov
For any dynamical system and for any invariant set one may costruct an invariant measure and this measure will be ergodic.
### Th. Poincore
For any $x \in P$ and for any its neighborhood $U$ ($x \in U$) there exists a time $t$ s.t.
$\varphi^t (x) \in U$
(For any $x$ trajectory will always be back)
# 4. Multiplicative ergodic theorem.
Let's imagine that we know exact equation that generates time series
$$x = F(x), x \in R^n$$
One of the solution is $x_0(t)$

We need to linearize the equation
$$x(t) = x_0(t) + u(t) = F(x_0(t) + u(t))=$$
The right side can be expanded to Taylor expansion with respect to $x_0(t)$
$$= F(x_0(t)) + [\frac{\delta f_i}{\delta x_j}|_{x=x_0(t)}] \cdot u(t)$$
__Def__ The Lyapunov exponent is $\lambda = \lim_{t \rightarrow \infty} \frac{\ln || u(t) ||}{t}$
## Multiplicate Ergodic Theorem
There are just n (n - number of equations) possible values of Lyapunov exponent. They collectively are the Lyapunov spectrum. The largest one (the first one) is called Largest Lyapunov Exponent (LLE)
$$ \lambda_1 \geq \lambda_2 \geq ... \geq \lambda_n $$
Hyperchaos is situation when the system has more than one positive LE
# 5. Taken's theorem
Let's consider manifold $M^d$  enveloping the strange attractor in question and the mapping $\Lambda: M^d \rightarrow R^m$ and let's consider a trajectory.

The shift of trajectory is $\varphi^\tau x$
1) $\Lambda, M^d, \varphi^\tau$ is twice differentiable
2) Whitney inequality holds: $m \geq 2 d + 1$
3) For any stationary point and for any cycle of the period $k \tau < d$ the eigen values should be simple (distinct) and not equal to 1

Then $\Lambda$ embeds $M^d$ into $R^m$ (embed = construct 1:1 continuous correspondence (inverse is continuous too))

d-dimensional z-vector is defined as $z_i^{(s)} = (𝑦_𝑖^{(s)} ..., y_{i+d-1}^{(s)})$. They are simply time series observations

If Takens Theorem holds then we have
1) 1:1 correspondence between true (but unknown) dynamics around attractor and untrue (but observable) dynamics. $R^m$ is constructed of z-vectors
2) All calculations estimated using z-vectors are the same as for the true dynamics
3) Let's return $z_i$ to the original space using inverse mapping. There will be $x_i$ which correspond. Using the true dynamics shift it to $x_{i+1} = \varphi^\tau x_i$ with $\tau$ equals to time delta between two measures in TS. After you can use direct mapping to obtain $z_{i+1} = \Lambda(\varphi^\tau \Lambda^{-1} z_i) = \lambda(z_i)$

$y_{i+1} = \lambda_1 (y_i, ..., y_{i-m+1})$, where $y$ is original TS

Conclusion: we can predict. 
# 6. Choosing the parameters of reconstruction
Spoiler: all the proposed methods are just user guides and not strict criterions, so it is not so bad to just brute force the parameters

## Finding $m$ (dimension of embedding space)
Let's $z_i^{(m)}$ and $z_j^{(m)}$ are two close neighbors in reconstruction of size $m$.

$z_i^{(m+1)}$ and $z_j^{(m+1)}$ are corresponding to them in reconstruction of size $m + 1$.

If we deal with "true" nearest neighbors, then they will be close to each other in both reconstructions

In contrary, if we deal with "false" nearest neighbors (FNN), then they will be close in m-dimensional reconstruction, but not close in m+1-dimensional recontruction

Now for each $m$ we can calculate the number of FNN.

For the correct size $\hat{m}$ of reconstruction we will be able to see that count of FNN decreased very significantly
## Finding $\tau$ (the interval between components of z-vectors)
$\tau$ does not directly provide good quality of reconstruction. Actually, the time window $w = (m-1)\tau$ (reconstruction window) affects most. It is the time period between first and last observations in z-vectors.

$\tau$ should not be too small or too big because of distortion

To evaluate effect of small $w$ we can perform estimation of $A_k = O(w^k)$. It is defined by some equation (not very important)
$\sigma(A_k) = ...$

And if this equation is true, then there is effect of small $w$
We can get approximate value of optimal $w$ by solving equation
$\sigma(A_0) = \sigma(A_1)$:
$$w_* = \frac{\sqrt{12} \sigma(x)}{\sigma(\frac{dx}{dt})}$$
$\sigma$ is function used to transform approximate equation for $A_k$ to exact equation

# 7. Horizon of predictability. Largest Lyapunov Exponent. Calculating of the Lyapunov estimate in case of analytically declared systems.
## Horizon of predictability
__Def__: Horizon of predictibility - is the number of observation that one is able to predict after one stopped observation

For regular time series the horizon of predictability is theoretically infinite

For chaotic time series the horizon of predictability is finite. Moreover it is possible to calculate it using the time series itself.
## Lyapunov Exponent
Lyapunov exponents are mathematically defined as the average exponential rate of divergence of nearby pairs of trajectories in phase space. In other words, they tell us how quickly the distance between two points in a system grows.
### Largest Lyapunov exponent
If one denotes $\epsilon(0)$ - initial error, $\epsilon(t)$ - error at point $t$, then $\epsilon(t) = e^{\lambda t}$
$\lambda$ - Largest Lyapunov Exponent (LLE)

If we have some $\epsilon_{max}$ - maximum possible error we can allow
$T = \frac{1}{\lambda} ln(\frac{\epsilon_{max}}{\epsilon(0)})$ - Horizon Of Predictability
## Algorithm
1. We define $n$ orthonormal vectors $v_0^{(i)}$.  We set
 $$\sigma_0^{(i)} = 0, t_0 = 0, u_0^{(i)} = v_0^{(i)}$$
 2. Solve the system $$\dot{x} = F(x), \dot{u}^{(i)} = DF(x)u^{(i)}$$$$x = x(t_k), u = u(t_k)$$
 3. Orthogonalize the system of vectors $u_{k+1}^{(i)}$ and get $\tilde{u}_{k+1}{(i)}$
 4. Calculate $\sigma_{k+1}^{(i)} = \sigma_{k}^{(i)} + \ln ||\tilde{u}_{k+1}^{(i)}||$ and increase $t$: $t_{k+1} = t_k + \Delta t$. Now the current estimate of Lyapunov exponent is $\hat{\lambda}_i(t) = \frac{\sigma_{k+1}^{(i)}}{t_{k+1}}$
 5. Normalize $\tilde{u}_{k+1}{(i)}$: $u_{k+1}^{(i)} = \frac{\tilde{u}_{k+1}^{(i)}}{||\tilde{u}_{k+1}^{(i)}||}$
 6. Repeat 2-5 sufficient amount of times $N$
 7. Get the final estimate as $$\hat{\lambda}_i(t) = \frac{\sigma_{N}^{(i)}}{t_{N}}$$
# 7. Horizon of predictability. Largest Lyapunov Exponent. Calculation of the Lyapunov exponent from a time series. Analog method.
To estimate LLE we need to know the changes of two initially close trajectories

It is proposed to build syntetic trajectory $u(t)$.
The main trajectory is denoted as $z(t)$ and neighboring trajectories as $z_{0i}(t)$
So, $u_i(t) = z_{0i}(t) - z_i(t)$.
Let's also denote $L(t) = ||u_i(t)||$ - length of trajectory

1) At $t_0$ we choose one of the neighboring trajectories $z_{01}(t_0)$ and lets $u(t) = \frac{u_1(t)}{||u_1(t_0)||}$
2) When at some moment $t_1$ the norm $||u_1(t)||$ become very large and we cannot consider the chosen neighboring trajectory as close, we need to rechoose the neighbor.
3) Denote as $L'(t_1)$ - the old length and $L(t_1)$ - the new length
4) We choose the next neighbor $z_{02}(t_1)$, so that the way of vector $u_1(t_1)$ and $u_2(t_1)$ is as close as possible
5) Then for some $t_2$ we again rechoose the neighbor and repeat the steps again

Finally we can estimate LLE as
$$\lambda_1 \approx \frac{1}{t_n - t_0}(\ln \frac{||u_1(t_1)||}{||u_1(t_0)||} + ... + \ln \frac{||u_{j_n}(t_n)||}{||u_{j_n}(t_{n-1})||})$$
# 9. Entropy-complex plain
This plain allws us to know if time series is chaotic or not

We need entropy-complexity plain, so let's define both components:
1) Entropy: $H(p) = \sum_i^N p_i \ln p_i$
2) Complexity: $C(p) = H(p) D(p)$, where $D(p)$ is the euclidian distance between $p = (p_1, ..., p_N)$ and $p_e = (\frac{1}{N}, ..., \frac{1}{N})$

Building points:
1. Let's construct all posible z-vectors
$z_i = (y_i, ..., y_{i+S})$
2. For each $z$ we define its ordinal pattern in this way: 
If $y_i , y_{i+1} \rightarrow y_i = 1$ else  $y_i = 0$
3. Finally we get something like this:
$z_i = (1, 0, 1, 0, 0, ..., 1)$ with length equal to $S - 1$
4. For each ordinal pattern we calculate the probabilty to appear in our TS: $$p(\text{pattern}) = \frac{\text{Number of exactly the same patterns}}{\text{Number of all patterns}}$$
5. We get probability distribution $p_1, ..., p_N$ of different unique patterns
6. Using this probabilities we can calculate $H(p)$ and $C(p)$
7. This two values produce a point on entropy-complexity plain. If this point is on the top of plain. We can say that we are dealing with chaotic TS

# 10. Kolmogorov-Sinai entropy: series, information. Generalized entropies.
_Def._ 
1) Lets divide space into sets $A_{i_1}$, where $diam A_{i_1} < \epsilon$
2) Define $A_{i_1 i_2} = A_{i_1} \cap f^{-1}(A_{i_2})$ ($x_{n+1} = f(x_n)$)
3) $A_{i_1 i_2 i_3} = A_{i_1} \cap f^{-1}(A_{i_2}) \cap f^{-2}(A_{i_3})$
4) k-step: $A_{i_1 i_2 ... i_k} = A_{i_1} \cap f^{-1}(A_{i_2}) ... \cap f^{-(k+1)}(A_{i_s})$

$H(k) = - \sum_{i_1 ... i_k} \mu (A_{i_1 ... i_k}) \ln\mu (A_{i_1 ... i_k})$, $\mu$ - invariant measure of dynamical system in question

If $\epsilon = \max_i diam A_i$ then 
KS - entropy: $KS = lim_{\epsilon \rightarrow 0} lim_{k \rightarrow \infty} [H(k+1) - H(k)] = lim_{\epsilon \rightarrow 0} lim_{k \rightarrow \infty} [H(k)/k]$
For a chaotic TS is $KS > 0$, for regular it is equal to zero
Chaotic system generate information with KS speed
### The generalized entropy or Renyi entropy
Used in complex systems where conventional Shanon entropy does not work

Renyi entropy: $$H_q = \frac{1}{1-q} ln \sum_{i=1}^n p_i^q, q \in (-\infty, +\infty)$$
if $q$ limits to $1$ then $H_q$ limits to conventional Shannon entropy
$$H_1 = \lim_{\gamma \rightarrow 0} - \frac{1}{\gamma} \ln \sum_{i=1}^n p_i p_i^\gamma = \lim_{\gamma \rightarrow 0} - \frac{1}{\gamma} \ln \sum_{i=1}^n p_i e^{\gamma \ln p_i} = $$
$$= \lim_{\gamma \rightarrow 0} - \frac{1}{\gamma} \ln [1 + \gamma \sum_{i=1}^n p_i \ln p_i] = - \sum_{i=1}^n p_i \ln p_i$$
One can calculate generalized Renyi for any q.
# 11. Prediction based on clustering.
## Prediction algo
Effective for multi-step ahead prediction

Termins:
1) `motifs` - typical sequences that occur repeatedly in a series with small variations

Preprocess TS:
- normalize
- make it stationary

Two params of algo for creating patterns
- K - max length between points in pattern
- L - length of pattern series

Generate motives from patterns:
- do not use clusters (return pure values of samples according to pattern)
- use clustering and just use centres of clusters

For each pattern we should do following:
- get set of samples for pattern
- calculate distance between current motive and generate ones
- create set of predictions by adding all values that have distance less than eps

Having set of predictions we can get single predictions using:
- mode
- mean
- weighted mean
- center of biggest dbscan cluster

Adding non-predictable points
- check if IQR is more than threshold
- using dbscan
	- large + lots of small - OK
	- two or more approx equal values - NONOK

Making predictions with non-predictable points
- exclude all patterns where these points are included relatively current which we want to predict
## Wishard clustering algorithm
Suppose we have already added $i$ elements of sampl and have already constructed a partial graph $G_i = <V_i, E_i>$. 

Moreover we have already placed all this first i-th elements to the respective clusters by labeling them $w(x_i) = q$
where $q$ is the number of cluster it belongs. If $q = 0$, then $x_i$ belongs to the intercluster noise

We add the i + 1 element and extend the set of vertices $V_{i+1} = V_i \cup (x_{i+1})$
and extend the set of edges by adding all edges s.t. $d(x_{i+1}, x_j) < d_k(x_j)$

What is $w(x_{i+1})$?
#### First option
$x_{i+1}$ is isolated (we haven't connected it to the graph). That means we should create new cluster and add new element to it.
#### Second option
$x_{i+1}$ is not isolated and connected to the elements from the same class, then 
1) If class is not formed, then we just add new point to this class
2) If class is already formed, label it as $0$ (zero)
#### Third option
There are several classes it is connected to $l_1, l_2, l_p$ then
Let $\zeta(h)$ be a number of h-significant classes among $l_1, l_2, l_p (l_1 < l_2 < ... < l_p)$
1) If $l_1$ > 0 and $\zeta(h) = 1$ (only single) then we destroy all other clusters and relabel them and add newly added point to this class
2) $l_1 = 0$ and $\zeta(h) > 1$. We make all significant classes formed, we destroy all non-significant clusters, label the elements as noise (0) and label $x_{i+1}$ as noise two
### Advantages
- no need to know the number of clusters
### Drawbacks
- hard calculations
- lots of elements become noise
# 12 . Dimensions of strange attractors and their computation.
#### Lebegue dimension
$d_T$

$d_T(\emptyset) = -1$
If one has two sets A and B, one can define the border between them as an intersection of $С \cap D$ . $A \in C, B \in D$

Space is n-dimensional if for any two sets in this one can find a border between them of no more than n dimensions

#### Hawsford dimension
$d_H$

Let's divide n-dimensional set into two subsets with diameter less than $\epsilon$ and let us consider all possible separation of this kind, then Hawsford sum is defined as:
$m(\epsilon, p) = \inf_{\{A_i\}} \sum_i (diam A_i)^p$
$d_H = \sup_p \{0 < m(\epsilon, p)  < +\infty\}$

___
Fractals are geometrical objects s.t. $d_T < d_H$ and regular shape are objects s.t. $d_T = d_H$

Attractors of any chaotic TS are fractals




