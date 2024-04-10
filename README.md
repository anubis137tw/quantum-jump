# Dynamics in Open Quantum System
An open quantum system stands as a captivating frontier, where the details of surrounding environment of the system we are interested is traced over. Unlike closed systems, open quantum systems engage in a perpetual interplay with their surroundings, exchanging energy, information, and entropy. This interplay gives rise to many fascinating phenomena such as decoherence and dissipation, where the delicate quantum coherence of the system is gradually erased due to the fluctuation of the environment. Furthermore, open quantum systems serve as testbeds for studying quantum technologies, unveiling the intricate interplay between quantum mechanics and the macroscopic world. Thus, the study of open quantum systems not only illuminates the fundamental principles of quantum mechanics but also holds the key to unlocking new frontiers in quantum technology and understanding the nature of quantum science. 

## System-bath Model
The open quantum system can be parameterized by the system-bath model. The relevant degrees of freedom are encoded in the system Hamiltonian $H_S$ while the environment is coarse grained into a phenomenological bath $H_{B}$. The interaction $V$ between the system and its environment allows the system to exchange energy and information to one another.

```math
H=H_S+H_B+V
```

If the interaction between the system and the environment is weak and thus can be treated perturbatively, the dynamics of an open quantum system can be described by the quantum master equation where the general formalism is:

```math
\frac{d}{dt}\sigma_{\alpha\beta}(t)=-i\omega_{\alpha\beta} \sigma_{\alpha\beta}(t)+\int_0^t d\tau \left[\Gamma_{\delta\beta\alpha\gamma}(\tau) + \Gamma_{\gamma\alpha\beta\delta}^*(\tau)-\sum_{\epsilon}\left(\Gamma_{\alpha\epsilon\epsilon\gamma}(\tau)\delta_{\beta\delta}+\Gamma^*_{\beta\epsilon\epsilon\delta}(\tau) \delta_{\alpha\gamma}\right)\right]\sigma_{\gamma\delta}(t)
```
where the system-bath coupling correlation function encodes the dissipative dynamics of the open system
```math
\Gamma_{\alpha\beta\gamma\delta}(t)=\mathrm{Tr}_B[V_{\alpha\beta}V_{\gamma\delta}(-t)\rho^{eq}_b]
```

## Redfield theory

## Linblad equation
