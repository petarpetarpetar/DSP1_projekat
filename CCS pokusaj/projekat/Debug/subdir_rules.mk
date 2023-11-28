################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Each subdirectory must supply rules for building sources it contributes
WAVheader.obj: ../WAVheader.c $(GEN_OPTS) $(GEN_HDRS)
	@echo 'Building file: $<'
	@echo 'Invoking: C5500 Compiler'
	"" -v5515 --memory_model=large -O0 -g --include_path="/include" --include_path="C:/Users/petar/Desktop/projekat/c55xx_csl/inc" --include_path="C:/Users/petar/Desktop/projekat/include" --define=c5535 --diag_warning=225 --ptrdiff_size=16 --preproc_with_compile --preproc_dependency="WAVheader.d" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: $<'
	@echo ' '

aic3204.obj: ../aic3204.c $(GEN_OPTS) $(GEN_HDRS)
	@echo 'Building file: $<'
	@echo 'Invoking: C5500 Compiler'
	"" -v5515 --memory_model=large -O0 -g --include_path="/include" --include_path="C:/Users/petar/Desktop/projekat/c55xx_csl/inc" --include_path="C:/Users/petar/Desktop/projekat/include" --define=c5535 --diag_warning=225 --ptrdiff_size=16 --preproc_with_compile --preproc_dependency="aic3204.d" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: $<'
	@echo ' '

aic3204_init.obj: ../aic3204_init.c $(GEN_OPTS) $(GEN_HDRS)
	@echo 'Building file: $<'
	@echo 'Invoking: C5500 Compiler'
	"" -v5515 --memory_model=large -O0 -g --include_path="/include" --include_path="C:/Users/petar/Desktop/projekat/c55xx_csl/inc" --include_path="C:/Users/petar/Desktop/projekat/include" --define=c5535 --diag_warning=225 --ptrdiff_size=16 --preproc_with_compile --preproc_dependency="aic3204_init.d" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: $<'
	@echo ' '

ezdsp5535_aic3204_dma.obj: ../ezdsp5535_aic3204_dma.c $(GEN_OPTS) $(GEN_HDRS)
	@echo 'Building file: $<'
	@echo 'Invoking: C5500 Compiler'
	"" -v5515 --memory_model=large -O0 -g --include_path="/include" --include_path="C:/Users/petar/Desktop/projekat/c55xx_csl/inc" --include_path="C:/Users/petar/Desktop/projekat/include" --define=c5535 --diag_warning=225 --ptrdiff_size=16 --preproc_with_compile --preproc_dependency="ezdsp5535_aic3204_dma.d" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: $<'
	@echo ' '

fir.obj: ../fir.c $(GEN_OPTS) $(GEN_HDRS)
	@echo 'Building file: $<'
	@echo 'Invoking: C5500 Compiler'
	"" -v5515 --memory_model=large -O0 -g --include_path="/include" --include_path="C:/Users/petar/Desktop/projekat/c55xx_csl/inc" --include_path="C:/Users/petar/Desktop/projekat/include" --define=c5535 --diag_warning=225 --ptrdiff_size=16 --preproc_with_compile --preproc_dependency="fir.d" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: $<'
	@echo ' '

main.obj: ../main.c $(GEN_OPTS) $(GEN_HDRS)
	@echo 'Building file: $<'
	@echo 'Invoking: C5500 Compiler'
	"" -v5515 --memory_model=large -O0 -g --include_path="/include" --include_path="C:/Users/petar/Desktop/projekat/c55xx_csl/inc" --include_path="C:/Users/petar/Desktop/projekat/include" --define=c5535 --diag_warning=225 --ptrdiff_size=16 --preproc_with_compile --preproc_dependency="main.d" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: $<'
	@echo ' '


