//////////////////////////////////////////////////////////////////////////////
// * File name: main.c
// *                                                                          
// * Description:  Main function.
// *                                                                          
// * Copyright (C) 2011 Texas Instruments Incorporated - http://www.ti.com/ 
// * Copyright (C) 2011 Spectrum Digital, Incorporated
// *                                                                          
// *                                                                          
// *                                                                          
//////////////////////////////////////////////////////////////////////////////

#include "stdio.h"
#include "ezdsp5535.h"
#include "ezdsp5535_i2c.h"
#include "aic3204.h"
#include "ezdsp5535_aic3204_dma.h"
#include "ezdsp5535_i2s.h"
#include "WAVheader.h"
#include "fir.h"
#include "low_pass_34th_order_650hz.h"

static WAV_HEADER outputWAVhdr;
static WAV_HEADER inputWAVhdr;

#define SAMPLE_RATE 48000L
#define GAIN 0
#define ARRAY_SIZE(x) ((sizeof x) / (sizeof *x))

#pragma DATA_ALIGN(InputBufferL,4)
Int16 InputBufferL[AUDIO_IO_SIZE];
#pragma DATA_ALIGN(InputBufferR,4)
Int16 InputBufferR[AUDIO_IO_SIZE];

#pragma DATA_ALIGN(OutputBufferL,4)
Int16 OutputBufferL[AUDIO_IO_SIZE];
#pragma DATA_ALIGN(OutputBufferR,4)
Int16 OutputBufferR[AUDIO_IO_SIZE];

Uint16 state1 = 0;
Int16 history1[35];

Uint16 state2 = 0;
Int16 history2[121];

/* TO DO: Define history buffers and Rd/Wr pointers*/
/* Your code here */

/*
 *
 *  main( )
 *
 */
void main( void )
{   
	int i, j;
	Int32 number_of_blocks;
	/* Initialize BSL */
	EZDSP5535_init( );


	/* Initialise hardware interface and I2C for code */
	aic3204_hardware_init();

	aic3204_set_input_filename("12.wav");
	aic3204_set_output_filename("out_signal1.wav");

	/* Initialise the AIC3204 codec */
	aic3204_init();

	aic3204_dma_init();

	aic3204_read_wav_header(&inputWAVhdr);

	// Set up output WAV header
	outputWAVhdr = inputWAVhdr;

	number_of_blocks = inputWAVhdr.data.SubChunk2Size/
				(inputWAVhdr.fmt.NumChannels*inputWAVhdr.fmt.BitsPerSample*AUDIO_IO_SIZE/8);

	aic3204_write_wav_header(&outputWAVhdr);

    /* TO DO: Initialize history buffers to 0 */
	for(i = 0; i < ARRAY_SIZE(history1); i++){
		history1[i] = 0;
	}

	for(i = 0; i < ARRAY_SIZE(history2); i++){
		history2[i] = 0;
	}


	for(i = 0; i < number_of_blocks; ++i)
	{
		aic3204_read_block(InputBufferL, InputBufferR);

		/* TO DO: Invoke filtering routine */
		/* Your code here */

		for(j = 0; j < AUDIO_IO_SIZE; j++)
		{
			OutputBufferL[j] = fir_circular(InputBufferL[j], low_pass_34th_order_650hz, history1, ARRAY_SIZE(history1), &state1, 3);
			OutputBufferR[j] = OutputBufferL[j];

//			OutputBufferL[j] = fir_circular(InputBufferL[j], band_stop_295hz_305hz, history2, ARRAY_SIZE(history2), &state2, 3);
//			OutputBufferR[j] = OutputBufferL[j];


		}
		aic3204_write_block(OutputBufferL, OutputBufferR);
	}
    	
	/* Disable I2S and put codec into reset */ 
    aic3204_disable();

    printf( "\n***Program has Terminated***\n" );
	SW_BREAKPOINT;
}

