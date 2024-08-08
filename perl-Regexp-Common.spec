#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v18
# autospec commit: f35655a
#
Name     : perl-Regexp-Common
Version  : 2024080801
Release  : 28
URL      : https://cpan.metacpan.org/authors/id/A/AB/ABIGAIL/Regexp-Common-2024080801.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AB/ABIGAIL/Regexp-Common-2024080801.tar.gz
Summary  : 'Provide commonly requested regular expressions'
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Regexp-Common-license = %{version}-%{release}
Requires: perl-Regexp-Common-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
==============================================================================
Release of version 2024080801 of Regexp::Common
==============================================================================

%package dev
Summary: dev components for the perl-Regexp-Common package.
Group: Development
Provides: perl-Regexp-Common-devel = %{version}-%{release}
Requires: perl-Regexp-Common = %{version}-%{release}

%description dev
dev components for the perl-Regexp-Common package.


%package license
Summary: license components for the perl-Regexp-Common package.
Group: Default

%description license
license components for the perl-Regexp-Common package.


%package perl
Summary: perl components for the perl-Regexp-Common package.
Group: Default
Requires: perl-Regexp-Common = %{version}-%{release}

%description perl
perl components for the perl-Regexp-Common package.


%prep
%setup -q -n Regexp-Common-2024080801
cd %{_builddir}/Regexp-Common-2024080801
pushd ..
cp -a Regexp-Common-2024080801 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Regexp-Common
cp %{_builddir}/Regexp-Common-%{version}/COPYRIGHT %{buildroot}/usr/share/package-licenses/perl-Regexp-Common/f5201c2780719096e19947873e0dca740c93ab0d || :
cp %{_builddir}/Regexp-Common-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Regexp-Common/f5201c2780719096e19947873e0dca740c93ab0d || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Regexp::Common.3
/usr/share/man/man3/Regexp::Common::CC.3
/usr/share/man/man3/Regexp::Common::SEN.3
/usr/share/man/man3/Regexp::Common::URI.3
/usr/share/man/man3/Regexp::Common::URI::RFC1035.3
/usr/share/man/man3/Regexp::Common::URI::RFC1738.3
/usr/share/man/man3/Regexp::Common::URI::RFC1808.3
/usr/share/man/man3/Regexp::Common::URI::RFC2384.3
/usr/share/man/man3/Regexp::Common::URI::RFC2396.3
/usr/share/man/man3/Regexp::Common::URI::RFC2806.3
/usr/share/man/man3/Regexp::Common::URI::fax.3
/usr/share/man/man3/Regexp::Common::URI::file.3
/usr/share/man/man3/Regexp::Common::URI::ftp.3
/usr/share/man/man3/Regexp::Common::URI::gopher.3
/usr/share/man/man3/Regexp::Common::URI::http.3
/usr/share/man/man3/Regexp::Common::URI::news.3
/usr/share/man/man3/Regexp::Common::URI::pop.3
/usr/share/man/man3/Regexp::Common::URI::prospero.3
/usr/share/man/man3/Regexp::Common::URI::tel.3
/usr/share/man/man3/Regexp::Common::URI::telnet.3
/usr/share/man/man3/Regexp::Common::URI::tv.3
/usr/share/man/man3/Regexp::Common::URI::wais.3
/usr/share/man/man3/Regexp::Common::_support.3
/usr/share/man/man3/Regexp::Common::balanced.3
/usr/share/man/man3/Regexp::Common::comment.3
/usr/share/man/man3/Regexp::Common::delimited.3
/usr/share/man/man3/Regexp::Common::lingua.3
/usr/share/man/man3/Regexp::Common::list.3
/usr/share/man/man3/Regexp::Common::net.3
/usr/share/man/man3/Regexp::Common::number.3
/usr/share/man/man3/Regexp::Common::profanity.3
/usr/share/man/man3/Regexp::Common::whitespace.3
/usr/share/man/man3/Regexp::Common::zip.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Regexp-Common/f5201c2780719096e19947873e0dca740c93ab0d

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
