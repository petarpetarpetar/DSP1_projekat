/**************************************************************
WinFilter version 0.8
http://www.winfilter.20m.com
akundert@hotmail.com

Filter type: Low Pass
Filter model: Rectangular Window
Sampling Frequency: 48 KHz
Cut Frequency: 0.650000 KHz
Coefficents Quantization: 16-bit
***************************************************************/
#define Ntap 35

#define DCgain 524288

Int16 lowpass_34th_order_650hz[Ntap] = {
        12425,
        12850,
        13257,
        13645,
        14011,
        14356,
        14677,
        14974,
        15246,
        15492,
        15711,
        15902,
        16065,
        16199,
        16304,
        16379,
        16424,
        16439,
        16424,
        16379,
        16304,
        16199,
        16065,
        15902,
        15711,
        15492,
        15246,
        14974,
        14677,
        14356,
        14011,
        13645,
        13257,
        12850,
        12425
};
