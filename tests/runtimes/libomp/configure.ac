#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.
#

AC_PREREQ(2.59)
AC_INIT([libomp], [3.9.0])
AC_CONFIG_MACRO_DIR([m4])
AM_INIT_AUTOMAKE([foreign])
m4_ifdef([AM_SILENT_RULES], [AM_SILENT_RULES([yes])])

# verify we have necessary environment variables set

AC_MSG_CHECKING([for LIBOMP_LIB environment variable])
if test "x$LIBOMP_LIB" = "x"; then
   AC_MSG_RESULT([no])
   echo
   AC_ERROR([LIBOMP_LIB not defined - please load libomp environment.])
else
   AC_MSG_RESULT([yes])
fi

# unset default compilers and detect compiler toolchain from environment

CC=" "
FC=" "
CFLAGS="-O2 -g -fopenmp"
CXXFLAGS="-O2 -g -fopenmp"
FCFLAGS="-O2 -g -fopenmp"
LDFLAGS="-lm"
LIBS="-lm"

OHPC_COMPILER_FAMILY

# test compilers

AC_PROG_CC
AC_PROG_FC

if test "$LMOD_FAMILY_COMPILER" = "intel"; then
   CFLAGS="${CFLAGS} -fp-model strict"
fi

AM_CONDITIONAL(USE_GNU_COMPILER, test "$LMOD_FAMILY_COMPILER" = "gnu")
AM_COND_IF(USE_GNU_COMPILER, LDFLAGS="${LDFLAGS} ")

# Set subdirectories
AC_CONFIG_FILES(Makefile tests/Makefile tests/ohpc_module/Makefile)

# Configure
AC_OUTPUT()

echo
echo '-------------------------------------------------- SUMMARY --------------------------------------------------'
echo
echo Package version............... : $PACKAGE-$VERSION
echo OHPC compiler toolchain........ : $LMOD_FAMILY_COMPILER
echo
echo C compiler.................... : `which $CC`
echo Fortran compiler.............. : `which $FC`
echo
echo C compiler flags.............. : $CFLAGS
echo Fortran compiler flags........ : $FCFLAGS
echo LDFLAGS linker flags.......... : $LDFLAGS
echo
echo '-------------------------------------------------------------------------------------------------------------'
