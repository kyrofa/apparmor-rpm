Name:     apparmor
Version:  2.11.0
Release:  1%{?dist}
Summary:  User-space parser utility for AppArmor

License:  BSD
URL:      http://wiki.apparmor.net/index.php/Main_Page
Source0:  https://launchpad.net/apparmor/2.11/2.11/+download/apparmor-%{version}.tar.gz
Patch0:   fix-podsyntax.patch

BuildRequires: bison, dejagnu, flex, gcc, gcc-c++, gettext, libstdc++-static, perl-Pod-Checker, perl-Pod-Html, pyflakes, which


%description
This provides the system initialization scripts needed to use the
AppArmor Mandatory Access Control system, including the AppArmor Parser
which is required to convert AppArmor text profiles into machine-readable
policies that are loaded into the kernel for use with the AppArmor Linux
Security Module.


%package libs
Summary: Libraries for %{name}

%description libs
Libraries for running %{name} applications.


%prep
%autosetup -p0


%build
(
  cd libraries/libapparmor
  %configure
  %make_build
)

%make_build -C binutils
%make_build -C utils
%make_build -C parser
%make_build -C profiles

%check
make check -C libraries/libapparmor
make check -C binutils
make check -C utils
make check -C parser
make check -C profiles


%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%install
%make_install -C libraries/libapparmor
%make_install -C binutils
%make_install -C utils
%make_install -C parser
%make_install -C profiles


%files
%license LICENSE
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Sep 25 2017 Kyle Fazzari <kyrofa@ubuntu.com> - 2.11.0-1
- Initial version of the package
