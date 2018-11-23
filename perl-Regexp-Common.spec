#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Regexp-Common
Version  : 2017060201
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/A/AB/ABIGAIL/Regexp-Common-2017060201.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AB/ABIGAIL/Regexp-Common-2017060201.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libr/libregexp-common-perl/libregexp-common-perl_2017060201-1.debian.tar.xz
Summary  : 'Provide commonly requested regular expressions'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-2.0 BSD-3-Clause GPL-1.0 GPL-2.0 MIT MPL-2.0
Requires: perl-Regexp-Common-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
==============================================================================
Release of version 2017060201 of Regexp::Common
==============================================================================

%package dev
Summary: dev components for the perl-Regexp-Common package.
Group: Development
Provides: perl-Regexp-Common-devel = %{version}-%{release}

%description dev
dev components for the perl-Regexp-Common package.


%package license
Summary: license components for the perl-Regexp-Common package.
Group: Default

%description license
license components for the perl-Regexp-Common package.


%prep
%setup -q -n Regexp-Common-2017060201
cd ..
%setup -q -T -D -n Regexp-Common-2017060201 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Regexp-Common-2017060201/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Regexp-Common
cp COPYRIGHT %{buildroot}/usr/share/package-licenses/perl-Regexp-Common/COPYRIGHT
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Regexp-Common/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Regexp-Common/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/CC.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/SEN.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/URI.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/URI/RFC1035.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/URI/RFC1738.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/URI/RFC1808.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/URI/RFC2384.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/URI/RFC2396.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/URI/RFC2806.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/URI/fax.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/URI/file.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/URI/ftp.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/URI/gopher.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/URI/http.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/URI/news.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/URI/pop.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/URI/prospero.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/URI/tel.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/URI/telnet.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/URI/tv.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/URI/wais.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/_support.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/balanced.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/comment.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/delimited.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/lingua.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/list.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/net.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/number.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/profanity.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/whitespace.pm
/usr/lib/perl5/vendor_perl/5.28.0/Regexp/Common/zip.pm

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
/usr/share/package-licenses/perl-Regexp-Common/COPYRIGHT
/usr/share/package-licenses/perl-Regexp-Common/LICENSE
/usr/share/package-licenses/perl-Regexp-Common/deblicense_copyright
