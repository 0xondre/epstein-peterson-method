## Epstein-Peterson method
This method evaluates the diffraction loss over a series of obstacles by treating them as a combination of knife-edge diffractions. It considers the geometry and position of the obstacles relative to the line of sight (LOS) between neighbouring obstacles/transmitter/receiver.
Formulas used in this implementation:

$$ℎ_𝑘=(𝐻_𝑘−𝐻_{𝑘−1})−\frac{𝑑_𝑘*(𝐻_{𝑘+1}−𝐻_{𝑘−1})}{𝑑_𝑘+𝑑_{𝑘+1}}$$
$$𝑣_𝑘=ℎ_𝑘*\sqrt{\frac{2∗(𝑑_𝑘+𝑑_{𝑘+1}}{λ∗𝑑_𝑘∗𝑑_{𝑘+1}}}$$
$$𝐴_{𝑑𝐵}(𝑀_𝑘)=6.9+20∗𝐿𝑜𝑔(\sqrt{(𝑣_𝑘−0.1)^2+1}+𝑣_𝑘−0.1)$$
$$,for \ 𝑣_𝑘≻−0.78$$
$$𝐴_{𝑑𝐵}=∑_{𝑘=1}^𝑁(𝐴_{𝑑𝐵}(𝑀_𝑘))$$


$ℎ_𝑘$ - height of the obstruction above LOS  
$𝑑_𝑘$ - distance from the next obstruction  
$𝑣_𝑘$ - Fresnel-Kirchhoff parameter  
$𝐴_{𝑑𝐵}(𝑀_𝑘)$ - diffraction loss for obstruction  
$𝐴_{𝑑𝐵}$ - total diffraction loss  
$𝐻_𝑘$ - height AMSL (above mean sea level)  
$λ$ - wavelength of the signal  
