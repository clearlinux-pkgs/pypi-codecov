#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-codecov
Version  : 2.1.13
Release  : 49
URL      : https://files.pythonhosted.org/packages/2c/bb/594b26d2c85616be6195a64289c578662678afa4910cef2d3ce8417cf73e/codecov-2.1.13.tar.gz
Source0  : https://files.pythonhosted.org/packages/2c/bb/594b26d2c85616be6195a64289c578662678afa4910cef2d3ce8417cf73e/codecov-2.1.13.tar.gz
Summary  : Hosted coverage reports for GitHub, Bitbucket and Gitlab
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-codecov-bin = %{version}-%{release}
Requires: pypi-codecov-license = %{version}-%{release}
Requires: pypi-codecov-python = %{version}-%{release}
Requires: pypi-codecov-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(coverage)
BuildRequires : pypi(requests)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
🚨🚨 Deprecation Notice 🚨🚨
This uploader is being deprecated by the Codecov team. We recommend migrating to our [new uploader](https://docs.codecov.com/docs/codecov-uploader) as soon as possible to prevent any lapses in coverage. [The new uploader is open source](https://github.com/codecov/uploader), and we highly encourage submitting Issues and Pull Requests.

%package bin
Summary: bin components for the pypi-codecov package.
Group: Binaries
Requires: pypi-codecov-license = %{version}-%{release}

%description bin
bin components for the pypi-codecov package.


%package license
Summary: license components for the pypi-codecov package.
Group: Default

%description license
license components for the pypi-codecov package.


%package python
Summary: python components for the pypi-codecov package.
Group: Default
Requires: pypi-codecov-python3 = %{version}-%{release}

%description python
python components for the pypi-codecov package.


%package python3
Summary: python3 components for the pypi-codecov package.
Group: Default
Requires: python3-core
Provides: pypi(codecov)
Requires: pypi(coverage)
Requires: pypi(requests)

%description python3
python3 components for the pypi-codecov package.


%prep
%setup -q -n codecov-2.1.13
cd %{_builddir}/codecov-2.1.13
pushd ..
cp -a codecov-2.1.13 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1681830484
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-codecov
cp %{_builddir}/codecov-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-codecov/061f495252a8a118c79bd9ace27758087c69f9d8 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/codecov

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-codecov/061f495252a8a118c79bd9ace27758087c69f9d8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
