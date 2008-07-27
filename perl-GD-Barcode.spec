%include	/usr/lib/rpm/macros.perl
%define		pdir	GD
%define		pnam	Barcode
Summary:	GD::Barcode Perl module - create barcode image with GD
Summary(pl.UTF-8):	Moduł Perla GD::Barcode - do tworzenia obrazów z kodem paskowym
Name:		perl-GD-Barcode
Version:	1.15
Release:	3
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	53788170efb00b671ffb6ced5b5b897b
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-GD
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD::Barcode is a subclass of GD and allows you to create barcode image
with GD.

%description -l pl.UTF-8
GD::Barcode jest podklasą klasy GD, pozwalającą na tworzenie obrazów
z kodem paskowym przy użyciu GD.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

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
