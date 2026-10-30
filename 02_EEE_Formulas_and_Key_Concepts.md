# EEE কোর ডিপার্টমেন্টাল ফর্মুলা শিট (BUET Pattern High-Yield Formulas)

বুয়েটের লিখিত পরীক্ষায় দ্রুত ম্যাথ সলভ করার জন্য নিচের সূত্রগুলো মুখস্থ এবং ঠোঁটস্থ থাকা আবশ্যক।

---

## ১. ইলেকট্রিক্যাল সার্কিট (Electrical Circuits)

### ক. থিভনিন ও ম্যাক্সিমাম পাওয়ার ট্রান্সফার (Thevenin & MPT)
* ডিসি সার্কিটের ক্ষেত্রে ম্যাক্সিমাম পাওয়ার স্থানান্তরের শর্ত:
  $$R_L = R_{th}$$
* সর্বোচ্চ পাওয়ার:
  $$P_{max} = \frac{V_{th}^2}{4 R_{th}}$$
* এসি সার্কিটের ক্ষেত্রে:
  $$Z_L = Z_{th}^* \quad (\text{Complex Conjugate})$$
  $$P_{max} = \frac{|V_{th}|^2}{4 R_{th}}$$

### খ. এসি পাওয়ার ও থ্রি-ফেজ পাওয়ার (AC & 3-Phase Power)
* সিঙ্গেল ফেজ পাওয়ার:
  * রিয়েল পাওয়ার (Real Power): $P = V_{rms} I_{rms} \cos \theta \quad [\text{W বা kW}]$
  * রিঅ্যাক্টিভ পাওয়ার (Reactive Power): $Q = V_{rms} I_{rms} \sin \theta \quad [\text{VAR বা kVAR}]$
  * অ্যাপারেন্ট পাওয়ার (Apparent Power): $S = V_{rms} I_{rms}^* = P + jQ \quad [\text{VA বা kVA}]$
  * পাওয়ার ফ্যাক্টর: $\text{pf} = \cos \theta = \frac{P}{|S|}$
* থ্রি-ফেজ ব্যালান্সড লোড:
  * $P = \sqrt{3} V_L I_L \cos \theta = 3 V_{ph} I_{ph} \cos \theta$
  * স্টার ($\text{Y}$) সংযোগ: $V_L = \sqrt{3} V_{ph} \angle 30^\circ, \quad I_L = I_{ph}$
  * ডেল্টা ($\Delta$) সংযোগ: $V_L = V_{ph}, \quad I_L = \sqrt{3} I_{ph} \angle -30^\circ$

### গ. ট্রানজিয়েন্ট টাইম কনস্ট্যান্ট (Transients)
* $RC$ সার্কিটের টাইম কনস্ট্যান্ট: $\tau = R C$
* $RL$ সার্কিটের টাইম কনস্ট্যান্ট: $\tau = \frac{L}{R}$

---

## ২. ইলেকট্রিক্যাল মেশিন (Electrical Machines)

### ক. ট্রান্সফরমার (Transformer)
* ট্রান্সফরমেশন রেশিও:
  $$\frac{V_1}{V_2} = \frac{N_1}{N_2} = \frac{I_2}{I_1} = a$$
* সেকেন্ডারির সাপেক্ষে সমতুল্য রেজিস্ট্যান্স:
  $$R_{02} = R_2 + R_1' = R_2 + \frac{R_1}{a^2}$$
* ভোল্টেজ রেগুলেশন (Voltage Regulation):
  $$\%VR = \frac{V_{NL} - V_{FL}}{V_{FL}} \times 100\% \approx \frac{I_2 R_{02} \cos \theta_2 \pm I_2 X_{02} \sin \theta_2}{V_2} \times 100\%$$
  *(+ চিহ্ন ল্যাগিং পাওয়ার ফ্যাক্টরের জন্য, - চিহ্ন লিডিংয়ের জন্য)*
