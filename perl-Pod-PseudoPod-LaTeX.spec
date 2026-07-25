%define upstream_name    Pod-PseudoPod-LaTeX
%define upstream_version 1.20190729

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    1

Summary:    Convert Pod::PseudoPod documents into LaTeX

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://github.com/chromatic/Pod-PseudoPod-LaTeX
Source0:    https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/Pod-PseudoPod-LaTeX-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires: perl(IO::String)
BuildRequires: perl(Pod::PseudoPod)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build)
BuildRequires: perl(JSON::PP)
BuildRequires: perl-devel

BuildArch: noarch

%description
Convert Pod::PseudoPod documents into LaTeX.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%clean

%files
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/ppod2latex



