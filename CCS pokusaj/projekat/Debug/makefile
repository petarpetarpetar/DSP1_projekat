################################################################################
# Automatically-generated file. Do not edit!
################################################################################

SHELL = cmd.exe

GEN_OPTS__FLAG := 
GEN_CMDS__FLAG := 

ORDERED_OBJS += \
"./WAVheader.obj" \
"./aic3204.obj" \
"./aic3204_init.obj" \
"./ezdsp5535_aic3204_dma.obj" \
"./fir.obj" \
"./main.obj" \
"../lnkx.cmd" \
"../c55xx_csl/lib/cslVC5505.lib" \
"../lib/ezdsp5535bsl.lib" \
$(GEN_CMDS__FLAG) \
-lrts55x.lib \
-lezdsp5535bsl.lib \
-lcslVC5505.lib \
-llibc.a \

-include ../makefile.init

RM := DEL /F
RMDIR := RMDIR /S/Q

# All of the sources participating in the build are defined here
-include sources.mk
-include subdir_vars.mk
-include c55xx_csl/lib/subdir_vars.mk
-include lib/subdir_vars.mk
-include subdir_rules.mk
-include c55xx_csl/lib/subdir_rules.mk
-include lib/subdir_rules.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(S_DEPS)),)
-include $(S_DEPS)
endif
ifneq ($(strip $(S_UPPER_DEPS)),)
-include $(S_UPPER_DEPS)
endif
ifneq ($(strip $(S62_DEPS)),)
-include $(S62_DEPS)
endif
ifneq ($(strip $(C64_DEPS)),)
-include $(C64_DEPS)
endif
ifneq ($(strip $(ASM_DEPS)),)
-include $(ASM_DEPS)
endif
ifneq ($(strip $(CC_DEPS)),)
-include $(CC_DEPS)
endif
ifneq ($(strip $(SV7A_DEPS)),)
-include $(SV7A_DEPS)
endif
ifneq ($(strip $(S55_DEPS)),)
-include $(S55_DEPS)
endif
ifneq ($(strip $(C67_DEPS)),)
-include $(C67_DEPS)
endif
ifneq ($(strip $(CLA_DEPS)),)
-include $(CLA_DEPS)
endif
ifneq ($(strip $(C??_DEPS)),)
-include $(C??_DEPS)
endif
ifneq ($(strip $(CPP_DEPS)),)
-include $(CPP_DEPS)
endif
ifneq ($(strip $(S??_DEPS)),)
-include $(S??_DEPS)
endif
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
ifneq ($(strip $(C62_DEPS)),)
-include $(C62_DEPS)
endif
ifneq ($(strip $(CXX_DEPS)),)
-include $(CXX_DEPS)
endif
ifneq ($(strip $(C++_DEPS)),)
-include $(C++_DEPS)
endif
ifneq ($(strip $(ASM_UPPER_DEPS)),)
-include $(ASM_UPPER_DEPS)
endif
ifneq ($(strip $(K_DEPS)),)
-include $(K_DEPS)
endif
ifneq ($(strip $(C43_DEPS)),)
-include $(C43_DEPS)
endif
ifneq ($(strip $(INO_DEPS)),)
-include $(INO_DEPS)
endif
ifneq ($(strip $(S67_DEPS)),)
-include $(S67_DEPS)
endif
ifneq ($(strip $(SA_DEPS)),)
-include $(SA_DEPS)
endif
ifneq ($(strip $(S43_DEPS)),)
-include $(S43_DEPS)
endif
ifneq ($(strip $(OPT_DEPS)),)
-include $(OPT_DEPS)
endif
ifneq ($(strip $(PDE_DEPS)),)
-include $(PDE_DEPS)
endif
ifneq ($(strip $(S64_DEPS)),)
-include $(S64_DEPS)
endif
ifneq ($(strip $(C_UPPER_DEPS)),)
-include $(C_UPPER_DEPS)
endif
ifneq ($(strip $(C55_DEPS)),)
-include $(C55_DEPS)
endif
endif

-include ../makefile.defs

# Add inputs and outputs from these tool invocations to the build variables 
EXE_OUTPUTS += \
Vezba7_sim.out \

EXE_OUTPUTS__QUOTED += \
"Vezba7_sim.out" \

BIN_OUTPUTS += \
Vezba7_sim.hex \

BIN_OUTPUTS__QUOTED += \
"Vezba7_sim.hex" \


# All Target
all: Vezba7_sim.out

# Tool invocations
Vezba7_sim.out: $(OBJS) $(CMD_SRCS) $(LIB_SRCS) $(GEN_CMDS)
	@echo 'Building target: $@'
	@echo 'Invoking: C5500 Linker'
	"" -z -m"Vezba7_sim.map" --stack_size=0x200 --heap_size=0x400 -i"/lib" -i"/include" -i"C:/Users/petar/Desktop/projekat/c55xx_csl/lib" -i"C:/Users/petar/Desktop/projekat/lib" --reread_libs --warn_sections --xml_link_info="vezba-ezdsp_linkInfo.xml" --ram_model --sys_stacksize=0x200 --fill_value=0x0000 -o "Vezba7_sim.out" $(ORDERED_OBJS)
	@echo 'Finished building target: $@'
	@echo ' '

Vezba7_sim.hex: $(EXE_OUTPUTS)
	@echo 'Invoking: C5500 Hex Utility'
	""  -o "Vezba7_sim.hex" $(EXE_OUTPUTS__QUOTED)
	@echo 'Finished building: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) $(EXE_OUTPUTS__QUOTED)$(BIN_OUTPUTS__QUOTED)
	-$(RM) "WAVheader.d" "aic3204.d" "aic3204_init.d" "ezdsp5535_aic3204_dma.d" "fir.d" "main.d" 
	-$(RM) "WAVheader.obj" "aic3204.obj" "aic3204_init.obj" "ezdsp5535_aic3204_dma.obj" "fir.obj" "main.obj" 
	-@echo 'Finished clean'
	-@echo ' '

.PHONY: all clean dependents
.SECONDARY:

-include ../makefile.targets

