#----------------------------------------------------------------------------bh-
# This RPM .spec file is part of the OpenHPC project.
#
# It may have been modified from the default version supplied by the underlying
# release package (if available) in order to apply patches, perform customized
# build/install configurations, and supply additional files to support
# desired integration conventions.
#
#----------------------------------------------------------------------------eh-

# LLVM OpenMP runtime build. This uses the compiler family defined by OHPC.
# Despite its origin, this runtime does not need to be compiled by Clang/LLVM.

#-ohpc-header-comp-begin----------------------------------------------

%include %{_sourcedir}/OHPC_macros
%{!?PROJ_DELIM: %global PROJ_DELIM -ohpc}

# OpenHPC convention: the default assumes the gnu toolchain;
# however, it can be overridden by specifing the
# compiler_family variable via rpmbuild or other

%{!?compiler_family: %global compiler_family gnu}

# Lmod dependency (note that lmod is pre-populated in the OpenHPC OBS build
# environment; if building outside, lmod remains a formal build dependency).
%if !0%{?OHPC_BUILD}
BuildRequires: lmod%{PROJ_DELIM}
%endif

# Compiler dependencies
%if %{compiler_family} == gnu
BuildRequires: gnu-compilers%{PROJ_DELIM}
Requires:      gnu-compilers%{PROJ_DELIM}
%endif
%if %{compiler_family} == intel
BuildRequires: gcc-c++ intel-compilers-devel%{PROJ_DELIM}
Requires:      gcc-c++ intel-compilers-devel%{PROJ_DELIM}
%if 0%{OHPC_BUILD}
BuildRequires: intel_licenses
%endif
%endif

#-ohpc-header-comp-end------------------------------------------------

# Base package name
%define pname libomp

# Build options

Summary:   LLVM OpenMP runtime library (libomp)
Name:      %{pname}-%{compiler_family}%{PROJ_DELIM}
Version:   3.9.0
Release:   1
License:   UIUC
Group:     %{PROJ_NAME}/runtimes
URL:       http://openmp.llvm.org
Source0:   http://llvm.org/releases/3.9.0/openmp-3.9.0.src.tar.xz
Source1:   OHPC_macros
Source2:   OHPC_setup_compiler
Patch1:    0001-Replace-enum-types-in-variadic-functions-by-build-in.patch
Patch2:    0002-Make-balanced-affinity-work-on-AArch64.patch
Patch3:    0003-Disable-KMP_CANCEL_THREADS-on-Android.patch
Patch4:    0004-kmp_taskdeps.cpp-Fix-debugging-output.patch
Patch5:    0005-Add-test-case-for-nested-creation-of-tasks.patch
Patch6:    0006-Fixed-x2APIC-discovery-for-256-processor-architectur.patch
Patch7:    0007-__kmp_free_task-Fix-for-serial-explicit-tasks-produc.patch
Patch8:    0008-Do-not-block-on-explicit-task-depending-on-proxy-tas.patch
Patch9:    0009-Mark-tests-with-task-dependencies-as-unsupported-wit.patch
Patch10:   0010-kmp_gsupport-Fix-library-initialization-with-taskgro.patch
Patch12:   0012-Fixes-for-hierarchical-barrier-possible-hang-if-team.patch
Patch13:   0013-cleanup-fixed-names-of-dummy-arguments-of-Fortran-in.patch
Patch14:   0014-Appease-older-gcc-compilers-for-the-many-microtask-a.patch
Patch15:   0015-Use-critical-reduction-method-when-atomic-is-not-ava.patch
Patch16:   0016-Replace-a-bad-instance-of-__kmp_free-with-KMP_CPU_FR.patch
Patch17:   0017-Decouple-the-kmp_affin_mask_t-type-from-determining-.patch
Patch18:   0018-Move-function-into-cpp-file-under-KMP_AFFINITY_SUPPO.patch
Patch19:   0019-OPENMP-Implementation-of-omp_get_default_device-and-.patch
Patch20:   0020-OPENMP-ppc64le-recognized-as-big-endian.patch
Patch21:   0021-Fix-bitmask-upper-bounds-check.patch
Patch22:   0022-OMPT-extend-ompt-tests-by-checks-for-frame-pointers.patch
Patch23:   0023-OMPT-Align-implementation-of-reenter-frame-address-t.patch
Patch24:   0024-OMPT-Reset-task-exit-frame-when-execution-is-finishe.patch
Patch25:   0025-OMPT-fix-__ompt_get_teaminfo-to-consult-lwt-entries-.patch
Patch26:   0026-OMPT-save-exit-address-to-lwt-if-available.patch
Patch27:   0027-OMPT-fix-task-frame-information-for-gomp-interface.patch
Patch28:   0028-cmake-Make-libgomp-libiomp5-alias-install-optional.patch
Patch29:   0029-Fix-respecting-LIBOMP_LLVM_LIT_EXECUTABLE-as-full-pa.patch
Patch30:   0030-Disable-monitor-thread-creation-by-default.patch
Patch31:   0031-Mixed-type-atomic-routines-for-unsigned-integers.patch
Patch32:   0032-Fix-incorrect-OpenMP-version-in-Fortran-module.patch
Patch33:   0033-test-Support-lit-executable-name.patch
Patch34:   0034-Insert-missing-checks-for-KMP_AFFINITY_CAPABLE-in-af.patch
Patch35:   0035-cmake-Fix-for-a-bug-https-llvm.org-bugs-show_bug.cgi.patch
Patch36:   0036-Enable-omp_get_schedule-to-return-static-steal-type.patch
Patch37:   0037-Code-cleanup-for-the-runtime-without-monitor-thread.patch
Patch38:   0038-Mixed-type-atomic-routines-added-for-capture-and-upd.patch
Patch39:   0039-Fix-a-compile-error-on-musl-libc-due-to-strerror_r-p.patch
Patch40:   0040-Fix-OpenMP-4.0-library-build.patch
Patch41:   0041-OpenMP-Fix-issue-with-directives-used-in-a-macro.patch
Patch42:   0042-Fixed-memory-leak-mistakenly-introduced-by-https-rev.patch
Patch43:   0043-Use-getpagesize-instead-of-PAGE_SIZE-macro-when-KMP_.patch
Patch44:   0044-Fixing-typos-in-__kmp_release_deps-trace-outputs.patch
Patch45:   0045-Fixed-a-memory-leak-related-to-task-dependencies.patch
Patch46:   0046-Add-more-conditions-to-check-whether-task-waiting-is.patch
Patch47:   0047-Fixed-problem-introduced-by-part-of-https-reviews.ll.patch
Patch48:   0048-Change-task-stealing-to-always-get-task-from-head-of.patch
Patch49:   0049-fixed-typo-in-comment.patch
Patch50:   0050-OpenMP-Enable-ThreadSanitizer-to-check-OpenMP-progra.patch
Patch51:   0051-Added-check-for-malloc-return.patch
Patch52:   0052-Introduce-dynamic-affinity-dispatch-capabilities.patch
Patch53:   0053-Update-stats-gathering-code.patch
Patch54:   0054-Fix-for-D25504-segfault-because-of-double-free-ing-i.patch
Patch55:   0055-Set-task-td_dephash-to-NULL-after-free.patch
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-root
DocDir:    %{OHPC_PUB}/doc/contrib
BuildRequires: make
BuildRequires: pkgconfig
BuildRequires: cmake
BuildRequires: python
BuildRequires: hwloc-devel

