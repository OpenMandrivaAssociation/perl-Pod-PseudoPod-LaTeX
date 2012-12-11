%define upstream_name    Pod-PseudoPod-LaTeX
%define upstream_version 1.101650

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

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
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
%{_bindir}/ppod2latex


%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 1.101.650-3mdv2011.0
+ Revision: 653618
- rebuild for updated spec-helper

* Thu Jul 29 2010 Jérôme Quelin <jquelin@mandriva.org> 1.101.650-2mdv2011.0
+ Revision: 563073
- rebuild

* Wed Jun 23 2010 Jérôme Quelin <jquelin@mandriva.org> 1.101.650-1mdv2011.0
+ Revision: 548677
- update to 1.101650

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 1.101.60-1mdv2010.1
+ Revision: 536220
- update to 1.101060

* Mon Mar 08 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-1mdv2010.1
+ Revision: 515749
- import perl-Pod-PseudoPod-LaTeX


* Mon Mar 08 2010 cpan2dist 1.000-1mdv
- initial mdv release, generated with cpan2dist