* সর্বোচ্চ দক্ষতার শর্ত (Condition for Maximum Efficiency):
  $$\text{Iron Loss } (P_i) = \text{Copper Loss } (P_{cu})$$
  সর্বোচ্চ দক্ষতার ফ্র্যাকশনাল লোড: $x = \sqrt{\frac{P_i}{P_{cu, FL}}}$

### খ. ইন্ডাকশন মোটর (Induction Motor)
* সিনক্রোনাস স্পিড: $N_s = \frac{120 f}{P}$ [RPM]
* স্লিপ (Slip): $s = \frac{N_s - N_r}{N_s}$
* রোটর ফ্রিকোয়েন্সি: $f_r = s \cdot f$
* পাওয়ার ফ্লো অনুপাত (সবচেয়ে বেশি আসা ম্যাথ):
  $$P_{gap} : P_{cu, rotor} : P_{mech} = 1 : s : (1 - s)$$
  * Rotor Copper Loss: $P_{cu} = s \cdot P_{gap}$
  * Developed Mechanical Power: $P_{mech} = (1 - s) \cdot P_{gap}$

### গ. ডিসি মেশিন (DC Motor / Generator)
* ব্যাক ইএমএফ / জেনারেটেড ইএমএফ:
  $$E = \frac{\Phi Z N P}{60 A}$$
  *(ল্যাপ ওয়াইন্ডিংয়ে $A = P$, ওয়েভ ওয়াইন্ডিংয়ে $A = 2$)*
* ডিসি মোটর সমীকরণ: $V = E_b + I_a R_a$
* টর্ক: $T \propto \Phi I_a$

---

## ৩. ইলেকট্রনিক্স (Electronics - Op-Amp)

বুয়েটে অপ-অ্যাম্প থেকে প্রতি পরীক্ষায় প্রশ্ন থাকে।
* **ইনভার্টিং অ্যাম্প্লিফায়ার (Inverting Amplifier):**
  $$V_{out} = -\frac{R_f}{R_{in}} V_{in}$$
* **নন-ইনভার্টিং অ্যাম্প্লিফায়ার (Non-Inverting Amplifier):**
  $$V_{out} = \left(1 + \frac{R_f}{R_{in}}\right) V_{in}$$
* **সামিং অ্যাম্প্লিফায়ার (Summing Amplifier):**
  $$V_{out} = -\left(\frac{R_f}{R_1} V_1 + \frac{R_f}{R_2} V_2 + \frac{R_f}{R_3} V_3\right)$$
* **ইন্টিগ্রেটর (Integrator):**
  $$V_{out} = -\frac{1}{R C} \int_0^t V_{in} \, dt$$
* **ডিফারেনশিয়েটর (Differentiator):**
  $$V_{out} = -R C \frac{d V_{in}}{dt}$$

---

## ৪. পাওয়ার সিস্টেম (Power Systems)

### ক. পার-ইউনিট সিস্টেম (Per-Unit System)
* বেস ইম্পিডেন্স:
  $$Z_{base} = \frac{(V_{base, LL, kV})^2}{S_{base, 3\phi, MVA}} \quad [\Omega]$$
* নতুন বেসে পার-ইউনিট মান পরিবর্তন:
  $$Z_{pu}^{new} = Z_{pu}^{old} \times \left(\frac{V_{base}^{old}}{V_{base}^{new}}\right)^2 \times \left(\frac{S_{base}^{new}}{S_{base}^{old}}\right)$$

### খ. ফল্ট ক্যালকুলেশন (Fault Calculation)
* ফল্ট কারেন্ট (Symmetrical):
  $$I_{f, pu} = \frac{1.0}{X_{th, pu}}$$
  $$I_{f, actual} = I_{f, pu} \times I_{base}$$
* শর্ট সার্কিট MVA:
  $$\text{SC MVA} = \frac{\text{Base MVA}}{X_{th, pu}}$$
