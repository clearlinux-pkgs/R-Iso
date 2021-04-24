#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Iso
Version  : 0.0.18.1
Release  : 31
URL      : https://cran.r-project.org/src/contrib/Iso_0.0-18.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Iso_0.0-18.1.tar.gz
Summary  : Functions to Perform Isotonic Regression
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-Iso-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
isotonic regression; bivariate isotonic regression
	     with linear order on both variables.

%package lib
Summary: lib components for the R-Iso package.
Group: Libraries

%description lib
lib components for the R-Iso package.


%prep
%setup -q -c -n Iso
cd %{_builddir}/Iso

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1590518702

%install
export SOURCE_DATE_EPOCH=1590518702
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Iso
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Iso
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Iso
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc Iso || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Iso/DESCRIPTION
/usr/lib64/R/library/Iso/INDEX
/usr/lib64/R/library/Iso/Isotonic.for
/usr/lib64/R/library/Iso/Meta/Rd.rds
/usr/lib64/R/library/Iso/Meta/data.rds
/usr/lib64/R/library/Iso/Meta/features.rds
/usr/lib64/R/library/Iso/Meta/hsearch.rds
/usr/lib64/R/library/Iso/Meta/links.rds
/usr/lib64/R/library/Iso/Meta/nsInfo.rds
/usr/lib64/R/library/Iso/Meta/package.rds
/usr/lib64/R/library/Iso/Meta/vignette.rds
/usr/lib64/R/library/Iso/NAMESPACE
/usr/lib64/R/library/Iso/R/Iso
/usr/lib64/R/library/Iso/R/Iso.rdb
/usr/lib64/R/library/Iso/R/Iso.rdx
/usr/lib64/R/library/Iso/data/Rdata.rdb
/usr/lib64/R/library/Iso/data/Rdata.rds
/usr/lib64/R/library/Iso/data/Rdata.rdx
/usr/lib64/R/library/Iso/doc/algorithm.R
/usr/lib64/R/library/Iso/doc/algorithm.Rnw
/usr/lib64/R/library/Iso/doc/algorithm.pdf
/usr/lib64/R/library/Iso/doc/index.html
/usr/lib64/R/library/Iso/draft0.tex
/usr/lib64/R/library/Iso/help/AnIndex
/usr/lib64/R/library/Iso/help/Iso.rdb
/usr/lib64/R/library/Iso/help/Iso.rdx
/usr/lib64/R/library/Iso/help/aliases.rds
/usr/lib64/R/library/Iso/help/paths.rds
/usr/lib64/R/library/Iso/html/00Index.html
/usr/lib64/R/library/Iso/html/R.css
/usr/lib64/R/library/Iso/makefor
/usr/lib64/R/library/Iso/pava.r
/usr/lib64/R/library/Iso/smooth.f.orig
/usr/lib64/R/library/Iso/ufit.r
/usr/lib64/R/library/Iso/unimode.r

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/Iso/libs/Iso.so
/usr/lib64/R/library/Iso/libs/Iso.so.avx2
/usr/lib64/R/library/Iso/libs/Iso.so.avx512
