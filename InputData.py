POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1         # years (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03
PSA_ON = False
# transition matrix
TRANS_MATRIX = [
    [0.75,  0.15,   0.0,    0.1],   # Well
    [0,     0.0,    1.0,    0.0],   # Stroke
    [0,     0.25,   0.55,   0.2],   # Post-Stroke
    [0.0,   0.0,    0.0,    1.0],   # Dead
    ]

# anticoagulation relative risk in reducing stroke incidence and stroke death while in “Post-Stroke”
RR_STROKE = 0.65
# anticoagulation relative risk in increasing mortality due to bleeding is 1.05.
RR_BLEEDING = 1.05


# annual cost of each health state
ANNUAL_STATE_COST = [
    0.0,   # well
    5000.0,   # stroke
    200.0    # post
    ]

# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    1,   # well
    0.8865,   # stroke
    0.9    # poststroke
    ]

# annual drug costs
NONE_COST = 0
ANTICOG_COST = 2000

# treatment relative risk
#TREATMENT_RR = 0.509
#TREATMENT_RR_CI = 0.365, 0.71  # lower 95% CI, upper 95% CI

# annual probability of background mortality (number per year per 1,000 population)
#ANNUAL_PROB_BACKGROUND_MORT = 8.15 / 1000


