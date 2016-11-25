TESTS_ENVIRONMENT = BATS_NO_SUMMARY=1
SUBDIRS           = ohpc_module

# Tests failing with GOMP are remarked with '#' (they are failing with libomp too)

TESTS             = do_ordered.ftest
#TESTS            += do_firstprivate.ftest
#TESTS            += do_lastprivate.ftest
#TESTS            += do_private.ftest
TESTS            += do_reduction.ftest
TESTS            += do_schedule_dynamic.ftest
TESTS            += do_schedule_guided.ftest
#TESTS            += do_schedule_static.ftest
TESTS            += has_openmp.ftest
TESTS            += omp_atomic.ftest
TESTS            += omp_barrier.ftest
TESTS            += omp_copyin.ftest
TESTS            += omp_critical.ftest
TESTS            += omp_flush.ftest
#TESTS            += omp_get_num_threads.ftest
#TESTS            += omp_in_parallel.ftest
TESTS            += omp_lock.ftest
TESTS            += omp_master.ftest
TESTS            += omp_nest_lock.ftest
TESTS            += omp_test_nest_lock.ftest
TESTS            += omp_nested.ftest
#TESTS            += omp_num_threads.ftest
TESTS            += omp_testlock.ftest
TESTS            += omp_threadprivate.ftest
TESTS            += omp_get_wticks.ftest
#TESTS            += omp_workshare_default.ftest
TESTS            += omp_workshare.ftest
TESTS            += omp_wtime.ftest
TESTS            += par_do_firstprivate.ftest
TESTS            += par_do_lastprivate.ftest
#TESTS            += par_do_ordered.ftest
TESTS            += par_do_private.ftest
TESTS            += par_do_reduction.ftest
TESTS            += par_section_firstprivate.ftest
TESTS            += par_section_lastprivate.ftest
TESTS            += par_section_private.ftest
TESTS            += par_section_reduct.ftest
TESTS            += section_firstprivate.ftest
TESTS            += section_lastprivate.ftest
TESTS            += section_private.ftest
TESTS            += section_reduction.ftest
TESTS            += omp_single.ftest
TESTS            += single_copyprivate.ftest
TESTS            += single_nowait.ftest
TESTS            += single_private.ftest
TESTS            += do_collapse.ftest
TESTS            += omp_master_3.ftest
TESTS            += omp_task.ftest
TESTS            += omp_task_if.ftest
#TESTS            += omp_task_untied.ftest
TESTS            += omp_task_shared.ftest
TESTS            += omp_task_private.ftest
TESTS            += omp_task_firstprivate.ftest
TESTS            += omp_taskwait.ftest
#TESTS            += omp_taskyield.ftest
#TESTS            += omp_task_final.ftest

