%include	/usr/lib/rpm/macros.perl
%define		pdir	GD
%define		pnam	Barcode
Summary:	GD::Barcode Perl module - create barcode image with GD
Summary(pl):	Modu� Perla GD::Barcode - do tworzenia obraz�w z kodem paskowym
Name:		perl-GD-Barcode
Version:	1.14
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	85aaa2f7722f8011714539476665e0ac
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-GD
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD::Barcode is a subclass of GD and allows you to create barcode image
with GD.

%description -l pl
GD::Barcode jest podklas� klasy GD, pozwalaj�c� na tworzenie obraz�w
z kodem paskowym przy u�yciu GD.

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
