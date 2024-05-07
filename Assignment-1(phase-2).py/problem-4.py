def future_gain_from_improvement(a_s_profit, i_c_rate, c_c_rate, EPL, i_cost):
    numerator = a_s_profit * (i_c_rate / c_c_rate)
    denominator = (1 / (0.05 - (i_cost * (1 + 0.05) ** EPL)))
    return int(numerator - (a_s_profit * (((1 + 0.05) ** EPL) - 1)) * denominator)

def total_gain_from_improvement(fgfi, epl):
    return fgfi / (1 + 0.05) ** epl

def annual_gain_from_improvement(tgfi, epl):
    return tgfi / epl

def annual_ROI(agfi, icost):
    return agfi / icost

def total_ROI(tgfi, icost):
    return tgfi / icost

def input_values():
    asp = int(input("Enter Annual Site Profit: "))
    icr = float(int(input("Enter Improved Conversion Rate (in %): ")) / 100)
    ccr = float(int(input("Enter Current Conversion Rate (in %): ")) / 100)
    epl = int(input("Enter Expected Project Life (in Years): "))
    ic = int(input("Enter Improvement Cost: "))
    return asp, icr, ccr, epl, ic

def calculate_ROI():
    asp, icr, ccr, epl, ic = input_values()
    
    fgfi = future_gain_from_improvement(asp, icr, ccr, epl, ic)
    tgfi = total_gain_from_improvement(fgfi, epl)
    agfi = annual_gain_from_improvement(tgfi, epl)
    a_roi = annual_ROI(agfi, ic)
    t_roi = total_ROI(tgfi, ic)
    
    print("\n * Defination of all the Terms *")
    print("|\t1. Annual Site Profit : An amount of money that you gain when you are paid more for something than it cost you to before the annual contribution margin.")
    print("|\t2. Improvement Conversion Rate : More of your site traffic converts to meaningful actions that grow your business")
    print("|\t3. Current Conversion Rate : The average number of conversions per ad interaction, shown as a percentage")
    print("|\t4. EPL : Expected Project life")
    print("|\t5. Improvement Cost : Costs of the design, permitting, construction and installation of the Improvements")
    print("*")
    print(f"\nFuture Gain from Improvement: {round(fgfi, 2)}")
    print(f"Total Gain from Improvement: {round(tgfi, 2)}")
    print(f"Annual Gain from Improvement: {round(agfi, 2)}")
    print(f"Annual ROI: {round(a_roi, 2)}")
    print(f"\nTotal ROI: {round(t_roi)}")

calculate_ROI()