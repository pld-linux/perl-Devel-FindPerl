#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Devel
%define		pnam	FindPerl
%include	/usr/lib/rpm/macros.perl
Summary:	Find the path to the current Perl interpreter
Name:		perl-Devel-FindPerl
Version:	0.012
Release:	1
License:	GPL+ or Artistic
Group:		Development/Libraries
Source0:	http://www.cpan.org/authors/id/L/LE/LEONT/Devel-FindPerl-%{version}.tar.gz
# Source0-md5:	d1184cf3a5b3b3d06f75f40944934714
URL:		http://search.cpan.org/dist/Devel-FindPerl/
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
# Run-time:
BuildRequires:	perl(Carp)
BuildRequires:	perl(Config)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(IPC::Open2)
BuildRequires:	perl(Scalar::Util)
# Tests:
%if %{with tests}
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(Test::More)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module tries to find the path to the currently running perl.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README
%{perl_vendorlib}/Devel/FindPerl.pm
%{_mandir}/man3/Devel::FindPerl.3pm*
