%define upstream_name    Pod-PseudoPod-LaTeX
%define upstream_version 1.20110710

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Convert Pod::PseudoPod documents into LaTeX

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

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