TESTS            += has_openmp.ctest
TESTS            += omp_atomic.ctest
TESTS            += omp_barrier.ctest
TESTS            += omp_critical.ctest
TESTS            += omp_flush.ctest
TESTS            += omp_for_firstprivate.ctest
TESTS            += omp_for_lastprivate.ctest
TESTS            += omp_for_ordered.ctest
TESTS            += omp_for_private.ctest
TESTS            += omp_for_reduction.ctest
TESTS            += omp_for_schedule_dynamic.ctest
TESTS            += omp_for_schedule_static.ctest
TESTS            += omp_for_nowait.ctest
TESTS            += omp_get_num_threads.ctest
TESTS            += omp_get_wtick.ctest
TESTS            += omp_get_wtime.ctest
TESTS            += omp_in_parallel.ctest
TESTS            += omp_lock.ctest
TESTS            += omp_master.ctest
TESTS            += omp_nest_lock.ctest
TESTS            += omp_parallel_copyin.ctest
TESTS            += omp_parallel_for_firstprivate.ctest
TESTS            += omp_parallel_for_lastprivate.ctest
TESTS            += omp_parallel_for_ordered.ctest
TESTS            += omp_parallel_for_private.ctest
TESTS            += omp_parallel_for_reduction.ctest
TESTS            += omp_parallel_num_threads.ctest
TESTS            += omp_parallel_sections_firstprivate.ctest
TESTS            += omp_parallel_sections_lastprivate.ctest
TESTS            += omp_parallel_sections_private.ctest
TESTS            += omp_parallel_sections_reduction.ctest
TESTS            += omp_section_firstprivate.ctest
TESTS            += omp_section_lastprivate.ctest
TESTS            += omp_section_private.ctest
TESTS            += omp_sections_reduction.ctest
TESTS            += omp_sections_nowait.ctest
TESTS            += omp_parallel_for_if.ctest
TESTS            += omp_single_copyprivate.ctest
TESTS            += omp_single_nowait.ctest
TESTS            += omp_single_private.ctest
TESTS            += omp_single.ctest
TESTS            += omp_test_lock.ctest
TESTS            += omp_test_nest_lock.ctest
TESTS            += omp_threadprivate.ctest
TESTS            += omp_parallel_default.ctest
TESTS            += omp_parallel_shared.ctest
TESTS            += omp_parallel_private.ctest
TESTS            += omp_parallel_firstprivate.ctest
TESTS            += omp_parallel_if.ctest
TESTS            += omp_parallel_reduction.ctest
TESTS            += omp_for_collapse.ctest
TESTS            += omp_master_3.ctest
TESTS            += omp_task.ctest
TESTS            += omp_task_if.ctest
#TESTS            += omp_task_untied.ctest
TESTS            += omp_task_shared.ctest
TESTS            += omp_task_private.ctest
TESTS            += omp_task_firstprivate.ctest
TESTS            += omp_taskwait.ctest
#TESTS            += omp_taskyield.ctest
#TESTS            += omp_task_final.ctest

# General Makefile containing all the necessary compiler flags for the tests

# modify CC and CFLAGS for OpenMP C compilers
# modify FC and FFLAGS for OpenMP Fortran compilers


# Content:
#########################################################

# 1. Basic usage
# 2. General testsuite settings
# 3. Compiler selection and Flags

#########################################################


#########################################################
# 1. Basic usage
#########################################################
# 	make ctest		generate c test "ctest"
# 	make ftest		generate fortran test "ftest"
#	make clean		removes all sources and binaries
# 	make cleanall	removes sources,binaries and logfiles


#########################################################
# 2. General testsuite settings
#########################################################

# For general testsuite settings see the configuration file
# ompts.conf

#########################################################
# 3. Compiler selection and Flags
#########################################################

# GNU Compiler
CC     = @CC@
CFLAGS = @CFLAGS@ @LDFLAGS@
FC     = @FC@
FFLAGS = @FCFLAGS@ @LDFLAGS@

# Fujitsu Compilers:
#CC = fcc
#CFLAGS = -KOMP,fast_GP2=2
#FC=frt
#FFLAGS=-KOMP,fast_GP2=2 -w -Am -X9 -Fixed


# PGI compilers
#CC = pgcc
#CFLAGS = -mp
#CFLAGS = -mp -DVERBOSE
#CFLAGS = -fast -mp

#FC = pgf90
#FFLAGS = -fast -mp
#FFLAGS = -mp -g


# Intel compilers:
#CC = icc
#CFLAGS = -O3 -ip -openmp
#CFLAGS = -Wall -O0 -openmp
#CFLAGS =  -openmp -lm
#CFLAGS =  -openmp -lm -DVERBOSE

#FC = ifort
#FFLAGS = -openmp -lm -fpp

# Omni compilers:
#CC = ompcc
#CFLAGS = -O3 -lm


# Assure compilers:
#CC = assurec
#CFLAGS = -O3 -WApname=project -DUSE_ASSURE=1
#FC =
#FFLAGS =

# NEC:
#CC = c++
#CC = sxc++
#CFLAGS = -Popenmp

#FC=sxf90
#FFLAGS= -Popenmp


# Hitachi:
#CC = xcc
#CFLAGS = -O4 -pvec +Op -parallel -omp
#FC =
#FFLAGS =


# SGI:
#CC = cc
#CFLAGS = -mp -lm
#FC =
#FFLAGS =


