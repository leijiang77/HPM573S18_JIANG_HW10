import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

# create and cohort
cohort = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.ANTICOAG)

simOutputs = cohort.simulate()


cohort2 = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE)

simOutputs2 = cohort2.simulate()

#Problem1
print("Problem1")
# print outcomes (means and CIs)
SupportMarkov.print_outcomes(simOutputs2, 'No treatment:')
SupportMarkov.print_outcomes(simOutputs, 'Anticoagulation:')