%description
The LLVM OpenMP runtime library which can be used as drop-in replacement
for GOMP or iomp5.

#!BuildIgnore: post-build-checks rpmlint-Factory

%define debug_package %{nil}

%prep
%setup -q -n openmp-%{version}.src

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1

# Default library install path
%define install_path %{OHPC_LIBS}/%{compiler_family}/%{pname}/%version

%build
# OpenHPC compiler designation
export OHPC_COMPILER_FAMILY=%{compiler_family}
. %{_sourcedir}/OHPC_setup_compiler
mkdir tmp
cd tmp
cmake   -DCMAKE_INSTALL_PREFIX=%{install_path}                          \
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE                              \
        -DCMAKE_BUILD_TYPE:STRING=RELEASE                               \
        -DBUILD_SHARED_LIBS:BOOL=ON                                     \
        -DCMAKE_SKIP_RPATH:BOOL=ON                                      \
        -DLIBOMP_COPY_EXPORTS:BOOL=FALSE                                \
        -DLIBOMP_USE_HWLOC:BOOL=TRUE                                    \
        -DLIBOMP_HWLOC_INSTALL_DIR=`pkg-config --variable=prefix hwloc` \
        -DLIBOMP_OMPT_SUPPORT:BOOL=ON                                   \
        ..
VERBOSE=1 make
cd ..

%install
cd tmp
DESTDIR=%{buildroot} INSTALL='install -p' VERBOSE=1 make install
cd ..
cd $RPM_BUILD_ROOT/%{install_path}/lib
ln -s libgomp.so libgomp.so.1
cd -

# OpenHPC module file
%{__mkdir} -p %{buildroot}%{OHPC_MODULEDEPS}/%{compiler_family}/%{pname}
%{__cat} << EOF > %{buildroot}/%{OHPC_MODULEDEPS}/%{compiler_family}/%{pname}/%{version}
#%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the %{pname} library built with the %{compiler_family} compiler toolchain"
puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname} built with %{compiler_family} toolchain"
module-whatis "Version: %{version}"
module-whatis "Category: runtime library"
module-whatis "Description: %{summary}"
module-whatis "%{url}"

set             version             %{version}

prepend-path    LD_LIBRARY_PATH     %{install_path}/lib

setenv          LIBOMP_DIR          %{install_path}
setenv          LIBOMP_LIB          %{install_path}/lib

EOF

%{__cat} << EOF > %{buildroot}/%{OHPC_MODULEDEPS}/%{compiler_family}/%{pname}/.version.%{version}
#%Module1.0#####################################################################
##
## version file for %{pname}-%{version}
##
set     ModulesVersion      "%{version}"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{OHPC_HOME}
%exclude %{install_path}/include

%changelog
