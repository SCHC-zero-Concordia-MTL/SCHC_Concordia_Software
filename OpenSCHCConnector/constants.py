from enum import IntEnum
class RegionalParameters:
    VER = "1.0.2"
    pass
class DataRates(IntEnum):
    DR0 = 0
    DR1 = 1
    DR2 = 2
    DR3 = 3
    DR4 = 4
    DR5 = 5
    DR6 = 6
    DR7 = 7
    DR8 = 8
    DR9 = 9
    DR10 = 10
    DR11 = 11
    DR12 = 12
    DR13 = 13
    DR14 = 14
    DR15 = 15

class SpreadingFactors(IntEnum):
    SF0 = 0
    SF1 = 1
    SF2 = 2
    SF3 = 3
    SF4 = 4
    SF5 = 5
    SF6 = 6
    SF7 = 7
    SF8 = 8
    SF9 = 9
    SF10 = 10
    SF11 = 11
    SF12 = 12

class US915(RegionalParameters):
    
    # MTU_M with no repeater
    MTU_M = \
    {
        DataRates.DR0: 19,
        DataRates.DR1: 61,
        DataRates.DR2: 133,
        DataRates.DR3: 250,
        DataRates.DR4: 250,
        DataRates.DR5: None,
        DataRates.DR6: None,
        DataRates.DR7: None,
        DataRates.DR8: 61,
        DataRates.DR9: 137,
        DataRates.DR10: 250,
        DataRates.DR11: 250,
        DataRates.DR12: 250,
        DataRates.DR13: 250,
        DataRates.DR14: None,
        DataRates.DR15: None,
    }

    DR_SF_MAP = \
    {
        DataRates.DR0: [SpreadingFactors.SF10, 125],
        DataRates.DR1: [SpreadingFactors.SF9, 125],
        DataRates.DR2: [SpreadingFactors.SF8, 125],
        DataRates.DR3: [SpreadingFactors.SF7, 125],
        DataRates.DR4: [SpreadingFactors.SF8, 500],
        DataRates.DR5: None,
        DataRates.DR6: None,
        DataRates.DR7: None,
        DataRates.DR8: [SpreadingFactors.SF12, 500],
        DataRates.DR9: [SpreadingFactors.SF11, 500],
        DataRates.DR10: [SpreadingFactors.SF10, 500],
        DataRates.DR11: [SpreadingFactors.SF9, 500],
        DataRates.DR12: [SpreadingFactors.SF8, 500],
        DataRates.DR13: [SpreadingFactors.SF7, 500],
        DataRates.DR14: None,
        DataRates.DR15: None,
    }


