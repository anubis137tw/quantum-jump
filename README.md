# Dynamics in Open Quantum System
An open quantum system stands as a captivating frontier, where the details of surrounding environment of the system we are interested is traced over. Unlike closed systems, open quantum systems engage in a perpetual interplay with their surroundings, exchanging energy, information, and entropy. This interplay gives rise to many fascinating phenomena such as decoherence and dissipation, where the delicate quantum coherence of the system is gradually erased due to the fluctuation of the environment. Furthermore, open quantum systems serve as testbeds for studying quantum technologies, unveiling the intricate interplay between quantum mechanics and the macroscopic world. Thus, the study of open quantum systems not only illuminates the fundamental principles of quantum mechanics but also holds the key to unlocking new frontiers in quantum technology and understanding the nature of quantum science. 

## **Introduction**
### **System-bath Model**
The open quantum system can be parameterized by the system-bath model. The relevant degrees of freedom are encoded in the system Hamiltonian $H_S$ while the environment is coarse grained into a phenomenological bath $H_{B}$. The interaction $V$ between the system and its environment allows the system to exchange energy and information to one another.

```math
H=H_S+H_B+V
```

If the interaction between the system and the environment is weak and thus can be treated perturbatively, the dynamics of an open quantum system can be described by a set of time-local markovian quantum master equations. For the populatioin transfer, the general formalism is:

```math
\frac{d}{dt}\sigma_{\alpha\alpha}(t)=\sum_{\beta}\left[k_{\alpha\leftarrow\beta}(t)\sigma_{\beta\beta}(t)-k_{\beta\leftarrow\alpha}(t)\sigma_{\alpha\alpha}(t)\right]
```
For the coherence $\alpha\neq\beta$, the dynamics includes the energy shift, pure dephasing, and population-transfer-induced dephasing. The general formalism is:

```math
\frac{d}{dt}\sigma_{\alpha\beta}(t)=-i\omega_{\alpha\beta}\sigma_{\alpha\beta}(t)-i\Delta_{\alpha\beta}(t)\sigma_{\alpha\beta}(t)-\gamma_{\alpha\beta}^{\mathrm{pd}}(t)\sigma_{\alpha\beta}(t)-\frac{1}{2}\sum_\gamma\left[k_{\alpha\leftarrow\gamma}(t)+k_{\beta\leftarrow\gamma}(t)\right]\sigma_{\alpha\beta}(t)
```

### **Redfield theory**
The quantum master equation for the bosonic bath.
also known as Bloch-Redfield equation, one of the general types of quantum master equations. where treats the system-environment coupling fully perturbatively. The system-bath coupling correlation function encodes the dissipative dynamics of the open system, including the energy shifts, dephasing rates, and population transfer rates.

```math
\Gamma_{\alpha\beta\gamma\delta}(t)=\mathrm{Tr}_B[V_{\alpha\beta}V_{\gamma\delta}(-t)\rho^{eq}_b]
```

```math
\frac{d}{dt}\sigma_{\alpha\beta}(t)=-i\omega_{\alpha\beta} \sigma_{\alpha\beta}(t)+\int_0^t d\tau \left[\Gamma_{\delta\beta\alpha\gamma}(\tau) + \Gamma_{\gamma\alpha\beta\delta}^*(\tau)-\sum_{\epsilon}\left(\Gamma_{\alpha\epsilon\epsilon\gamma}(\tau)\delta_{\beta\delta}+\Gamma^*_{\beta\epsilon\epsilon\delta}(\tau) \delta_{\alpha\gamma}\right)\right]\sigma_{\gamma\delta}(t)
```
### **Coherent Modified Redfield theory**
[paper](https://doi.org/10.1063/1.4905721)[^1][^2]
[^1]: On the accuracy of coherent modified Redfield theory in simulating excitation energy transfer dynamics
[^2]: A coherent modified Redfield theory for excitation energy transfer in molecular aggregates

### **Linblad equation**
The general Linblad form is defined as
```math
\frac{d}{dt}\sigma(t)=-i[H,\sigma(t)]+\frac{1}{2}\sum_k\gamma_{k}(t) \left[2S_k\sigma(t)S^\dagger_k-\{S^\dagger_kS_k,\sigma(t)\}\right]
```
where the dissipative dynamics is controlled by the decay rate $\gamma_k(t)$ for each decay mode $k=(\alpha\leftarrow\beta)$

The Linblad equation can be computed by the quantum jump method.
