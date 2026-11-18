#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	GD
%define		pnam	Barcode
Summary:	GD::Barcode Perl module - create barcode image with GD
Summary(pl.UTF-8):	Moduł Perla GD::Barcode - do tworzenia obrazów z kodem paskowym
Name:		perl-GD-Barcode
Version:	2.02
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/M/MI/MICHIELB/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	975d474d2552dd6693414881eb2ff472
URL:		https://metacpan.org/release/GD-Barcode
BuildRequires:	perl-GD
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD::Barcode is a subclass of GD and allows you to create barcode image
with GD.

%description -l pl.UTF-8
GD::Barcode jest podklasą klasy GD, pozwalającą na tworzenie obrazów z
kodem paskowym przy użyciu GD.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/GD/Barcode.pm
%{perl_vendorlib}/GD/Barcode
%{_mandir}/man3/*
