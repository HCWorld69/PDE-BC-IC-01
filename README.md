# PDE-BC-IC-01

Pytorch implementation for fluid PDE problem with boundary conditions

(∂u_z)/∂t=v 1/r  ∂/∂r (r (∂u_z)/∂r)-1/ρ  ∂p/∂z
where v is the kinematic viscosity and ρ is the density of the fluid. The position along the radius of the blood vessel is measured by r. The pressure gradient oscillates in time with frequency, ω(rad/s), to simulate the pumping action of the heart:
-∂p/∂z=Δp/L cos⁡(ωt)
The initial and boundary conditions for this problem are as follows:
Initial condition:
t=0□( ) u_z=u_z0
Boundary conditions: □( ) t>0□( ) r=0□( )  (∂u_z)/∂r=0□( ) u_z is finite
r=R□( ) u_z=0
The following constants may be used for the solution of this problem. These are characteristic of the human left main artery, human blood, and heart pumping action:
■(&R=0.425" " cm□( ) V=0.09〖" " cm〗^2/s□( ) ρ=1" " g/cm^3@&ω=3" cycles per second " =6πrad/s@&Δp/L=1" dyne " /cm^3=1(" g.cm " /s^2 )/cm^3 )
