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

BuildArch: noarch

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%clean

%files
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/ppod2latex