# IBM compilers:
#CC = xlc_r
#CFLAGS = -qsmp=omp -lm


#FC=xlf90_r
#FFLAGS=-qsmp=omp -qfixed=132 -qlanglvl=extended


# SUN compilers
#CC = cc
#CFLAGS = -fast -xopenmp -lm

#FC =f90
#FFLAGS = -xopenmp -fast -lm


# open64 compilers
# remark: -I. was a workaround because the installation came without omp.h file
#CC = opencc
#CFLAGS = -O0 -openmp -lm -I. -lomp -lpthread
#CFLAGS = -O0 -openmp -lm -I /home/matthew/opt/usr/include -lpthread
#CFLAGS = -openmp -lm

#FC = openf90
#FFLAGS = -O0 -openmp -lm  -lomp -lpthread


#Pathscale Compiler
#CC = pathcc
#CFLAGS = -mp -Ofast -lm

#FC=pathf90
#FFLAGS= -mp -Ofast -lm


#OpenUH Compiler
#CC = uhcc
#CFLAGS = -mp

#FC = uhf90
#FFLAGS = -mp

#########################################################################

help:
	@echo "OpenMP Validation Suite, v3.0"
	@echo "(C) University of Stuttgart, University of Houston"
	@echo ""
	@echo "Do make [rule], where rule may be one of:"
	@echo "  ctest"
	@echo "    Build and run the OpenMP/C validation tests."
	@echo "  ftest"
	@echo "    Build and run the OpenMP/Fortran validation tests."
	@echo "  print_compile_options"
	@echo "    Display the default compiler and compiler options being tested"
	@echo "  cleansrcs"
	@echo "    Remove sources generated from the templates"
	@echo "  cleanbins"
	@echo "    Remove executables from bin/ directory"
	@echo "  cleanouts"
	@echo "    Remove all *.out files from bin/ directory"
	@echo "  cleanlogs"
	@echo "    Remove all *.log files from bin/ directory"
	@echo "  clean"
	@echo "    Remove all sources and executables from bin/ directory"
	@echo "  cleanall"
	@echo "    Remove the entire bin/ directory"

omp_my_sleep:
	mkdir -p bin/c
	cp omp_my_sleep.h bin/c/
	mkdir -p bin/fortran
	cp omp_my_sleep.f bin/fortran/
omp_testsuite: omp_testsuite.h
	mkdir -p bin/c
	cp omp_testsuite.h bin/c/
	mkdir -p bin/fortran
	cp omp_testsuite.f bin/fortran/
omp_testsuite.h: ompts-c.conf c/*
	./ompts_makeHeader.pl -f=ompts-c.conf -t=c
.c.o: omp_testsuite omp_my_sleep
	$(CC) $(CFLAGS) -c $<
.f.o: omp_my_sleep omp_testsuite
	$(FC) $(FFLAGS) -c $<
%.ctest: omp_my_sleep omp_testsuite
	@ln -sf runctest $@
%.ftest: omp_my_sleep omp_testsuite
	@ln -sf runftest $@

ctest: omp_my_sleep omp_testsuite
	./runtest.pl --lang=c testlist-c.txt

ftest: omp_my_sleep omp_testsuite
	./runtest.pl --lang=fortran testlist-f.txt

print_compile_options:
	@echo "-------------------"
	@echo "C compiler"
	@echo "-------------------"
	@echo "compilation: $(CC) $(CFLAGS)"
	@$(CC) --version
	@echo "-------------------"
	@echo "Fortran compiler"
	@echo "-------------------"
	@echo "compilation: $(FC) $(FFLAGS)"
	@$(FC) --version

cleansrcs:
	find bin/ -iname "*.[cf]" -exec rm {} \;
cleanbins:
	find bin/ -perm /a+x -type f -exec rm {} \;
cleanouts:
	find bin/ -iname "*.out" -exec rm {} \;
cleanlogs:
	find bin/ -iname "*.log" -exec rm {} \;
cleanlinks:
	rm -f *.ftest
	rm -f *.ctest

clean: cleansrcs cleanbins cleanlinks

cleanall: cleanlinks
	rm -rf bin/
